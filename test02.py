import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import numpy as np

# 超参数
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MAX_LEN = 20
VOCAB_SIZE = 10000
EMBED_SIZE = 512
NUM_HEADS = 8
NUM_LAYERS = 6
FFN_HIDDEN = 2048
DROPOUT = 0.1

# 数据集（简单的占位符实现）
class TranslationDataset(Dataset):
    def __init__(self):
        self.data = [
            ("hello", "bonjour"),
            ("how are you", "comment ça va"),
            ("good morning", "bonjour"),
        ]
        self.src_vocab = {"<PAD>": 0, "<SOS>": 1, "<EOS>": 2, "hello": 3, "how": 4, "are": 5, "you": 6, "good": 7, "morning": 8}
        self.tgt_vocab = {"<PAD>": 0, "<SOS>": 1, "<EOS>": 2, "bonjour": 3, "comment": 4, "ça": 5, "va": 6}
        self.src_vocab_size = len(self.src_vocab)
        self.tgt_vocab_size = len(self.tgt_vocab)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        src, tgt = self.data[idx]
        src_ids = [self.src_vocab[word] for word in src.split()] + [2]  # Add <EOS>
        tgt_ids = [1] + [self.tgt_vocab[word] for word in tgt.split()] + [2]  # Add <SOS> and <EOS>
        return torch.tensor(src_ids), torch.tensor(tgt_ids)

dataset = TranslationDataset()
data_loader = DataLoader(dataset, batch_size=2, shuffle=True)

# 位置编码
class PositionalEncoding(nn.Module):
    def __init__(self, embed_size, max_len):
        super(PositionalEncoding, self).__init__()
        self.encoding = torch.zeros(max_len, embed_size)
        positions = torch.arange(0, max_len).unsqueeze(1).float()
        div_term = torch.exp(torch.arange(0, embed_size, 2).float() * (-np.log(10000.0) / embed_size))
        self.encoding[:, 0::2] = torch.sin(positions * div_term)
        self.encoding[:, 1::2] = torch.cos(positions * div_term)
        self.encoding = self.encoding.unsqueeze(0)

    def forward(self, x):
        seq_len = x.size(1)
        return x + self.encoding[:, :seq_len, :].to(x.device)

# 注意力机制
class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, num_heads, dropout):
        super(MultiHeadAttention, self).__init__()
        assert embed_size % num_heads == 0
        self.num_heads = num_heads
        self.head_dim = embed_size // num_heads
        self.scale = torch.sqrt(torch.tensor(self.head_dim, dtype=torch.float32))
        self.qkv_proj = nn.Linear(embed_size, embed_size * 3)
        self.out_proj = nn.Linear(embed_size, embed_size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, query, key, value, mask=None):
        batch_size, seq_len, embed_size = query.size()
        qkv = self.qkv_proj(query).reshape(batch_size, seq_len, 3, self.num_heads, self.head_dim)
        q, k, v = qkv.unbind(dim=2)
        q, k, v = [x.transpose(1, 2) for x in (q, k, v)]  # [B, num_heads, seq_len, head_dim]

        attn_weights = (q @ k.transpose(-2, -1)) / self.scale
        if mask is not None:
            attn_weights = attn_weights.masked_fill(mask == 0, float("-inf"))
        attn_weights = self.dropout(F.softmax(attn_weights, dim=-1))
        out = (attn_weights @ v).transpose(1, 2).reshape(batch_size, seq_len, embed_size)
        return self.out_proj(out)

# 前馈网络
class FeedForward(nn.Module):
    def __init__(self, embed_size, hidden_dim, dropout):
        super(FeedForward, self).__init__()
        self.ff = nn.Sequential(
            nn.Linear(embed_size, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, embed_size),
            nn.Dropout(dropout)
        )

    def forward(self, x):
        return self.ff(x)

# Transformer Encoder
class TransformerEncoderLayer(nn.Module):
    def __init__(self, embed_size, num_heads, ffn_hidden, dropout):
        super(TransformerEncoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(embed_size, num_heads, dropout)
        self.ff = FeedForward(embed_size, ffn_hidden, dropout)
        self.norm1 = nn.LayerNorm(embed_size)
        self.norm2 = nn.LayerNorm(embed_size)

    def forward(self, x, mask=None):
        x = self.norm1(x + self.self_attn(x, x, x, mask))
        x = self.norm2(x + self.ff(x))
        return x

class TransformerEncoder(nn.Module):
    def __init__(self, num_layers, embed_size, num_heads, ffn_hidden, vocab_size, dropout):
        super(TransformerEncoder, self).__init__()
        self.embed = nn.Embedding(vocab_size, embed_size)
        self.pos_enc = PositionalEncoding(embed_size, MAX_LEN)
        self.layers = nn.ModuleList([TransformerEncoderLayer(embed_size, num_heads, ffn_hidden, dropout) for _ in range(num_layers)])

    def forward(self, x, mask=None):
        x = self.pos_enc(self.embed(x))
        for layer in self.layers:
            x = layer(x, mask)
        return x

# Transformer Decoder
class TransformerDecoderLayer(nn.Module):
    def __init__(self, embed_size, num_heads, ffn_hidden, dropout):
        super(TransformerDecoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(embed_size, num_heads, dropout)
        self.cross_attn = MultiHeadAttention(embed_size, num_heads, dropout)
        self.ff = FeedForward(embed_size, ffn_hidden, dropout)
        self.norm1 = nn.LayerNorm(embed_size)
        self.norm2 = nn.LayerNorm(embed_size)
        self.norm3 = nn.LayerNorm(embed_size)

    def forward(self, x, enc_out, src_mask=None, tgt_mask=None):
        x = self.norm1(x + self.self_attn(x, x, x, tgt_mask))
        x = self.norm2(x + self.cross_attn(x, enc_out, enc_out, src_mask))
        x = self.norm3(x + self.ff(x))
        return x

class TransformerDecoder(nn.Module):
    def __init__(self, num_layers, embed_size, num_heads, ffn_hidden, vocab_size, dropout):
        super(TransformerDecoder, self).__init__()
        self.embed = nn.Embedding(vocab_size, embed_size)
        self.pos_enc = PositionalEncoding(embed_size, MAX_LEN)
        self.layers = nn.ModuleList([TransformerDecoderLayer(embed_size, num_heads, ffn_hidden, dropout) for _ in range(num_layers)])
        self.fc_out = nn.Linear(embed_size, vocab_size)

    def forward(self, x, enc_out, src_mask=None, tgt_mask=None):
        x = self.pos_enc(self.embed(x))
        for layer in self.layers:
            x = layer(x, enc_out, src_mask, tgt_mask)
        return self.fc_out(x)

# Transformer 模型
class Transformer(nn.Module):
    def __init__(self, src_vocab_size, tgt_vocab_size, embed_size, num_layers, num_heads, ffn_hidden, dropout):
        super(Transformer, self).__init__()
        self.encoder = TransformerEncoder(num_layers, embed_size, num_heads, ffn_hidden, src_vocab_size, dropout)
        self.decoder = TransformerDecoder(num_layers, embed_size, num_heads, ffn_hidden, tgt_vocab_size, dropout)

    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        enc_out = self.encoder(src, src_mask)
        out = self.decoder(tgt, enc_out, src_mask, tgt_mask)
        return out

# 初始化模型
model = Transformer(
    src_vocab_size=dataset.src_vocab_size,
    tgt_vocab_size=dataset.tgt_vocab_size,
    embed_size=EMBED_SIZE,
    num_layers=NUM_LAYERS,
    num_heads=NUM_HEADS,
    ffn_hidden=FFN_HIDDEN,
    dropout=DROPOUT
).to(DEVICE)

# 打印模型结构
print(model)

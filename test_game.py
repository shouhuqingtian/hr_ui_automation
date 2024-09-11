# -*- coding: utf-8 -*-
# @Time    : 2024/9/4
# @Author  : Bin
# @Software: PyCharm
# @File    : test_game.py

import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 玩家角色
player_width = 50
player_height = 60
player_x = (screen_width - player_width) / 2
player_y = screen_height - player_height - 10
player_speed = 5

# 障碍物
block_width = 50
block_height = 50
block_speed = 5
block_list = []


# 生成随机障碍物
def create_block():
    x_pos = random.randint(0, screen_width - block_width)
    y_pos = -block_height
    block_list.append([x_pos, y_pos])


# 游戏循环
running = True
clock = pygame.time.Clock()
score = 0

# 主循环
while running:
    screen.fill(WHITE)

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取按键
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # 创建新障碍物
    if random.randint(1, 60) == 1:
        create_block()

    # 绘制障碍物
    for block in block_list:
        block[1] += block_speed
        pygame.draw.rect(screen, RED, (block[0], block[1], block_width, block_height))

        # 检测碰撞
        if (block[0] < player_x < block[0] + block_width or block[0] < player_x + player_width < block[
            0] + block_width) and \
                (block[1] < player_y < block[1] + block_height or block[1] < player_y + player_height < block[
                    1] + block_height):
            running = False  # 碰撞结束游戏

    # 绘制玩家
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))

    # 更新显示
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(60)

# 退出游戏
pygame.quit()

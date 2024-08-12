# -*- coding: utf-8 -*-
# @Time    : 2024/8/9
# @Author  : Bin
# @Software: PyCharm
# @File    : test_sales_order.py

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        self.driver.get("http://192.168.16.50:10006/customer/inquiryBox/inquiryQuotation?type=nav")
        self.driver.set_window_size(1550, 926)
        self.driver.find_element(By.CSS_SELECTOR, "#inquiryListBtns .el-button--success:nth-child(1) > span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".is-required .el-select .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-autocomplete .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-button > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-button > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) > .el-table_4_column_34 > .cell").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-form-item:nth-child(6) > .el-form-item__content > .el-input > .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-form-item:nth-child(6) > .el-form-item__content > .el-input > .el-input__inner").send_keys(
            "7342039")
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-dialog__footer:nth-child(3) .el-button--primary > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-table__body-wrapper .current-row > .el-table_1_column_7 > .cell")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-table__body-wrapper .current-row > .el-table_1_column_7 > .cell")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-table__body-wrapper .current-row > .el-table_1_column_7 > .cell")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "inquiryQuotationTopBox").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__body-wrapper .current-row > .el-table_1_column_7 > .cell").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#inquiryListDetailBtns .el-button--success:nth-child(1) > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "#inquiryListDetailBtns .el-button--success:nth-child(1) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".is-required:nth-child(1) > .el-form-item__content > .el-input > .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".is-required:nth-child(1) > .el-form-item__content > .el-input > .el-input__inner").send_keys(
            "371992")
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(5) .el-form-item:nth-child(6) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(5) .el-form-item:nth-child(6) .el-input__inner").send_keys(
            "测试")
        self.driver.find_element(By.CSS_SELECTOR, ".is-required:nth-child(8) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".is-required:nth-child(8) .el-input__inner").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(5) .el-form-item:nth-child(3) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(5) .el-form-item:nth-child(3) .el-input__inner").send_keys(
            "RCF6708")
        self.driver.find_element(By.CSS_SELECTOR, ".abow_dialog:nth-child(5) .el-button--primary > span").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__body-wrapper .el-table_2_column_3 .el-checkbox__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-button--default").click()
        self.driver.find_element(By.CSS_SELECTOR, "#quotationListBtns .el-button:nth-child(1) > span").click()
        self.driver.find_element(By.CSS_SELECTOR, "#quotationBtns > .el-button:nth-child(1) > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#quotationBtns > .el-button:nth-child(1) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-select .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-form-item__content:nth-child(2) > .el-button > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-form-item__content:nth-child(2) > .el-button > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__row:nth-child(1) > .el-table_6_column_100 > .cell").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-select .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary > span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".vxe-table--body:nth-child(3) .vxe-checkbox--icon").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(6) > span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-row:nth-child(8) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-row:nth-child(7) > .el-col:nth-child(2) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown:nth-child(20) .hover").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(17) .el-dialog__footer .el-button--primary").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(17) > .el-dialog > .el-dialog__header .el-dialog__close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(12) .el-button--default").click()
        self.driver.find_element(By.CSS_SELECTOR, ".vxe-table--body:nth-child(3) .vxe-checkbox--icon").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(6)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-row:nth-child(7) > .el-col:nth-child(2) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown:nth-child(19) .hover").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-row:nth-child(8) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown:nth-child(20) .hover").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-row:nth-child(8) > .el-col:nth-child(1) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(18) .el-dialog__footer").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(18) .el-dialog__footer .el-button--primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-dialog__wrapper:nth-child(18) .el-dialog__footer .el-button--primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(18) > .el-dialog > .el-dialog__header .el-dialog__close").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-table--scrollable-y > .el-table__body-wrapper")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-table--scrollable-y > .el-table__body-wrapper")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-table--scrollable-y > .el-table__body-wrapper")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__body-wrapper .hover-row > .el-table_5_column_75 > .cell").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".is-scrolling-right")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".is-scrolling-right")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".is-scrolling-right")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".is-active .nest-menu:nth-child(3) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".is-active .nest-menu:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".vxe-table--body:nth-child(3) .vxe-checkbox--icon").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "div:nth-child(1) > div > .el-button--primary > span:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "div:nth-child(1) > div > .el-button--primary > span:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--success:nth-child(1) > span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-table_8_column_134 .el-radio__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-table_9_column_148 .el-radio__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--success:nth-child(1) > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--success:nth-child(1) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__row:nth-child(1) > .el-table_10_column_181 .toDetails").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(16) > .el-dialog > .el-dialog__header .el-dialog__close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".current-row > .el-table_10_column_182 > .cell").click()
        self.driver.find_element(By.CSS_SELECTOR, ".has-gutter .el-table_10_column_179 > .cell").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".demo-form-inline > .is-required > .el-form-item__content > .el-input > .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".demo-form-inline > .is-required > .el-form-item__content > .el-input > .el-input__inner").send_keys(
            "·")
        self.driver.find_element(By.CSS_SELECTOR, ".is-required:nth-child(8) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".is-required:nth-child(8) .el-input__inner").send_keys("·")
        self.driver.find_element(By.CSS_SELECTOR, ".width148 > .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".demo-form-inline > .is-success:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".demo-form-inline > .is-success > .el-form-item__content > .el-input > .el-input__inner").send_keys(
            "1")
        self.driver.find_element(By.CSS_SELECTOR, ".is-success:nth-child(8)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".is-success:nth-child(8) .el-input__inner").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, ".is-error").click()
        self.driver.find_element(By.CSS_SELECTOR, ".width148 > .el-input__inner").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, ".paddingBtn2:nth-child(1) > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".paddingBtn2:nth-child(1) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".wutop > .el-dialog__header .el-dialog__close").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__row:nth-child(1) > .el-table_9_column_148 .el-radio__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--success:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".quoteDetailManage1 > .el-dialog > .el-dialog__header .el-dialog__close").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".vxe-table--body:nth-child(3) .vxe-body--row:nth-child(1) .vxe-checkbox--icon").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(6) > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(6) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-row:nth-child(8) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-row:nth-child(8) > .el-col:nth-child(1) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown:nth-child(19) .el-scrollbar__view").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-row:nth-child(7) > .el-col:nth-child(2) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(18) .el-dialog__footer .el-button--primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-dialog__footer:nth-child(3) .el-button--primary > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__fixed-body-wrapper .el-table__row:nth-child(1) .el-button:nth-child(3) > span").click()
        self.driver.find_element(By.CSS_SELECTOR, "#outboundInstructionBtns > .el-button:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#outboundInstructionBtns > .el-button:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-col > .el-col:nth-child(1) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-col > .el-col .el-form-item__content > .el-input > .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-col > .el-col .el-form-item__content > .el-input > .el-input__inner").send_keys(
            "312423")
        self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(6) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(3) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(7) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown:nth-child(20) .hover").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(9) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown:nth-child(21) .hover").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-col-24:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(10) .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown:nth-child(22) .hover").click()
        self.driver.find_element(By.CSS_SELECTOR, ".dialog-footer > .el-button--primary:nth-child(3) > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".dialog-footer > .el-button--primary:nth-child(3) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "div:nth-child(1) > div:nth-child(1) > .el-button--primary:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "div:nth-child(1) > div:nth-child(1) > .el-button--primary:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".wutop > .el-dialog__body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".enginePage:nth-child(3) .el-select__caret")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".wutop > .el-dialog__body").click()
        self.driver.find_element(By.CSS_SELECTOR, ".wutop .commodity").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".wutop .commodity")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__row:nth-child(1) > .el-table_17_column_331 > .cell").click()
        self.driver.find_element(By.CSS_SELECTOR, ".current-row > .el-table_17_column_337 > .cell").click()
        self.driver.find_element(By.CSS_SELECTOR, ".wutop > .el-dialog__footer .el-button--primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".wutop > .el-dialog__footer .el-button--primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(5) .el-dialog__footer:nth-child(3) .el-button--primary > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-dialog__wrapper:nth-child(5) .el-dialog__footer:nth-child(3) .el-button--primary > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(5) .el-dialog__footer:nth-child(3) .el-button--default > span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".wutop .el-dialog__close").click()
        element = self.driver.find_element(By.ID, "outboundInstructionBtns")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "outboundInstructionBtns")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "outboundInstructionBtns")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".father").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".father")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(9) .el-button--default").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(9) .el-button--default")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__body-wrapper .hover-row > .el-table_15_column_287 > .cell").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__body-wrapper .hover-row > .el-table_15_column_287 > .cell").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .el-button:nth-child(1) > .el-icon-plus").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(2) > .el-table_17_column_331").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".current-row > .el-table_17_column_332 > .cell > span:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".wutop > .el-dialog__footer .el-button--primary > span").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(5) .el-dialog__footer:nth-child(3) .el-button--primary > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-dialog__wrapper:nth-child(5) .el-dialog__footer:nth-child(3) .el-button--primary > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__body-wrapper .el-table_16_column_303 .el-checkbox__inner").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "div:nth-child(1) > div > .el-button--primary:nth-child(2) > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "div:nth-child(1) > div > .el-button--primary:nth-child(2) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(6) .el-button--primary > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-dialog__wrapper:nth-child(6) .el-button--primary > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".is-error .el-input__inner").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(6) .el-button--primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown:nth-child(24) .hover").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(6) .el-button--primary > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-dialog__wrapper:nth-child(6) .el-button--primary > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".commodity > .el-dialog__wrapper:nth-child(6) .el-dialog__header").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".commodity > .el-dialog__wrapper:nth-child(6) .el-dialog__close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--default > span:nth-child(2)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--default > span:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__body-wrapper .el-table__row:nth-child(1) > .el-table_15_column_282 .el-checkbox__inner").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-table__fixed-body-wrapper .el-table__row:nth-child(10) .el-button:nth-child(2) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".selectClassTable > .el-table__body-wrapper")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".selectClassTable > .el-table__body-wrapper")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".selectClassTable > .el-table__body-wrapper")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-table__body-wrapper .el-table_16_column_306 .toDetails").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(7) > .productDetails > .el-dialog__header").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(7) > .productDetails > .el-dialog__header").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(7) > .productDetails > .el-dialog__header .el-dialog__close").click()
        self.driver.find_element(By.CSS_SELECTOR, "#outboundInstructionBtns > .el-button:nth-child(3) > span").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-dialog__wrapper:nth-child(25) .el-button--primary > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-dialog__wrapper:nth-child(25) .el-button--primary > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__body-wrapper .el-table_16_column_303 .el-checkbox__inner").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > .el-button--primary:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(6) .el-button--primary > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".el-dialog__wrapper:nth-child(6) .el-button--primary > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".is-error .el-input__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown:nth-child(26) .hover").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(6) .el-button--primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__wrapper:nth-child(6) .el-button--primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".el-table__body-wrapper .el-table__row:nth-child(1) > .el-table_20_column_384 .el-checkbox__inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--success > span:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--success > span:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()


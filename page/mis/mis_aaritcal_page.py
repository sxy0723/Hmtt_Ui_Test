"""后台管理系统--审核文章"""
import time

from selenium.webdriver.common.by import By
from utils import check_channel_option, DriverUtils
from base.mis_base.base_page import BasePage, BaseHandle


# 对象库层
class MisAtcalPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章标题搜索输入框
        self.ari_title_box = (By.CSS_SELECTOR, "[placeholder*='文章']")
        # 选择频道 --->之前已经封装过一个公用下拉框选择的方法
        # 查询按钮
        self.query_btn = (By.CSS_SELECTOR, ".find")
        # 通过按钮
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        # 驳回按钮
        self.reject_btn = (By.XPATH, "//*[text()='驳回']")
        # 通过确认/驳回按钮
        self.con_rej_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # 找到文章标题搜索输入框
    def find_ari_title_box(self):
        return self.find_elt(self.ari_title_box)

    # 找到查询按钮
    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    # 找到通过按钮
    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    # 找到驳回按钮
    def find_reject_btn(self):
        return self.find_elt(self.reject_btn)

    # 找到通过/驳回确认按钮
    def find_con_rej_btn(self):
        return self.find_elt(self.con_rej_btn)


# 操作层
class MisArtcalHandle(BaseHandle):
    def __init__(self):
        self.mis_atcal_page = MisAtcalPage()

    # 文章标题搜索输入框输入
    def input_ari_title(self, ari_title):
        element = self.mis_atcal_page.find_ari_title_box()
        self.input_text(element, ari_title)

    # 选择文章状态
    def check_ari_status(self, ari_status):
        check_channel_option(DriverUtils.get_mis_driver(), "请选择状态", ari_status)

    # 查询按钮点击
    def click_query_btn(self):
        self.mis_atcal_page.find_query_btn().click()

    # 审核通过按钮点击
    def click_aduit_pass_btn(self):
        self.mis_atcal_page.find_pass_btn().click()

    # 驳回按钮点击
    def click_reject_btn(self):
        self.mis_atcal_page.find_reject_btn().click()

    # 审核通过/驳回的确定按钮点击
    def click_confirm_btn(self):
        self.mis_atcal_page.find_con_rej_btn().click()


# 业务层
class MisArcalProxy:
    def __init__(self):
        self.mis_at_hl = MisArtcalHandle()

    # 审核通过的测试用例
    def test_aduit_pass(self, ari_title):
        # 输入搜索的文章名称
        self.mis_at_hl.input_ari_title(ari_title)
        # 选择文章状态
        self.mis_at_hl.check_ari_status("待审核")
        # 点击查询按钮
        self.mis_at_hl.click_query_btn()
        time.sleep(3)
        # 点击通过按钮
        self.mis_at_hl.click_aduit_pass_btn()
        # 点击提示框的确认按钮
        self.mis_at_hl.click_confirm_btn()

    # 审核驳回的测试用例
    def test_reject(self):
        # 选择文章状态
        self.mis_at_hl.check_ari_status("待审核")
        # 点击查询按钮
        self.mis_at_hl.click_query_btn()
        time.sleep(3)
        # 点击驳回按钮
        self.mis_at_hl.click_reject_btn()
        # 点击提示框的确认按钮
        self.mis_at_hl.click_confirm_btn()
        time.sleep(3)
        # 切换审核失败界面
        self.mis_at_hl.check_ari_status("审核失败")
        # 点击查询按钮
        self.mis_at_hl.click_query_btn()
        time.sleep(3)

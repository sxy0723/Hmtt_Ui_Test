from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle


# 定义页面对象类
class MisHomePage(BasePage, BaseHandle):
    # 定义实例属性-->每个元素对象就是页面对象的实例属性
    def __init__(self):
        super().__init__()
        # 信息管理菜单
        self.info_mange_tab = (By.XPATH, "//*[contains(text(),'信息管理')]")
        # 内容审核菜单栏
        self.context_mange_tab = (By.XPATH, "//*[contains(text(),'内容审核')]")

    # 定义实例属性
    def to_aaritcal_page(self):
        self.find_elt(self.info_mange_tab).click()
        self.find_elt(self.context_mange_tab).click()

from selenium import webdriver
from test_package.search_Baidu import Modular_01        #调用类
import unittest

class Test_search_baidu(unittest.TestCase):

    def setUp(self) -> None:

        self.driver=webdriver.Chrome()

    def test_search_Baidu(self):

        information="Python"

        page=Modular_01(self.driver)      #调用Modular_01并关联驱动器

        page.get_url()

        page.search_Baidu(information)       #调用search_Baidu方法并输入值

        self.assertIn(information,page.check_information())    #断言

    def tearDown(self) -> None:

        self.driver.close()
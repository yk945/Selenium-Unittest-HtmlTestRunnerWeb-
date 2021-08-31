'''此文件为封装自动化脚本'''

from test_lib.Element_Find_Method import method            #调用封装好的元素查找方法
from time import sleep
from test_lib.Read_Config import ReadConfig                #调用Read_Config文件

class Modular_01(method):

    url=ReadConfig().get_http()                   #调用get_http方法，获取config.ini中配置的url

    def search_Baidu(self,information):

        self.method_xpath("//input[contains(@id,'kw')]").send_keys(information)

        sleep(1)

        self.method_xpath("//input[contains(@id,'su')]").click()

        sleep(2)

    def check_information(self):

        return self.get_title()                    #获取标题
















    ###################          Design By YK           ##########################
from test_lib.Get_Path_Info import Get_Path
import os
import configparser

path= Get_Path()

config_path=os.path.join(path, '../config.ini')           #获取config.ini文件

config=configparser.ConfigParser()

config.read(config_path,encoding='utf-8')

class ReadConfig():

    def get_http(self):

        return config.get('HTTP',"url")









    ###################          Design By YK           ##########################
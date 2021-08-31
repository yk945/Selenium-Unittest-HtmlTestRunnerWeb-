import os

def Get_Path():

    path=os.path.split(os.path.realpath(__file__))[0]       #获取当前所处的绝对路径

    return path
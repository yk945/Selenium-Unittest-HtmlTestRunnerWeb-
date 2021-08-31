import time
import unittest
import HTMLTestRunner

test_dir="D:/自动化/UI自动化框架/test_case"

def case():

    discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py",top_level_dir=None)       #获取测试用例

    return discover

if __name__=='__main__':

    now=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())

    report_path="D:/自动化/UI自动化框架/test_report/"+now+"-result.html"                                  #报告路径

    file_path=open(report_path,"wb")                                                                   #创建报告

    runner=HTMLTestRunner.HTMLTestRunner(stream=file_path,title=u"UI自动化测试报告",description=u"用例执行结果")         #自定义报告标题

    runner.run(case())

    print("用例执行完成，报告已保存至："+str(report_path))

    file_path.close()


    ###################          Design By YK           ##########################
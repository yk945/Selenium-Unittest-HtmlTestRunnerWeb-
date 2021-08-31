'''此文件可以自行封装selenium方法，在此仅举例几个'''
class method():

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def method_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def method_class_name(self,locator):
        return self.driver.find_element_by_class_name(locator)

    def method_link_text(self,locator):
        return self.driver.find_element_by_link_text(locator)

    def get_text_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator).text

    def get_text_class(self,locator):
        return self.driver.find_element_by_class_name(locator).text

    def get_attribute(self,locator,attribute):
        return self.driver.find_element_by_xpath(locator).get_attribute(attribute)

    def implicitly_wait(self,time):
        return self.driver.implicitly_wait(time)

    def get_title(self):
        return self.driver.title

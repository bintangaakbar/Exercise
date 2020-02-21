from selenium import webdriver
from time import sleep

class instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
    
    def get_unfollowers(self):
            self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
                .click()

instabot('baanugrah__', 'password')

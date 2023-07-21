from selenium import webdriver
import os
demo = os.path.exists("../Driver/chromedriver.exe")
# driver = webdriver.chrome("../Driver/chromedriver.exe")
# in above line we have created an object for chrome class which is present in webdriver module
print(demo)
# driver = webdriver.chrome(r"../Driver/chromedriver.exe")
driver = webdriver.Chrome("../Driver/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.find_element_by_name("username").send_keys("Admin")
driver.implicitly_wait(10)
driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_xpath('button[@type="submit"]').click()
driver.quit()



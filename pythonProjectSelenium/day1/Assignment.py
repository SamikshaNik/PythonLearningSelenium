import time
from selenium import webdriver
driver = webdriver.Chrome("../Driver/chromedriver.exe")
driver.get("https://agiliad.com")
driver.implicitly_wait(10)
HomePageTitle = driver.title
if HomePageTitle == "Agiliad":
    print("HomePageValidation Pass")
    print(HomePageTitle)
else:
    print("HomePageValidation Fail")
driver.implicitly_wait(5)
ProEngText = driver.find_element_by_xpath("//p[contains(text(),'We help our customers realize and accelerate their')]").text
driver.implicitly_wait(5)
print(ProEngText)
SerEngText = driver.find_element_by_xpath("//p[contains(text(),'As part of our Services, we strive to deliver exce')]").text
print(SerEngText)
driver.find_element_by_xpath("//a[@href='/product-engineering/'][normalize-space()='Learn more']").click()
driver.implicitly_wait(7)
Page2Title = driver.title
if Page2Title == "Product Engineering – Agiliad":
    print("Product Engineering PageTitleValidation Pass")
    print(Page2Title)
else:
    print("Product Engineering PageTitleValidation Fail")
driver.find_element_by_link_text("Services").click()
driver.implicitly_wait(7)
Page3Title = driver.title
if Page3Title == "Services – Agiliad":
    print("ServicePageTitleValidation Pass")
    print(Page3Title)
else:
    print("ServicePageTitleValidation Fail")
driver.find_element_by_link_text("Careers").click()
driver.implicitly_wait(7)
Page4Title = driver.title
if Page4Title == "Services – Agiliad":
    print("Careers PageTitleValidation Pass")
    print(Page4Title)
else:
    print("Careers PageTitleValidation Fail")

driver.find_element_by_link_text("About Us").click()
driver.implicitly_wait(7)
Page5Title = driver.title
if Page5Title == "About Us – Agiliad":
    print("About Us PageTitleValidation Pass")
    print(Page5Title)
else:
    print("About Us PageTitleValidation Fail")




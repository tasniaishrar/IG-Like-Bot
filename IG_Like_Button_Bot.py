from selenium import webdriver
from selenium.webdriver import ActionChains
import time

username=input("Input your username: ")
password=input("Input your password: ")
ig_handle=input("IG account to deploy like bot: ")

driver=webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe")
action=ActionChains(driver)
driver.get("https://www.instagram.com/")
time.sleep(2)

#insert username and pass
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)

#click login btn
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(2)

#find search box
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(ig_handle)
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
time.sleep(2)

post_num = driver.find_element_by_class_name("g47SY ").text
time.sleep(2)

driver.find_element_by_class_name('_9AhH0').click()
time.sleep(2)

for photo in range(1,int(post_num)+1):
    if photo==1:
        time.sleep(1)
        action = ActionChains(driver)
        x = action.double_click(driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[1]/div[2]'))
        x.perform()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
    elif photo==post_num:
        time.sleep(1)
        action = ActionChains(driver)
        x = action.double_click(driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[1]/div[2]'))
        x.perform()
    else:
        time.sleep(1)
        action = ActionChains(driver)
        x = action.double_click(driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[2]'))
        x.perform()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()





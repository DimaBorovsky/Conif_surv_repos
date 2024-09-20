from selenium import webdriver
import time
server_name = #server names will appear here in a large string unless any better way to do it

My_driver = webdriver.Chrome()
My_driver.get(f"https://zamsh-incap.{server_name}.infra-net.mobi")

#find the HTML value of the repos that needs to be zeroised
My_driver.find_element(by=,value=).send_keys("0")

#finds the HTML value of the repos that needs to be zeroised
My_driver.find_element(by=,value=).send_keys("0")

My_driver.find_element(by=, value=).click()
time.sleep(5)

actual= My_driver.find_element(by=,value).text

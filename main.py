from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.common.alert import Alert
from time import sleep
import pyautogui
from datetime import datetime
from os import system

print("Enter Your Email")
email = input()
system('cls')
print("Enter Your Password")
psswd = input()
system('cls')     
print("Enter Meeting Code Without Any Special-Character")
code = input()
system('cls')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("Time To Join Class [ Format = H:M:S ] eg. 01:59:20")
time = input()

while current_time != (time):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    system("cls")  
if current_time == (time):
    path = "chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://meet.google.com/new")
    search = driver.find_element_by_name("identifier")
    print(search)
    search.send_keys(email)
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    search = driver.find_element_by_name("password")
    print(search)
    search.send_keys(psswd)
    search.send_keys(Keys.RETURN)
    sleep(3)
    driver.get("https://meet.google.com/lookup/" + code)
    sleep(3)
    driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span").click()
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div").click()
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/div/div").click()
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()




#driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div").click()  # To quit Google Meet

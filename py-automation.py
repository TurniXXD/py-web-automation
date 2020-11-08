from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://web.telegram.org/')

time.sleep(2)

inputfield = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input')
inputfield.send_keys(telNumber) #insert tel number

nextButton = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[1]/div/a')
nextButton.click()

phoneNumberCorrectionButton = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[4]/div[2]/div/div/div[2]/button[2]')
phoneNumberCorrectionButton.click()

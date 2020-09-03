from selenium import webdriver	 

# For using sleep function because selenium 
# works only when all the elements of the page are loaded. 
import time 

from selenium.webdriver.common.keys import Keys 

# Creating an instance webdriver 
browser = webdriver.Chrome(r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
browser.get("https://www.twitter.com") 

# Lets the user see and also load the element 
time.sleep(2) 

login = browser.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]') 

login[0].click() 

print("Login in Twitter") 

user = browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input') 

# Enter User Name 
user[0].send_keys('NEHA GUPTA') 

user = browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input') 

# Reads password from a text file because saving the password in this script makes the password available for others. 
with open('password_page.txt', 'r') as myfile: 
	Password = myfile.read().replace('\n', '') 
user.send_keys(Password) 

LOG = browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]') 
LOG[0].click() 
print("Login is successfully done!") 
time.sleep(5) 

elem = browser.find_element_by_name("q") 
elem.click() 
elem.clear() 

elem.send_keys("Stack Overflow") 

# using keys to send special KEYS 
elem.send_keys(Keys.RETURN) 

print("Search is successfully completed!") 

# closing the browser 
browser.close() 

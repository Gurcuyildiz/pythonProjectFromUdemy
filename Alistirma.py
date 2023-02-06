'''
from selenium import webdriver
from time import sleep
import os
class Bot:
def _init_(self):
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

self.options = webdriver.ChromeOptions()
self.options.headless = True
self.options.add_argument(f'user-agent={user_agent}')
self.options.add_argument("--window-size=1920,1080")
self.options.add_argument('--ignore-certificate-errors')
self.options.add_argument('--allow-running-insecure-content')
self.options.add_argument("--disable-extensions")
self.options.add_argument("--proxy-server='direct://'")
self.options.add_argument("--proxy-bypass-list=*")
self.options.add_argument("--start-maximized")
self.options.add_argument('--disable-gpu')
self.options.add_argument('--disable-dev-shm-usage')
self.options.add_argument('--no-sandbox')
self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options= self.options)
self.driver.get("https://google.com")
self.driver.get_screenshot_as_file("screenshot.png")
print(self.driver.title

###to run the above code to go and take screenshot of google, go to command prompt/terminal,
 write python then the file name with its extension , hit enter will run in headless mode and put a screenshot
 under the screenshot folder
(python app.py)
'''



# ChromeOptions options = new ChromeOptions()
# options.addArguments("--headless")
# options.addArguments("window-size=1280,800")
#we need to define chrome options before driver and pass the options to the driver constructor
#then it will open chorme in headless mode
# webdriver driver = new ChromeDriver(options)





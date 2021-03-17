import pandas as pd
import  time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
driver = webdriver.Ie(executable_path="C:\\Program Files\\Internet Explorer\\IEDriverServer.exe")
driver.get("https://free-ss.site/")
time.sleep(60)

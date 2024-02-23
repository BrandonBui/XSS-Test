from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()

options = ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

uniquePayload = "SjWUxfdW"
urlWithPayload = os.environ["URL"] + uniquePayload

driver.get(urlWithPayload)
sleep(0.1)

html = BeautifulSoup(driver.page_source, "html.parser")
prettyHTML = html.prettify()

for elem in html(text=uniquePayload):
    print(elem.parent)

# driver.save_screenshot("screenshot.png")

# file = open("source.html", "w")
# file.write(driver.page_source)
# file.close()

# file = open("pretty.html", "w")
# file.write(prettyHTML)
# file.close()
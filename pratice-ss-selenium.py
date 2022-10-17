from requests import options
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
options.add_argument("--window-size=1920,1080")


driver = webdriver.Chrome(options=options)
driver.get("https://github.com")
print(driver.title)
driver.get_screenshot_as_file("screenshot.png")
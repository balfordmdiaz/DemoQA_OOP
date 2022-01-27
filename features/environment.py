from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from features.pages.demoQA_formpage import demoqaPage
from dotenv import *
import time

def before_all(context):
    load_dotenv()
    config = dotenv_values(find_dotenv())
    options = Options()
    options.headless = False #para que no se abra la ventana
    context.driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    context.driver.maximize_window()
    context.demoQA = demoqaPage(context.driver)
    context.webQA = config.get("QA_URL")

def after_all(context):
    time.sleep(3)
    context.driver.close()
    context.driver.quit()
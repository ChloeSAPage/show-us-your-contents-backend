from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://show-us-your-contents.netlify.app/")

    # Click on treasures
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Treasures"))
    ).click()

except Exception as error:
    print("Error: ", error)

finally:
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

def perform_full_scroll(driver):
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

driver_manager = ChromeDriverManager()
service = webdriver.ChromeService(
    executable_path=driver_manager.install()
)
driver = webdriver.Chrome(service=service)
driver.get("https://www.imdb.com/")

try:
    # wait for website to load
    print('Waiting for page load...')
    top_10_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'home_img_holder')))
    print('Page loaded. Scrolling down....')
    perform_full_scroll(driver)
    print('Scrolling down...')
    time.sleep(4)

    print('Trying to find Top 10 container...')
    top_10_movies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.top-ten > div.ipc-poster-card"))
    )
    print('Found top 10 container')

    for movie in top_10_movies:
        title_span = movie.find_element(By.CSS_SELECTOR, 'span[data-testid=title]')
        print(title_span.text)

except TimeoutException as te:
    print(te)
    print('Timeout exception')
except Exception as e:
    print(e)
    print('Something went wrong')


# movies = driver.find_elements(By.CSS_SELECTOR, "div[data-testid = 'shoveler-items-container']")





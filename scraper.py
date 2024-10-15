from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_website(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(5)  # Wait for the dynamic content to load
    content = driver.page_source
    driver.quit()
    
    soup = BeautifulSoup(content, 'html.parser')
    return soup.prettify()

def save_to_file(data, filename):
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)
    return file_path

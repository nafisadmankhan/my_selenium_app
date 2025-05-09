import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")  # New headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    # Use the Chrome binary installed by browser-actions/setup-chrome
    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_python_website(browser):
    browser.get("https://www.python.org")
    assert "Python" in browser.title
    download_link = browser.find_element(By.LINK_TEXT, "Downloads")
    assert download_link.is_displayed()
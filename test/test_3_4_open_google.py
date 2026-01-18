import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


@pytest.mark.google
def test_google(driver):
    url = "https://www.google.com/"
    driver.get(url)
    driver = webdriver.Chrome()
    driver.get(url)

    assert driver.title == "Google"
    assert driver.current_url == url

@pytest.mark.selenium
def test_selenium(driver):
    url = "https://github.com/"
    driver.get(url)
    driver = webdriver.Chrome()
    driver.get(url)

    assert (
        driver.title == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub"
    )
    assert driver.current_url == url

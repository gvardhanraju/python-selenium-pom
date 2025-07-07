import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser selection")

@pytest.fixture(scope="function")
def browserControl(request):
    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    driver.get("https://demo.automationtesting.in/Register.html")
    yield driver
    driver.quit()


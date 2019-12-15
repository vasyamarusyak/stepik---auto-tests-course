import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    #browser_name = request.config.getoption("browser_name")
    #browser_name == "firefox"
    browser = webdriver.Chrome() 
    yield browser
    print("\nquit browser..")
    browser.quit()

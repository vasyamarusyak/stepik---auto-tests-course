import pytest
# ^_^
# :-Р
# :)
# .:-Р
# .:3

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

    
@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")

    yield
    print(":3", "\n")



@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_second_smiling_faces(self, prepare_faces, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

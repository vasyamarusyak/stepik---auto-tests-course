import pytest
from selenium import webdriver

# якщо тест неочіквано пройшов а він не мав би пройти, то помічає тест що як упавщий.
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False

#Завдання перевіряє строку із еталонним значенням, якщо воно не співпадає то
# то воно усі неспівпадіння збирає в одну строку і виводить в консолі.
from selenium import webdriver
import pytest
import time
import math

final = '' #пуста строка для введення неспівпадінь


@pytest.fixture(scope="session")
def browser():
    br = webdriver.Chrome()
    yield br
    br.quit()
    print(final)  # напечатать ответ про Сов в конце всей сессии


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])#пераметри для входу на різні сторінки
def test_find_hidden_text(browser, lesson):
    global final # Оператор global объявляет переменную доступной для блока кода, следующим за оператором
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.implicitly_wait(10)#чекаємо елемент до 10 сек  кожні 500 мс чекаємо чи він з*явився
    browser.get(link)
    answer = math.log(int(time.time()))#рахуємо функцію
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))#знаходимо поле і вписуємо відповідь
    browser.find_element_by_css_selector('.submit-submission ').click()
    check_text = browser.find_element_by_css_selector('.smart-hints__hint').text#знаходимо текст і переводимо в текст
    try:
        assert 'Correct!' == check_text
    except AssertionError:
        final += check_text  # собираем ответ про Сов с каждой ошибкой

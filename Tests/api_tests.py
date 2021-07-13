import allure

@allure.story("Тесты для проверки Ассертейшенов")
@allure.step("Тест Ok статус")
def test_ok():
    assert 1 == 1

@allure.story("Тесты для проверки Ассертейшенов")
@allure.step("Тест fail статус")
def test_fail():
    assert 1 == 2

@allure.story("Тесты для проверки Ассертейшенов")
@allure.step("Тест Ok1 статус")
def test_ok1():
    assert 2 == 2


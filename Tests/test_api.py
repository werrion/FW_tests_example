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

"""
 def test_get_variable_type_int1(key_1, key_2, key_3, command, section_var):
        print(f'{script_path} {key_1} {key_2} {key_3} {command} {section_var}')
        result = subprocess.run([script_path,
                                 key_1, key_2, key_3, command, section_var],
                                stdout=subprocess.PIPE, encoding='utf-8')
        print("Тест test_get_variable_type_int1", result.stdout)
        # assert del_inf_result(result.stdout)[29:46] == "UserProfile.money"
        # assert del_inf_result(result.stdout)[49:58] == "VALUE = 0"
        # print("Тест test_get_variable_type_int1", result.stdout)"""

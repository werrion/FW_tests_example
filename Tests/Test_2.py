import subprocess
import allure
from models.Params import Keys, Commands, Sections, Var_name, Values, Section_var
script_path = r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe"

def del_inf_result(text):
    lines = text.split('==========================================')
    res = lines[1]
    return res

@allure.story("Тесты для проверки Базовых операций с переменными")
@allure.step("Тест test_set_variable_type_int1")
def test_set_variable_type_int1(key_1, key_2, key_3, command, section, var_name, value):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section, var_name, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[7:24] == "UserProfile.money"
    assert del_inf_result(result.stdout)[27:49] == "VALUE is setted to - 0"
    print("Тест test_set_variable_type_int1", result.stdout)


def test_set_variable_type_int2(key_1, key_2, key_3, command, section, var_name, value):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section, var_name, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[7:29] == "UserProfile.money_user"
    assert del_inf_result(result.stdout)[32:56] == "VALUE is setted to - 111"
    print("Тест test_set_variable_type_int2", result.stdout)


def test_set_variable_type_str1(key_1, key_2, key_3, command, section, var_name, value):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section, var_name, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[7:24] == "UserProfile.12345"
    assert del_inf_result(result.stdout)[27:53] == "VALUE is setted to - Vasya"
    print("Тест test_set_variable_type_str1", result.stdout)


def test_set_variable_type_float1(key_1, key_2, key_3, command, section, var_name, value):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section, var_name, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[7:26] == "UserProfile.award01"
    assert del_inf_result(result.stdout)[29:53] == "VALUE is setted to - 0.1"
    print("Тест test_set_variable_type_float1", result.stdout)


def test_set_variable_type_array1(key_1, key_2, key_3, command, section, var_name, value):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section, var_name, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[7:28] == "UserProfile.chest(15)"
    assert del_inf_result(result.stdout)[31:57] == "VALUE is setted to - 1 2 3"
    print("Тест test_set_variable_type_array1", result.stdout)


def test_set_variable_type_dict1(key_1, key_2, key_3, command, section, var_name, value):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section, var_name, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[7:27] == "UserProfile.chest.21"
    assert del_inf_result(result.stdout)[30:73] == "VALUE is setted to - {'key1': 1, 'key2': 2}"
    print("Тест test_set_variable_type_dict1", result.stdout)


def test_set_variable_type_none(key_1, key_2, key_3, command, section, var_name, value):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section, var_name, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест test_set_variable_type_none", result.stdout)
    assert del_inf_result(result.stdout)[7:25] == "UserProfile.aw..23"
    #assert del_inf_result(result.stdout)[30:52] == "VALUE is setted to -  "


def test_get_variable_type_int1(key_1, key_2, key_3, command, section_var):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:46] == "UserProfile.money"
    assert del_inf_result(result.stdout)[49:58] == "VALUE = 0"
    print("Тест test_get_variable_type_int1", result.stdout)


def test_get_variable_type_int2(key_1, key_2, key_3, command, section_var):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:51] == "UserProfile.money_user"
    assert del_inf_result(result.stdout)[54:65] == "VALUE = 111"
    print("Тест test_get_variable_type_int2", result.stdout)


def test_get_variable_type_str1(key_1, key_2, key_3, command, section_var):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:46] == "UserProfile.12345"
    assert del_inf_result(result.stdout)[49:62] == "VALUE = Vasya"
    print("Тест test_get_variable_type_str1", result.stdout)


def test_get_variable_type_float1(key_1, key_2, key_3, command, section_var):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:48] == "UserProfile.award01"
    assert del_inf_result(result.stdout)[51:62] == "VALUE = 0.1"
    print("Тест test_get_variable_type_float1", result.stdout)


def test_get_variable_type_array1(key_1, key_2, key_3, command, section_var):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:50] == "UserProfile.chest(15)"
    assert del_inf_result(result.stdout)[53:66] == "VALUE = 1 2 3"
    print("Тест test_get_variable_type_array1", result.stdout)


def test_get_variable_type_dict1(key_1, key_2, key_3, command, section_var):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print(del_inf_result(result.stdout)[29:49])
    assert del_inf_result(result.stdout)[29:49] == "UserProfile.chest.21"
    assert del_inf_result(result.stdout)[52:82] == "VALUE = {'key1': 1, 'key2': 2}"
    print("Тест test_get_variable_type_dict1", result.stdout)





#print(del_inf_result(result.stdout)[32:56])
#if __name__ == '__main__':

# test_set_variable_type_int1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Sections.userprofile, Var_name.name_1, Values.int_1)
# test_set_variable_type_int2(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Sections.userprofile, Var_name.name_2, Values.int_2)
# test_set_variable_type_str1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Sections.userprofile, Var_name.name_7, Values.str_1)
# test_set_variable_type_float1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Sections.userprofile, Var_name.name_3, Values.float_1)
# test_set_variable_type_array1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Sections.userprofile, Var_name.name_4, Values.array_1)
# test_set_variable_type_dict1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Sections.userprofile, Var_name.name_5, Values.dict_1)
# #test_set_variable_type_none(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Sections.userprofile,Var_name.name_9, Values.int_0)
# test_get_variable_type_int1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_1)
# test_get_variable_type_int2(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_2)
#test_get_variable_type_str1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_7)
#test_get_variable_type_float1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_3)
# test_get_variable_type_array1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_4)
#test_get_variable_type_dict1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_5)
test_get_variable_type_dict1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_5)
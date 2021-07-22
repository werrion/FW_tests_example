import subprocess
import allure
from models.Params import Commands, Sections, Var_name, Values, Section_var, Key_param, Timing_val
script_path = r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe"

def read_inf_result(text):
    lines = text.split('\n')
    result = []
    for item in lines:
        result.append(item.split(' '))
    return result

@allure.story("Base varible operations test")
@allure.step("Test_set_variable_type_int1")
def test_set_variable_type_int1(key_param, command, section_var, value):
    result = subprocess.run([script_path, *key_param, command, section_var, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    #assert read_inf_result(result.stdout)[0][2] == Section_var.section_var_1
    #assert read_inf_result(result.stdout)[0][9] == Values.int_1
    # assert read_inf_result(result.stdout)[1][4] == Timing_val.time1
    print("Тест test_set_variable_type_int1", result.stdout)


def test_set_variable_type_int2(key_param, command, section_var, value):
    result = subprocess.run([script_path, *key_param, command, section_var, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert read_inf_result(result.stdout)[0][2] == Section_var.section_var_2
    assert read_inf_result(result.stdout)[0][9] == Values.int_2
    # assert read_inf_result(result.stdout)[1][4] == Timing_val.time1
    print("Тест test_set_variable_type_int2", result.stdout)


def test_set_variable_type_str1(key_param, command, section_var, value):
    result = subprocess.run([script_path, *key_param, command, section_var, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert read_inf_result(result.stdout)[0][2] == Section_var.section_var_7
    assert read_inf_result(result.stdout)[0][9] == Values.str_1
    # assert read_inf_result(result.stdout)[1][4] == Timing_val.time1
    print("Тест test_set_variable_type_str1", result.stdout)


def test_set_variable_type_float1(key_param, command, section_var, value):
    result = subprocess.run([script_path, *key_param, command, section_var, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert read_inf_result(result.stdout)[0][2] == Section_var.section_var_3
    assert read_inf_result(result.stdout)[0][9] == Values.float_1
    # assert read_inf_result(result.stdout)[1][4] == Timing_val.time1
    print("Тест test_set_variable_type_float1", result.stdout)


def test_set_variable_type_array1(key_param, command, section_var, value):
    result = subprocess.run([script_path, *key_param, command, section_var, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert read_inf_result(result.stdout)[0][2] == Section_var.section_var_4
    assert read_inf_result(result.stdout)[0][9] == Values.array_1
    # print("Тест test_set_variable_type_array1", result.stdout)


def test_set_variable_type_dict1(key_param, command, section_var, value):
    result = subprocess.run([script_path, *key_param, command, section_var, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    # assert del_inf_result(result.stdout)[7:27] == "UserProfile.chest.21"
    # assert del_inf_result(result.stdout)[30:73] == "VALUE is setted to - {'key1': 1, 'key2': 2}"
    # print("Тест test_set_variable_type_dict1", result.stdout)


def test_set_variable_type_none(key_param, command, section_var, value):
    result = subprocess.run([script_path, *key_param, command, section_var, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    # print("Тест test_set_variable_type_none", result.stdout)
    #assert del_inf_result(result.stdout)[7:25] == "UserProfile.aw..23"
    #assert del_inf_result(result.stdout)[30:52] == "VALUE is setted to -  "


def test_get_variable_type_int1(key_param, command, section_var):
    result = subprocess.run([script_path, *key_param, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    #assert del_inf_result(result.stdout)[29:46] == "UserProfile.money"
    #assert del_inf_result(result.stdout)[49:58] == "VALUE = 0"
    print("Тест test_get_variable_type_int1", result.stdout)


def test_get_variable_type_int2(key_param, command, section_var):
    result = subprocess.run([script_path, *key_param, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:51] == "UserProfile.money_user"
    assert del_inf_result(result.stdout)[54:65] == "VALUE = 111"
    print("Тест test_get_variable_type_int2", result.stdout)


def test_get_variable_type_str1(key_param, command, section_var):
    result = subprocess.run([script_path, *key_param, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:46] == "UserProfile.12345"
    assert del_inf_result(result.stdout)[49:62] == "VALUE = Vasya"
    print("Тест test_get_variable_type_str1", result.stdout)


def test_get_variable_type_float1(key_param, command, section_var):
    result = subprocess.run([script_path, *key_param, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:48] == "UserProfile.award01"
    assert del_inf_result(result.stdout)[51:62] == "VALUE = 0.1"
    print("Тест test_get_variable_type_float1", result.stdout)


def test_get_variable_type_array1(key_param, command, section_var):
    result = subprocess.run([script_path, *key_param, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:50] == "UserProfile.chest(15)"
    assert del_inf_result(result.stdout)[53:66] == "VALUE = 1 2 3"
    print("Тест test_get_variable_type_array1", result.stdout)


def test_get_variable_type_dict1(key_param, command, section_var):
    result = subprocess.run([script_path, *key_param, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:49] == "UserProfile.chest.21"
    assert del_inf_result(result.stdout)[52:82] == "VALUE = {'key1': 1, 'key2': 2}"
    print("Тест test_get_variable_type_dict1", result.stdout)

"""Требует для правильной работы рабочий вайп- пока не работает - баг 108"""
def test_get_variable_for_create_new_profile(key_param, command, section_var):
    result = subprocess.run([script_path, *key_param, command, section_var],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert del_inf_result(result.stdout)[29:49] == "UserProfile.chest.21"
    assert del_inf_result(result.stdout)[52:60] == "VALUE = "
    FileOpen = open('C:/Users/oleg.krivov/Desktop/FW_tests_example/Util/data/UserProfile.dat', 'r')
    print("Тест test_get_variable_type_dict1", result.stdout)


def test_create_5_variable_and_test_value(key_param, command, section_var, command1, section_var1):
    result = subprocess.run([script_path, *key_param, command, section_var, command1, section_var1],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print(del_inf_result(result.stdout)[32:56])
    #assert del_inf_result(result.stdout)[29:49] == "UserProfile.chest.21"
    #assert del_inf_result(result.stdout)[52:82] == "VALUE = {'key1': 1, 'key2': 2}"
    print("Тест test_get_variable_type_dict1", result.stdout)








#FileOpen = open('C:/Users/oleg.krivov/Desktop/FW_tests_example/Util/data/UserProfile.dat', 'r')




#print(del_inf_result(result.stdout)[32:56])
#if __name__ == '__main__':

test_set_variable_type_int1(Key_param.offline_timing_on_without_wipe, Commands.set, Section_var.section_var_1, Values.int_1)
# test_set_variable_type_int2(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Section_var.section_var_2, Values.int_2)
# test_set_variable_type_str1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Section_var.section_var_7, Values.str_1)
# test_set_variable_type_float1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Section_var.section_var_3, Values.float_1)
# test_set_variable_type_array1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Section_var.section_var_4, Values.array_1)
# test_set_variable_type_dict1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Section_var.section_var_5, Values.dict_1)
# test_set_variable_type_none(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Section_var.section_var_9, Values.int_0)
#test_get_variable_type_int1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_1)
# test_get_variable_type_int2(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_2)
# test_get_variable_type_str1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_7)
# test_get_variable_type_float1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_3)
# test_get_variable_type_array1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_4)
# test_get_variable_type_dict1(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.get, Section_var.section_var_5)
#test_get_variable_for_create_new_profile(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_on, Commands.get, Section_var.section_var_5)

# test_create_10_variable_and_test_value(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_on, Commands.get, Section_var.section_var_5, Commands.get, Section_var.section_var_5)
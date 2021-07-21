import subprocess
script_path = r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe"
def del_inf_result(text):
    lines = text.split('==========================================')
    res = lines[1]
    return res
def test_set_variable_type_int():
    result = subprocess.run([script_path,
                             "0", "1", "0", "set", "UserProfile", "money", "0"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест test_set_variable_type_int", result.stdout)
    print(del_inf_result(result.stdout)[27:49])
    assert del_inf_result(result.stdout)[7:24] == "UserProfile.money"
    assert del_inf_result(result.stdout)[27:49] == "VALUE is setted to - 0"

def test_set_variable_type_float():
    result = subprocess.run([script_path,
                             "0", "1", "0", "set", "UserProfile", "exp", "1.234"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест test_set_variable_type_float", result.stdout)
    assert del_inf_result(result.stdout)[7:22] == "UserProfile.exp"
    assert del_inf_result(result.stdout)[25:51] == "VALUE is setted to - 1.234"
def test_set_variable_type_array():
    result = subprocess.run([script_path,
                             "0", "1", "0", "set", "UserProfile", "inv", "1 2 3"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест test_set_variable_type_array", result.stdout)
    assert del_inf_result(result.stdout)[7:22] == "UserProfile.inv"
    assert del_inf_result(result.stdout)[25:51] == "VALUE is setted to - 1 2 3"
def test_set_variable_type_dict():
    result = subprocess.run([script_path,
                             "0", "1", "0", "set", "UserProfile", "awards", "{'key1': 1, 'key2': 2}"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест test_set_variable_type_array", result.stdout)
    assert del_inf_result(result.stdout)[7:25] == "UserProfile.awards"
    assert del_inf_result(result.stdout)[28:71] == "VALUE is setted to - {'key1': 1, 'key2': 2}"
def test_set_variable_type_none():
    result = subprocess.run([script_path,
                             "0", "1", "0", "set", "UserProfile", "reser5", ""],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест test_set_variable_type_none", result.stdout)
    # print(del_inf_result(result.stdout)[28:49])
    # assert del_inf_result(result.stdout)[7:25] == "UserProfile.reserv"
    # assert del_inf_result(result.stdout)[28:49] == "VALUE is setted to - "
# def test_get_variable_type_array():
#     result = subprocess.run([script_path,
#                             "0", "1", "0", "get", "UserProfile.inv"],
#                             stdout=subprocess.PIPE, encoding='utf-8')
#     print("Тест test_set_variable_type_array", result.stdout)
#     #assert del_inf_result(result.stdout)[7:22] == "UserProfile.inv"
#     #assert del_inf_result(result.stdout)[25:51] == "VALUE is setted to - 1 2 3"

if __name__ == '__main__':
    test_set_variable_type_int()
    # test_set_variable_type_float()
    # test_set_variable_type_array()
    # test_set_variable_type_dict()
    #test_get_variable_type_int()
    #test_get_variable_type_array()
    #test_set_variable_type_none()



# print(del_inf_result(result.stdout)[25:51])
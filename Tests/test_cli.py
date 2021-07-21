import subprocess
script_path = r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe"
key_list = ["0", "1", "0"]
def del_inf_result(text):
    lines = text.split('==========================================')
    res = lines[1]
    return res


def test_set_variable_type_int(key_config):
    result = subprocess.run([script_path,
                             *key_config, "set", "UserProfile", "money", "222"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест test_set_variable_type_int", result.stdout)
    assert del_inf_result(result.stdout)[7:24] == "UserProfile.money"
    assert del_inf_result(result.stdout)[27:51] == "VALUE is setted to - 222"

test_set_variable_type_int(key_list)
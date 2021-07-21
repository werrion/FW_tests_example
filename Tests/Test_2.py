import subprocess
from Test_Params import Keys, Commands, Sections, Var_name, Values
script_path = r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe"

def del_inf_result(text):
    lines = text.split('==========================================')
    res = lines[1]
    return res


def test_set_variable_type_int(key_1, key_2, key_3, command, section, var_name, value):
    result = subprocess.run([script_path,
                             key_1, key_2, key_3, command, section, var_name, value],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест test_set_variable_type_int", result.stdout)
    assert del_inf_result(result.stdout)[7:24] == "UserProfile.money"
    assert del_inf_result(result.stdout)[27:51] == "VALUE is setted to - 111"

test_set_variable_type_int(Keys.network_mode_offline, Keys.timer_on, Keys.wipe_off, Commands.set, Sections.userprofile, Var_name.name_1, Values.int_2)
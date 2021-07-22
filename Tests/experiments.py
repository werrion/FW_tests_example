import subprocess
from models.Params import Commands, Sections, Var_name, Values, Section_var, Key_param
script_path = r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe"

def read_inf_result(text):
    lines = text.split('\n')
    result = []
    for item in lines:
        result.append(item.split(' '))
    return result


def test_set_variable_type_int1(key_param, command, section_var, value, command1, section_var1, value1):
    result = subprocess.run([script_path,
                             *key_param, command, section_var, value, command1, section_var1, value1],
                            stdout=subprocess.PIPE, encoding='utf-8')
    #assert read_inf_result(result.stdout)[0][2] == Section_var.section_var_1
    #assert read_inf_result(result.stdout)[0][9] == Values.int_1
    #assert read_inf_result(result.stdout)[1][4] == 5
    print("Тест test_set_variable_type_int1", result.stdout)


test_set_variable_type_int1(Key_param.offline_timing_on_without_wipe, Commands.set, Section_var.section_var_1, Values.int_1, Commands.set, Section_var.section_var_2, Values.int_2)
#print(result.stdout)
#print(read_inf_result(result.stdout))



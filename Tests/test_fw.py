import subprocess

def test_set_variable_type_int():
    result = subprocess.run([r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe",
                             "0","1","0","set","system.userprofile","money","222"],
                             stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест 1 - Set Var_test", result.stdout)




test_set_variable_type_int()
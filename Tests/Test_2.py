import subprocess

# def test_set_2variable_type_int():
#     result = subprocess.run([r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe",
#                              "1","1","0","set","system.userprofile.money","222",
#                              "set","system.userprofile.exp","111"],
#                              stdout=subprocess.PIPE, encoding='utf-8')
#     print("Тест 1 - Set Var", result.stdout)
#
# def test_Get_variable():
#     result = subprocess.run([r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe",
#                              "1", "1", "0", "get", "system.userprofile.money",
#                              "get", "system.userprofile.exp"],
#                             stdout=subprocess.PIPE, encoding='utf-8')
#     print("Тест 2 - Get var", result.stdout)

def test_Set_variable_dict():
    result = subprocess.run([r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe",
                             "0", "1", "0", "set", "system.userprofile","money","11",
                             "gettype", "system.userprofile.money"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест 2 - Get var", result.stdout)

test_Set_variable_dict()

# test_set_2variable_type_int()
# test_Get_variable()
#assert result.stdout[41:65] == "1VALUE is setted to - 222"
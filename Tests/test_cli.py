import subprocess

#result = subprocess.run([r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe",
                        # "1","1","1","set","system.userprofile.money","222"], stdout=subprocess.PIPE, encoding='utf-8')
#print("Тест 1", result.stdout)
#print(result.stdout[41:65])

#assert result.stdout[41:65] == "VALUE is setted to - 222"
def test_set_variable_type_int():
    result = subprocess.run([r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe",
                             "1","1","0","set","system.userprofile.money","222"],
                             stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест 1 - Set Var", result.stdout)

def test_Get_variable():
    result = subprocess.run([r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe",
                             "1","1","0","get","system.userprofile.money"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    print("Тест 2 - Get var", result.stdout)





test_set_variable_type_int()
test_Get_variable()
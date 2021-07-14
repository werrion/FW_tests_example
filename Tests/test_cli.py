import subprocess

result = subprocess.run([r"C:\Users\oleg.krivov\Desktop\FW_tests_example\Util\ABUtility.exe",
                         "1","1","1","set","system.userprofile.money","222"], stdout=subprocess.PIPE, encoding='utf-8')
print(result.stdout)
print(result.stdout[41:65])

assert result.stdout[41:65] == "VALUE is setted to - 222"

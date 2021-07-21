class Keys:
    """Three first arguments in list are flags:
    1. Framework network mode (1 - online, 0 - offline)
    2. Turn on/off timer for command execution time
    3. Clear saved progress - if "1" - will be erase profile before execute command"""
    network_mode_online = '1'
    network_mode_offline = '0'
    timer_on = '1'
    timer_off = '0'
    wipe_on = '1'
    wipe_off = '0'


class Commands:
    """Three first arguments in list are flags:
    1. Framework network mode (1 - online, 0 - offline)
    2. Turn on/off timer for command execution time
    3. Clear saved progress - if "1" - will be erase profile before execute command"""
    set = 'set'
    get = 'get'
    set_type = 'settype'
    get_type = 'gettype'
    conditional = 'cond'


class Sections:
    """Name sections for tests"""
    userprofile = 'UserProfile'
    levels_config = 'levels_config'


class Var_name:
    """Name sections for tests"""
    name_1 = 'money'
    name_2 = 'money_user'
    name_3 = '!@#$%^'

class Values:
    """different values for tests"""
    int_1 = '1'
    int_2 = '111'
    int_3 = '10003849234783246273647236463487362837'
    int_4 = '-1'
    int_5 = '-12345'
    str_1 = 'Vasya'
    str_2 = 'Вася'
    str_3 = '!@#$%^&*()_+'
    float_1 = '0.1'
    float_2 = '0,1'
    float_3 = '-0,1'
    float_4 = '-0.14546676859867987070790897566456465674'
    bool_true = 'True'
    bool_false = 'False'
    array_1 = '1 2 3'
    array_2 = '1, 2, 3'
    array_3 = 'name, age, gender'
    dict_1 = "{'key1': 1, 'key2': 2}"
    dict_2 = 'key : val, key1 : val1'
    binary_1 = 'path1'
    binary_2 = 'path2'
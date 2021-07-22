
class Key_param:
    offline_timing_on_without_wipe = ["network", "0", "timing", "1"]
    offline_timing_off_without_wipe = ["network", "0", "timing", "0"]
    offline_timing_on_with_wipe = ["network", "0", "timing", "1", "wipe"]
    online_timing_on_without_wipe = ["network 1", "timing", "1"]
    online_timing_off_without_wipe = ["network 1", "timing", "0"]
    online_timing_on_with_wipe = ["network", "1", "timing", "1", "wipe"]


class Commands:
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
    name_0 = ''
    name_1 = 'money'
    name_2 = 'money_user'
    name_3 = 'award01'
    name_4 = 'chest(15)'
    name_5 = 'chest.21'
    name_6 = '!@#$%^'
    name_7 = '12345'
    name_8 = '........'
    name_9 = 'aw..23'

class Section_var:
    section_var_0 = ''
    section_var_1 = 'UserProfile.money'
    section_var_2 = 'UserProfile.money_user'
    section_var_3 = 'UserProfile.award01'
    section_var_4 = 'UserProfile.chest(15)'
    section_var_5 = 'UserProfile.chest.21'
    section_var_6 = 'UserProfile.!@#$%^'
    section_var_7 = 'UserProfile.12345'
    section_var_8 = 'UserProfile.........'
    section_var_9 = 'UserProfile.aw..23'


class Values:
    """different values for tests"""
    int_0 = ''
    int_1 = '0'
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


class Timing_val:
    """Сommand execution time in ms """
    time1 = '1'
    time5 = '5'
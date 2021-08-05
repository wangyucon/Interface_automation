import os

import yaml

def get_project_path():
    '''获取当前项目路径'''
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return BASE_DIR


def read_extract_yaml(yaml_name):
    """
    读取临时变量yaml文件
    :param yaml_name:传入yaml文件名
    :return:

    """
    with open(get_project_path() + '/'+yaml_name, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    return result


def write_extract_yaml(extract_dict):
    """
    将临时变量写入yaml文件
    :param yaml_name:传入临时变量名
    :return:

    """
    with open(get_project_path() + '/extract.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(data={'authorization': extract_dict}, stream=f, allow_unicode=True)


def read_testcase_yaml(yaml_name):
    """
    读取测试用例yaml文件
    :param yaml_name:传入yaml文件名
    :return:

    """
    with open(get_project_path()+'/testcase/'+yaml_name, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        return result


def get_testcase_list():
    '''获取用例集list'''

    resut = []
    list_new = []
    for yaml_file in fileNames(get_project_path()+'/testcase/', '.yaml'):
        resut.append(yaml_file)
    for i in range(0, len(resut)):
        a = read_testcase_yaml(resut[i])
        for j in a:
            list_new.append(j)
    return list_new


def fileNames(root, suffix=None):
    """
    获取指定目录下指定后缀名文件集合
    :param root:传入指定path
    :param root:传入指定文件后缀名
    :return:

    """
    names = os.listdir(root)
    result = []
    if suffix:
        for name in names:
            if os.path.splitext(name)[1] == suffix:
                result.append(name)
    else:
        result = names
    return result


def get_json_value_by_key(in_json, target_key, results=None):
    """
    根据key值读取对应的value值
    :param in_json:传入的json
    :param target_key: 目标key值
    :param results:
    :return:

    """
    if results is None:
        results = []
    if isinstance(in_json, dict):  # 如果输入数据的格式为dict
        for key in in_json.keys():  # 循环获取key
            data = in_json[key]
            get_json_value_by_key(data, target_key, results=results)  # 回归当前key对于的value
            if key == target_key:  # 如果当前key与目标key相同就将当前key的value添加到输出列表
                results.append(data)
    elif isinstance(in_json, list) or isinstance(in_json, tuple):  # 如果输入数据格式为list或者tuple
        for data in in_json:  # 循环当前列表
            get_json_value_by_key(data, target_key, results=results)  # 回归列表的当前的元素
    return results






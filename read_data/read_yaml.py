import yaml

from conftest import BASE_DIR


def build_ui_data():
    # with open('../data/ui_examine_data.yaml', encoding='utf-8') as f:
    with open(BASE_DIR + '/data/ui_examine_data.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        data_list = list()
        for i in data:
            data_list.append((i.get('tencent')))
        print(data_list)
        return data_list  # 返回测试数据


if __name__ == '__main__':
    pass

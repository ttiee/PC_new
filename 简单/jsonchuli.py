import json


json_dic = {'data': {'yesterday': {'date': '8日星期五', 'high': '高温 35℃', 'fx': '东风', 'low': '低温 25℃', 'fl': '<![CDATA[2级]]>', 'type': '晴'}, 'city': '北京', 'forecast': [{'date': '9日星期六', 'high': '高温 34℃', 'fengli': '<![CDATA[2级]]>', 'low': '低温 24℃', 'fengxiang': '北风', 'type': '多云'}, {'date': '10日星期天', 'high': '高温 32℃', 'fengli': '<![CDATA[2级]]>', 'low': '低温 23℃', 'fengxiang': '南风', 'type': '小雨'}, {'date': '11日星期一', 'high': '高温 31℃', 'fengli': '<![CDATA[2级]]>', 'low': '低温 22℃', 'fengxiang': '东南风', 'type': '多云'}, {'date': '12日星期二', 'high': '高温 29℃', 'fengli': '<![CDATA[2级]]>', 'low': '低温 23℃', 'fengxiang': '东北风', 'type': '中雨'}, {'date': '13日星期三', 'high': '高温 30℃', 'fengli': '<![CDATA[2级]]>', 'low': '低温 22℃', 'fengxiang': '北风', 'type': '小雨'}], 'ganmao': '感冒易发期，外出请适当调整衣物，注意补充水分。', 'wendu': '32'}, 'status': 1000, 'desc': 'OK'}


def main1():
    with open('tianqi.json', 'r', encoding='utf-8') as f:
        r = json.load(f)
    with open("tianqi1.json", 'w') as n:
        n.write(json.dumps(r, indent=4))
        json.dump(r, n, indent=4)


def main(dic: dict) -> None:
    with open("01.json", 'w') as n:
        # n.write(json.dumps(dic, indent=4))
        json.dump(dic, n, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main(dic=json_dic)

# coding=utf-8

'''
    序号:033
    功能:有道翻译---使用POST方式抓取数据
    运行条件:安装requests库
    编辑时间:2022/01/28
    作者:奕凌天
'''

import requests
import json
#自定义函数
def get_translate_date(word=None):
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult =rule'
    Form_data = {'i':word, 'from':'AUTO','to': 'AUTO','smartresult': 'dict', 'client':'fanyideskweb',
                'salt':'1512399450582','sign':'78181ebbdcb38de9b4a3f4cd1d3 8816b','doctype':'json',
                'version': '2.1','keyfrom':'fanyi.web','action':'FY_BY_ CLICKBUTTION','typoResult':'false'}	
    # 请求表单数据
    response = requests.post(url, data=Form_data)                
    # 将JSON格式字符串转字典
    content = json.loads(response.text)                  
    # 返回翻译后的数据
    return(content['translateResult'][0][0]['tgt'])

if __name__ == "__main__":

    print("="*25 + "开始翻译" + "="*25)

    result = input('请输入想要翻译的文字:',)

    print("翻译结果是:",get_translate_date(result))

    print("="*25 + "翻译结束" + "="*25)

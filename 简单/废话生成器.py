import requests
import re

# url = 'https://suulnnka.github.io/BullshitGenerator/index.html?主题={}'
url = 'https://api.edwiv.com/bzsy/gen.php?event={0}&length={1}&counterType={2}&isWritten=0'


def get_useless_text(__theme: str = '一天掉多少根头发', __length: int = 6000, __count_type: int = 0) -> str:
    pre_text = requests.get(url=url.format(__theme, __length, __count_type)).text
    __text = pre_text.replace('<br/>', '\n').replace(': ', '\t: ')
    return __text


theme = input('请输入主题：')
length = int(input('请输入字数：'))
text = get_useless_text(__theme=theme, __length=length)
print(text)

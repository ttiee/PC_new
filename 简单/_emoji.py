import emoji


for i, v in emoji.EMOJI_UNICODE.items():
    for j, p in v.items():
        print(p, end=' ')


print('\n')
print('\U0001F601')






# print(emoji)
print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize('Python is :thumbsup:', use_aliases=True))  # 使用别名
# print(emoji.demojize('Python is 👍'))
# print(emoji.EMOJI_UNICODE)
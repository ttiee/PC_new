import re


letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def solve_password(password: str, key: int = 2):
    pd_list = re.split('', password)
    for index, i in enumerate(pd_list):
        if i in letters_list:
            letters_list_index = letters_list.index(i)
            replace_letter = letters_list[(letters_list_index + key)%26]
            pd_list[index] = replace_letter
    end_sentence = ''.join(pd_list)
    return end_sentence

pd = solve_password("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
print(pd)
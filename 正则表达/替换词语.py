import re


def a():
    pattern = r'(shit)|(sb\w+)'
    about = 'shit! sb!6sb SB! 6*SBsb sb吗？ SB吗？ sb!'
    match = re.sub(pattern=pattern, repl='大妈', string=about, flags=re.I)
    print(match)


def b():

    pattern = r"(土狗)|(sb)"
    about = "他是一只土狗吗？他是SB吗"
    match = re.sub(pattern=pattern, repl="达咩", string=about, flags=2)
    print(match)
    print(int(re.I))


b()

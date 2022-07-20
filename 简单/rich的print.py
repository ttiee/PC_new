import time

from rich import print
from rich.console import Console


def main():
    print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")
    con = Console()
    con.print('h [bold cyan]Will[/bold cyan] h', 'hh', style='bold red')


def main2():

    # 采用中括号将颜色包起来，指定在想要改变颜色的字符串的前面即可
    print("[blue]古明地觉是一个连幽灵都为之惧怕的少女")
    # 也可以指定其它属性，比如粗体、斜体、下划线等等
    print("[bold]粗体")
    # 当然也可以同时指定，注意：斜体的话只适用于英文
    print("[bold red]红色粗体")
    print("[italic red]italic red")
    print("[underline red]红色下划线")
    # 当然这些属性是可以搭配使用的
    print("[bold italic underline red]加粗、下划线、红色，但是下划线对中文无效")

    # 一个字符串中可以为不同的部分指定不同的颜色、属性
    print("[italic bold red]komeiji[cyan bold]satori")

    # 但是问题来了，如果我希望只对字符串的某一部分做处理的话该怎么做呢？
    # 比如："komeiji satori" 的 komeiji 指定为绿色粗体，但其它的部分不变，就可以这么做
    # "[bold green]komeiji[/bold green] satori"，将前面的属性在指定部分的后面重新写一遍、并且在开头加上一个 /，表示限定结束位置
    # 如果没有 / ，那么相当于为不同的部分指定不同的颜色属性，指定的 / 则是起一个限定范围的作用
    print("[italic bold red]komeiji[/italic bold red]satori")


def main3():
    print("[italic red]Hello[/italic red] World!", locals())


def main4():
    from rich.progress import Progress
    with Progress() as progress:
        task1 = progress.add_task('[red]Downloading...', total=1000)
        task2 = progress.add_task('[green]Processing...', total=1000)
        task3 = progress.add_task('[cyan]Cooking...', total=1000)

        while not progress.finished:
            progress.update(task1, advance=5)
            progress.update(task2, advance=3)
            progress.update(task3, advance=9)
            time.sleep(0.02)


if __name__ == '__main__':
    # main()
    # main2()
    main3()
    # main4()

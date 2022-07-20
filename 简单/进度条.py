import time
# from rich.console import Console
from rich.progress import Progress


def main():
    with Progress() as progress:
        task1 = progress.add_task('[red]Downloading...', total=1000)
        task2 = progress.add_task('[green]Processing...', total=1000)
        task3 = progress.add_task('[cyan]Cooking...', total=1000)

        while not progress.finished:
            progress.update(task1, advance=5)
            progress.update(task2, advance=3)
            progress.update(task3, advance=9)
            time.sleep(0.02)


def main1():
    def p():
        n = int((input(':')))
        return n

    with Progress() as progress:
        t1 = progress.add_task('01...', total=1000)
        for i in range(1000):
            n = p()
            progress.update(task_id=t1, completed=n)
            time.sleep(1)


# ━ ━ ━━
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40
# ▄▄

if __name__ == '__main__':
    main()
    # main1()
    # print(len('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'))

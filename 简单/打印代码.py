from rich.console import Console
from rich.syntax import Syntax


string = '''
from rich.console import Console
from rich.syntax import Syntax


string = 3


def main():
    syntax = Syntax(string, 'python', theme='monokai', line_numbers=True)
    console = Console()
    console.print(syntax)


if __name__ == '__main__':
    main()


'''


def main():
    syntax = Syntax(string, 'python', theme='monokai', line_numbers=True)
    console = Console()
    console.print(syntax)


if __name__ == '__main__':
    main()

import time
from rich.live import Live
from rich.table import Table
table = Table()
table.add_column('test')
with Live(table, refresh_per_second=4) as live:
    for row in range(12):
        time.sleep(0.4)
        table.add_row('yes')
        live.console.log('log')

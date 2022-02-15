import time
for i in range(1000):
    print("█"*(i//100), i/10, "%\r", end = '')
    time.sleep(0.003)
print('█'*10+'     OK!   ')
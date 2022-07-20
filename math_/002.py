class Jfk:
    day = 0

    def joinjf(self):
        self.day += 1


list1 = []
zjf = 10
days = 0
while True:
    days += 1
    if zjf >= 10:
        list1.append(Jfk())
        zjf -= 10
    for i in list1:
        i.joinjf()
        if i.day > 30:
            list1.remove(i)
    for i in list1:
        zjf += 0.4
    if days > 30:
        break

print(zjf)

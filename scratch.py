#ef genSet(clist):
    #a = list(set(clist))
    #return sorted(a)


#if __name__ == "__main__":
    #print
    #genSet([5, 2, 8, 4, 1, 8])
    #print
    #genSet([3, -2, -4, -8, 6, -9, 0])

a = []
c = int(input("Сколько добавить чисел \n"))
for i in range(0, c):
    if c > 0:
        a.append(input("Введите число \n"))
    else:
        exit()
a.reverse()
print(a)
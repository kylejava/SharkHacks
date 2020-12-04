#get birthday, (month, day, year) and mod by 4
def getBirthday(bithday):
    x = (birthday) % 898

    if x == 0:
        x = x+1
        return x
    elif x != 0:
        return x

print("test")

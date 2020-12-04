#get birthday, (month, day, year) and mod by 4
def getBirthday(bithday):
    x = (birthday) % 898

    if x == 0:
        x = x+1
        return x
    elif x != 0:
        return x


def return_birthday(queue):
    current_num = ""
    num_arr = []
    for i in range(len(queue)):
        if(queue[i].isdigit()):
            current_num += queue[i]
        else:
            num_arr.append(current_num)
            current_num = ""
    num_arr.append(current_num)
    return num_arr


def obtain_date(s):
    num_arr = []
    queue = []
    birthday = 0
    for i in range(len(s)):

        if(s[i].isdigit() or s[i] == '/'):
            queue.append(s[i])


    num_arr = return_birthday(queue)

    for i in range(len(num_arr)):
        num = int(num_arr[i])
        birthday += num

    return birthday

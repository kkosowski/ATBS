def fun(list):
    for i in range(len(list)):
        if len(list)-1 == i:
            print('and', end = ' ')
            print(list[i])
            break
        else:
            print(list[i], end = ', ')


spam = [1,2,3]
fun(spam)

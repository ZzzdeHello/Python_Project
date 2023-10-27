if __name__ == '__main__':
    # x = int(input("Please enter an integer: "))
    x = 2
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')
    # number
    numbers = (1, 2, 3, 4)
    for s in numbers:
        print(s)

    while x <= 9:
        print('The count is:', x)
        x = x + 1
    else:
        print('x 循环结束')
    print(x, " is not less than 6")

    range_demo = range(0,10,2)
    for r in range_demo:
        print(r)
        if r == 6:
            print('this is six continue')
            continue
    range_demo2 = range(0,10,2)
    for r in range_demo2:
        print(r)
        if r == 6:
            print('this is six break')
            break

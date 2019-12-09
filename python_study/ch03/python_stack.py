def push(list, item):
    if len(list) == 5:
        print('Overflow \n')
    if len(list) != 5:
        list.append(item)
        print('push : {} ->\n'.format(list))


def pop():
    if len(list) == 0:
        print('Underflow \n')
    if len(list) != 0:
        del list[len(list)-1]
        print('pop : {} -> \n'.format(list))


def prn_stack():
    for t in list[0:len(list)-1]:  # for 반복문
        print(t)


if __name__ == "__main__":
    list = []
    push(list, 'a')
    push(list, 'b')
    push(list, 'c')
    push(list, 'd')
    push(list, 'e')
    push(list, 'f')
    pop()
    pop()
    pop()
    pop()
    pop()
    pop()

    # prn_stack()


# for t in list[0:len(list)]:
#     print(list)

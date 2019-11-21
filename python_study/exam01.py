# stack 구현

def push(list, item):
    if len(list) == 5:
        print('[Stack Overflow!!]')
    if len(list) != 5:
        print('Push : {}'.format(item))
        list.append(item)


def pop(list):
    if len(list) == 0:
        print('[Stack Underflow!!]')
    if len(list) != 0:
        print('Pop : {}'.format(list[len(list)-1]))
        del list[len(list)-1]


def prn_stack(list):
    prt = 'stack :'
    for t in list[0:len(list):1]:
        prt = prt + ("{} -> ".format(t))
    print(prt + 'END of Stack')


if __name__ == "__main__":
    list = []

    push(list, 'a')
    push(list, 'b')
    push(list, 'c')
    push(list, 'd')
    push(list, 'e')
    push(list, 'f')

    prn_stack(list)

    pop(list)
    pop(list)
    pop(list)
    pop(list)
    pop(list)
    pop(list)

    prn_stack(list)

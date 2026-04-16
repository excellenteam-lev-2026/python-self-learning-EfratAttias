def cup_of_join(*args ,sep='-'):
    l = []

    for i, lst in enumerate(args):
        l.extend(lst)
        if i < len(args) - 1:
            l.append(sep)

    return l

if __name__ == "__main__":
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())
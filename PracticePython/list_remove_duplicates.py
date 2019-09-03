def main():
    a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]
    print(remove_dupes_loop(a))
    print(remove_dupes_set(a))


def remove_dupes_loop(lis: list):
    no_dupes = []
    for i in lis:
        if i not in no_dupes:
            no_dupes.append(i)
    return no_dupes


def remove_dupes_set(lis: list):
    return list(set(lis))


main()

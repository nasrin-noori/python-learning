from typing import List
from itertools import permutations 


def char_split(text: str):
    return [text[index: index + 1] for index in range(0, len(text))]


def count_list_char(xs: list):
    a = {item: 0 for item in xs}
    for item in xs:
        a[item] += 1
    return a


def lookup(short: str, long: List[str]):
    def sampling():
        return [count_list_char(char_split(long[index: index + len(short)])) for index in range(0, len(long) - len(short) + 1)]

    return count_list_char(char_split(short)) in sampling()


def apply_on_permutation(short: str, long: str):
    def permutation_string():
        return list(set(["".join(list(element)) for element in permutations(short)]))
    for item in permutation_string():
        yield lookup(item, long)


if __name__ == '__main__':
    s_1 = "bradsasarstewrwer" #sucess
    t_1 = "wer"

    s_2 = "tytpopaosadasd@"
    t_2 = "daas"

    s_3 = "uiuhapodsdasd"
    t_3 = "hapdos"

    s_4 = "ijijpasdsdasdqwe"
    t_4 = "123534123"

    assert lookup(t_1, s_1), 'failed'
    assert lookup(t_2, s_2), 'failed'
    assert lookup(t_3, s_3), 'failed'
    assert not lookup(t_4, s_4), 'success'

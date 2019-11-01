"""
Joe Vita
10/21/19
CSCI-141 Herring


"""
from dataclasses import dataclass


@dataclass
class box_count:
    __slots__ = "cookie", "count"  # gives errors when attribute spelling mistake
    cookie: str
    count: int


@dataclass
class order:
    __slots__ = "name", "addy", "cost", "paid", "cookies"
    name: str
    addy: str
    cost: float
    paid: bool
    cookies: list  # of box_count


@dataclass
class food:
    __slots__ = "name", "calories", "sugar", "fat"
    name: str
    calories: int
    sugar: float
    fat: float


@dataclass
class dog:
    __slots__ = "name", "breed", "age"
    name: str
    breed: str
    age: int


def main():
    dic()
    sets()
    dataclass()

    box = box_count(cookie='thin mints', count=5)
    print(box.cookie)
    # box.cooky = 'lemonades' #does not give error, adds cooky as attribute unless not in __slots__
    # print(box.cooky)

    donut = food(name='donut', calories=300, sugar=20, fat=20)
    ass = food(name='booty', calories=0, sugar=0, fat=400)

    print()
    print(donut.name)
    print(ass.fat)


def dic():
    dic = {'j': 'Joseph', 'c': 'Charles', 'v': 'Vita', 'b': 'Bruce', 'l': 'Lee', 'h': 'Herring'}
    for x in 'jcv blh':
        if x == ' ':
            print()
        else:
            print(dic[x])
    print()
    print()
    for x in dic:
        print(x, ': ', dic[x])


def sets():
    set1 = set()
    set2 = {1, 3, 5}
    set2.add(8)
    intset = set()
    for x in range(100):
        intset.add(x)
    print()
    print()
    for x in intset:
        print(x, end=" ")


def add_name(dict, first, middle, last):
    dict[first[0:1]] = first
    dict[middle[0:1]] = middle
    dict[last[0:1]] = last
    return dict


def paid(order):
    order.paid = True


def get_box_counts(order):
    return len(order.cookies)
        \


if __name__ == '__main__':
    main()

from dataclasses import dataclass


@dataclass
class coin:
    __slots__ = "name", "denom"
    name: str
    denom: int

PENNY = coin("Penny", 1)
NICKEL = coin("Nickel", 5)
DIME = coin("Dime", 10)
QUARTER = coin("Quarter", 25)
DOLLAR = coin("DOLLAR", 100)

def create_ascii_map(ascii_map):
    for x in range(65, 123):
        ascii_map[chr(x)]


def print_map(map):
    for key in map:
        print(key + ':' + str(map[key]), end=' ')


def map_words(words_map, filename):
    file = open(filename)
    for line in file:
        f_ch = line[0]
        if f_ch in words_map:
            words_map[f_ch] += [line.strip()]
        else:
            words_map[f_ch] = [line.strip()]


def make_change(price, payment):
    change = payment - price
    coins = []
    for x in range(change // 100):
        coins.append(DOLLAR)
    change -= 100 * change // 100
    for x in range(change // 25):
        coins.append(QUARTER)
    change -= 25 * change // 25
    for x in range(change // 1):
        coins.append(DIME)
    change -= 10 * change // 10
    for x in range(change // 5):
        coins.append(NICKEL)
    change -= 5 * change // 5
    for x in range(change // 1):
        coins.append(PENNY)
    change -= 1 * change // 1
    return coins

def main():
    # ascii_map = {}
    # create_ascii_map(ascii_map)
    # print_map(ascii_map)

    # word_map = ()
    # ch = input('Enter a letter: ')
    # while ch != '':
    #     print (word_map[ch])
    #     ch = input("Enter a letter: ")

    print(make_change(169, 200))

if __name__ == '__main__':
    main()
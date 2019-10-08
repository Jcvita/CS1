"""
This program includes a function to find and return
the length of a longest common consecutive substring
shared by two strings.

If the strings have nothing in common, the longest
common consecutive substring has length 0.

For example, if string1 = "established", and
string2 = "ballistic", the function returns the
integer 3, as the string "lis" is the longest common
consecutive substring shared by the two strings.

The function tests all possible pairs of starting points
(starting point for string 1, and starting point for string 2),
and measures the match from each.  It keeps
track of the length of the best match seen,
and returns that when finished checking all starting points.

The function has bug(s).

There are no tests (yet).

Your job is to
1) include in this program a sufficient
suite of pass/fail tests to thoroughly
test the function and expose all error(s).

2) Generate a screenshot that
demonstrates your use of a debugger
to step through the function. Specifically it should
illustrate the execution point of a test at
which the function makes (or is about to make)
a mistake.

3) fix the code and document your fix(es).
Include additional tests if you feel it
necessary to thoroughly test the function.

You will submit your updated version of this
file (along with a separate document containing
the screenshot and answered questions).

File:  test_debug2.py
Author: CS @ RIT
Author: (Joseph Vita)

"""


def match(string1, string2):
    """
    Identifies and returns the length of a longest
    common consecutive substring shared
    by the two input strings.
    :param string1: The first string.
    :param string2: The second string.
    :return: length of a longest shared consecutive string.
    """

    best_length = 0
    # for all possible string1 start points
    for idx1 in range(len(string1) - 1):
        # for all possible string2 start points
        for idx2 in range(len(string2) - 1):
            # check if these characters match
            if string1[idx1] == string2[idx2]:
                this_match_count = 1
                # see how long the match continues
                while string1[idx1 + this_match_count] == \
                        string2[idx2 + this_match_count]:
                    this_match_count += 1
                    if idx1 + this_match_count >= len(string1) or \
                            idx2 + this_match_count >= len(string2):
                        break

                # compare to best so far
                if this_match_count > best_length:
                    best_length = this_match_count

    # now return the result
    return best_length


def test():
    print(match("established", "ballistic"))  # 3
    print(match("qwertyuiop", "asdfghjkl"))  # 0
    print(match("test", "test"))  # 4
    print(match("qwertyuiop", "rtyu"))  # 4
    print(match("qwertyuiop", "qwertyuiop"))  # 10
    print(match("jflvnhsrlk", "ajksdhfoas"))  # 1
    print(match("123456789", "987654321"))  # 1
    print(match("ppppp", "bbbbpppppp"))  # 5
    print(match("ppppp", "ppppppppbbbbpppppp"))  # 5
    print(match("", ""))  # 0


test()
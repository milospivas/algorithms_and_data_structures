""" author: Miloš Pivaš
    date: 09.03.2020
"""

class KMP:
    'Implements Knuth-Morris-Pratt algorithm for string pattern matching'
    version = '0.1'

    @staticmethod
    def preprocess(p : str) -> list:
        'Preprocess the string pattern p'

        if len(p) == 0:
            return []

        t = [0 for _ in p]  # fill the table with 0

        j = 0
        for i in range(1, len(p)):
            if p[i] == p[j]:
            # if there's a continuing match
                t[i] = t[i-1] + 1   # increment the table entry
                j += 1              # move j
            else:
            # if there isn't a continuing match
                while j > 0 and p[i] != p[j]:
                # while we're in the pattern and there isn't a character match:
                    j = t[j-1]  # since we've already matched with characters p[:t[j-1]] characters, try matching the next one

                if p[i] == p[j]:
                # if there is an earlier match
                    t[i] = t[j] + 1     # continue filling the table from the earlier table entry
                    j += 1              # move j
        return t

    @staticmethod
    def find(s : str, p : str) -> int:
        'Given strings s and p, find the starting index of the first occurrence p in s. Return -1 if there is none.'
        t = KMP.preprocess(p)

        i = j = 0   # start at the starts of s and p
        while i < len(s) and j < len(p):
        # while both are not processed
            if s[i] == p[j]:
            # if there's a character match
                i += 1  # move i
                j += 1  # move j
                if j == len(p):
                # this means we've found the pattern
                    return i - len(p)   # return the index of the start of the pattern
            else:
            # if there isn't a character match
                if j == 0:
                # if we are at the start of the pattern
                    i += 1  # just move on to the next char in the s
                else:
                # if we are in the pattern,
                    # we have already matched t[j-1] characters in s with p[:t[j-1]]
                    # so just backtrack to the next character in p, the p[t[j-1]]
                    j = t[j-1]

        return -1   # we haven't found the pattern

def print_preprocessing(p : str, t: list) -> None:
    'for preprocessing testing'
    print('pattern char, preprocessing table entry')
    for c, i in zip(p, t):
        print(c, i)

# # preprocessing testing
# p = "abcdabca"
# t = KMP.preprocess(p)
# print_preprocessing(p, t)

# p = "abcdabcabcd"
# t = KMP.preprocess(p)
# print_preprocessing(p, t)

# p = "aabaabaaa"
# t = KMP.preprocess(p)
# print_preprocessing(p, t)

# find testing
s = "abcdabcyabcdabca"
p = "abcdabca"
idx = KMP.find(s, p)
assert p == s[idx : idx + len(p)]

s = "aabaaabaabaabaabaaaaaaabaaa"
p = "aabaabaaa"
idx = KMP.find(s, p)
assert p == s[idx : idx + len(p)]

s = "sdfadfasfasd"
p = "asdf"
idx = KMP.find(s, p)
assert idx == -1

s = "2121212121212122121212121212122112"
p = "2112"
idx = KMP.find(s, p)
assert p == s[idx : idx + len(p)]
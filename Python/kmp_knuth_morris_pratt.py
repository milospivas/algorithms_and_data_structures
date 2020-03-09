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

        t = [0 for _ in p]

        j = 0
        for i in range(1, len(p)):
            if p[i] == p[j]:
                t[i] = t[i-1] + 1
                j += 1
            else:
                while j > 0 and p[i] != p[j]:
                    j = t[j-1]

                if p[i] == p[j]:
                    t[i] = t[j] + 1
                    j += 1
            
        return t

    @staticmethod
    def find(s : str, p : str) -> int:
        'Given strings s and p, find the starting index of the first occurrence p in s. Return -1 if there is none.'
        t = KMP.preprocess(p)

        i = j = 0
        while i < len(s) and j < len(p):
            if s[i] == p[j]:
                i += 1
                j += 1
                if j == len(p):
                    return i - len(p)
            else:
                if j == 0:
                    i += 1
                else:
                    j = t[j-1]                

        return -1

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
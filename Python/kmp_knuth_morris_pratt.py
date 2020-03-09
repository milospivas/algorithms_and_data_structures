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
                j = 0
                if p[i] == p[j]:
                    t[i] = 1
                    j += 1
                
        return t

def print_preprocessing(p : str, t: list) -> None:
    'for preprocessing testing'
    print('pattern char, preprocessing table entry')
    for c, i in zip(p, t):
        print(c, i)

# preprocessing testing
p = "abcdabca"
t = KMP.preprocess(p)
print_preprocessing(p, t)

p = "abcdabcabcd"
t = KMP.preprocess(p)
print_preprocessing(p, t)

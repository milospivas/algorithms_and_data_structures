''' Dynamic Programming: Text justification
    Problem: Split text into lines of limitted line width, minimizing white space.

    Author: Miloš Pivaš, student
'''

### shared function(s) ##################################################################

def badness(words, start, next_start, line_character_limit):
    ''' Evaluate 'badness' of having words[start:next_start] form a line
    in a text of given limit for character width.

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    start : int
        Index of the first word in the line.
    next_start : int
        Index of the first word in the next line.
    line_character_limit : int
        Maximum number of characters that can fit in a line of text.

    Returns
    -------
    out: int
        Evaluated badness.
    '''

    number_of_word_characters = 0
    for word in words[start:next_start]:
        number_of_word_characters += len(word)

    spaces_between_words = len(words[start:next_start]) - 1

    b = (line_character_limit - number_of_word_characters - spaces_between_words)**3

    if b < 0:
        b = float('inf')

    return b


### Naive recursive DP ##################################################################

def justify_nr(words, line_character_limit):
    ''' Insert new lines into given text to justify it.

    Naive recursive method using dynamic programming (without caching - hence naive).

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    line_character_limit : int
        Line width in number of characters.

    Returns
    -------
    out : list, int
        list
            A list of indices where new lines are to be inserted.
        int
            Accumulated badness score
            (='inf' if there is a word larger than line_character_limit).
    '''

    def __justify(start = 0):

        if start == len(words):
            return [], 0

        min_score = float('inf')

        for next_start in range(start+1, len(words)+1):

            next_indices, next_score = __justify(next_start)

            score = next_score + badness(words, start, next_start, line_character_limit)

            if score < min_score:
                min_score = score
                min_indices = next_indices + [next_start]

        return min_indices, min_score

    min_indices, min_score = __justify()
    min_indices.sort()
    return min_indices, min_score


### Recursive DP with caching (memoization) #############################################

def justify_rc(words, line_character_limit):
    ''' Insert new lines into given text to justify it.

    Recursive method using dynamic programming with caching (memoization).

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    line_character_limit : int
        Line width in number of characters.

    Returns
    -------
    out : list, int
        list
            A list of indices where new lines are to be inserted.
        int
            Accumulated badness score
            (='inf' if there is a word larger than line_character_limit).
    '''

    def __cache_init():
        cache = {}
        cache[len(words)] = [], 0
        return cache

    def __justify_with_caching(start = 0):
        if start in cache:
            return cache[start]

        min_score = float('inf')
        for next_start in range(start+1, len(words)+1):

            next_indices, next_score = __justify_with_caching(next_start)

            score = next_score + badness(words, start, next_start, line_character_limit)

            if score < min_score:
                min_score = score
                min_indices = next_indices + [next_start]

        cache[start] = min_indices, min_score

        return min_indices, min_score

    cache = __cache_init()
    min_indices, min_score = __justify_with_caching()
    min_indices.sort()
    return min_indices, min_score


### Iterative DP bottom-up ##############################################################

def justify_bu(words, line_character_limit):
    ''' Insert new lines into given text to justify it.

    Iterative, bottom-up method using dynamic programming.

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    line_character_limit : int
        Line width in number of characters.

    Returns
    -------
    out : list, int
        list
            A list of indices where new lines are to be inserted.
        int
            Accumulated badness score
            (='inf' if there is a word larger than line_character_limit).
    '''

    def __cache_init():
        cache = {}
        cache[len(words)] = [], 0
        return cache

    def __get_topological_order():
        for start in range(len(words)-1, -1, -1):
            yield start

    cache = __cache_init()
    topological_order = __get_topological_order()

    for start in topological_order:

        min_score = float('inf')
        for next_start in range(start+1, len(words)+1):

            next_indices, next_score = cache[next_start]

            score = next_score + badness(words, start, next_start, line_character_limit)

            if score < min_score:
                min_score = score
                min_indices = next_indices + [next_start]

        cache[start] = min_indices, min_score

    min_indices, min_score = cache[0]
    min_indices.sort()
    return min_indices, min_score


### testing #############################################################################

def get_justified_text(words, indices):
    ''' Produces justified text from words with new lines at given indices.

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    indices : list
        A list of indices where new lines are to be inserted.

    Returns
    -------
    out : str
        Justified text.
    '''

    txt = ''
    new_line_idx = 0
    for word_idx, word in enumerate(words):
        txt += word
        if word_idx == indices[new_line_idx]-1:
            txt += '\n'
            new_line_idx += 1
        else:
            txt += ' '

    return txt


def test(words, line_character_limit, justfy_func):
    ''' Tests given justification function.

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    line_character_limit : int
        Line width in number of characters.
    justify_func : function handle
        The justification function to test.
        The function needs to have this interface:

            Parameters
            ----------
            words : list
                The list of words representing text to be justified.
            line_character_limit : int
                Line width in number of characters.

            Returns
            -------
            out : list, int
                list
                    A list of indices where new lines are to be inserted.
                int
                    Accumulated badness score
                    (='inf' if there is a word larger than line_character_limit).
    '''

    indices, score = justfy_func(words, line_character_limit)
    txt = get_justified_text(words, indices)

    print('words:', words)
    print('line_character_limit:', line_character_limit)
    print('score:', score)
    print('indices:', indices)
    print('justified text:')
    print(txt)


for functions in [justify_nr, justify_rc, justify_bu, get_justified_text, test]:
    help(functions)

text = '12345678901 123 123 123 123'
line_character_limit = 11
words = text.split(' ')

for justify_func in [justify_nr, justify_rc, justify_bu]:

    test(words, line_character_limit, justify_func)


print('Exiting...')
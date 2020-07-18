''' Dynamic Programming: Text justification
    Problem: Split text into lines of limitted line width, minimizing white space.

    Author: Miloš Pivaš, student
'''

### shared function(s)

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


### Naive recursive DP

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


### Recursive DP with caching (memoization)

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

    def cache_init():
        cache = {}
        cache[len(words)] = [], 0
        return cache

    def __justify_with_caching(start = 0):

        min_score = float('inf')
        for next_start in range(start+1, len(words)+1):

            next_indices, next_score = cache[next_start] if next_start in cache else __justify_with_caching(next_start)

            score = next_score + badness(words, start, next_start, line_character_limit)

            if score < min_score:
                min_score = score
                min_indices = next_indices + [next_start]

        cache[start] = min_indices, min_score

        return min_indices, min_score

    if len(words) == 0:
        return [], 0

    cache = cache_init()
    min_indices, min_score = __justify_with_caching()
    min_indices.sort()
    return min_indices, min_score


### Iterative DP bottom-up

def justify_bu(words, line_width):
    ''' Insert new lines into given text to justify it.

    Iterative, bottom-up method using dynamic programming.

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    line_width : int
        Line width in number of characters.

    Returns
    -------
    out : list, int
        list
            A list of indices where to insert new lines.
        int
            Accumulated badness score
            (='inf' if there is a word larger than the line_width).
    '''

    n = len(words)

    # init cache
    cache = {}
    cache[n] = ([], 0)

    for i in range(n-1, -1, -1):
    # iterate in topologicaly sorted order,
    # from the end of the text to the begining

        min_score = float('inf')

        # for every of the remaining words
        for j in range(i+1, n+1):
        # pick a break-point for the next line
            # justify the rest of words after new line

            # retrieve the score for the next lines
            _, score = cache[j]

            # add the score for the current line
            score += badness(words, i, j, line_width)

            # keep min
            if score < min_score:
                min_score = score
                min_index = j

        # retrieve optimum indices
        min_indices, _ = cache[min_index]

        # add the break-point index (if it is a new index)
        if (len(min_indices) == 0) or (min_index != min_indices[-1]):
            min_indices += [min_index]

        # store min in cache
        cache[i] = (min_indices, min_score)

    # solution is in cache for the whole text
    return cache[0]


### testing

def test(words, line_width, justfy_function):
    ''' Tests given justification function.

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    line_width : int
        Line width in number of characters.
    justify_function : function handle
        A function to use for justification.
        The function needs to follow this format:

            Parameters
            ----------
            words : list
                The list of words representing text to be justified.
            line_width : int
                Line width in number of characters.
            i : int, optional
                Index of the word from which to start justifying.

            Returns
            -------
            out : list, int
                list
                    A list of indices where to insert new lines.
                int
                    Accumulated badness score
                    (='inf' if there is a word larger than the line_width).
    '''

    help(justfy_function)

    indices, score = justfy_function(words, line_width)
    indices.sort()
    print('words:', words)
    print('line_width:', line_width)
    print('score:', score)
    print('indices:', indices)

    print('justified text:')
    k = 0
    for i, word in enumerate(words):
        print(word, end='')
        if i == indices[k]-1:
            print('\n', end='')
            k += 1
        else:
            print(' ', end='')


text = '12345678901 123 123 123 123'
words = text.split(' ')
line_width = 11

test(words, line_width, justify_nr)

test(words, line_width, justify_rc)

test(words, line_width, justify_bu)


print('Exiting...')
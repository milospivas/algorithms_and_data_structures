''' Dynamic Programming: Text justification

    Author: Miloš Pivaš, student
'''


def badness(words, i, j, line_width):
    ''' Evaluate 'badness' of having words[i:j] form a line 
    in a text of given limit for character width.

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    i : int
        Index of the first word in the line.
    j : int
        Index of the first word in the next line.
    line_width : int
        Line width in characters

    Returns
    -------
    int
        Evaluated badness.
    '''

    # calculating character width of the words
    width = 0
    for word in words[i:j]:
        width += len(word)
    
    # adding the number of spaces
    width += len(words[i:j]) - 1

    b = (line_width - width)**3

    if b < 0:
        b = float('inf')
    
    return b


### Naive recursive DP

def justify_nr(words, line_width, i = 0):
    ''' Insert new lines into given text to justify it.

    Naive recursive method using dynamic programming (without caching - hence naive).

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    line_width : int
        Line width in number of characters.
    [i : int]
        Index of the word from which to start justifying.

    Returns
    -------
    (list, int)
    list
        A list of indices where to insert new lines.
    int
        Accumulated badness score 
        (='inf' if there is a word larger than the line_width).
    '''

    # calculate the number of remaining words
    n = len(words)
    n_remaining = n-i

    if n_remaining == 0:
        return [], 0

    min_score = float('inf')

    # for every of the remaining words
    for j in range(i+1, n+1):
    # pick a break-point for the new line
        # justify the rest of words after new line
        later_indices, score = justify_nr(words, line_width, j)
        
        # add the score for the current line
        score += badness(words, i, j, line_width)
        
        # keep min
        if score < min_score:
            min_score = score
            min_indices = later_indices + [j]

    return min_indices, min_score


### Recursive DP with caching (memoization)

def justify_rc(words, line_width, i = 0, cache = None):
    ''' Insert new lines into given text to justify it.

    Recursive method using dynamic programming with caching (memoization).

    Parameters
    ----------
    words : list
        The list of words representing text to be justified.
    line_width : int
        Line width in number of characters.
    [i : int]
        Index of the word from which to start justifying.
    [cache : dict]
        Dictionary of already calculated solutions.

    Returns
    -------
    (list, int)
    list
        A list of indices where to insert new lines.
    int
        Accumulated badness score 
        (='inf' if there is a word larger than the line_width).
    '''

    # calculate the number of remaining words
    n = len(words)
    n_remaining = n-i

    if n_remaining == 0:
        return [], 0

    if cache is None:
        cache = {}

    min_score = float('inf')

    # for every of the remaining words
    for j in range(i+1, n+1):
    # pick a break-point for the new line
        # justify the rest of words after new line

        if j in cache:
            # get it from cache if it's already computed
            later_indices, score = cache[j]
        else:
            # compute it
            later_indices, score = justify_rc(words, line_width, j, cache)
            cache[j] = (later_indices, score)

        # add the score for the current line
        score += badness(words, i, j, line_width)
        
        # keep min
        if score < min_score:
            min_score = score
            min_indices = later_indices + [j]

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
    (list, int)
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
            [i : int]
                Index of the word from which to start justifying.

            Returns
            -------
            (list, int)
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
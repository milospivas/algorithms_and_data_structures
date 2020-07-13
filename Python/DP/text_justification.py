''' Dynamic Programming: Text justification

    Author: Miloš Pivaš
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

# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) <= 1:
        return sequence

    # for i in range(len(sequence)):
    #     temp = sequence.replace(sequence[i], "")
    #     for j in range(len(sequence)):
    #         perm = "".join([temp[0:j], sequence[i], temp[j:]])
    #         print(perm)
    answerList = []

    if len(sequence) == 1:
        return [sequence]
    else:
        # select the first word
        insertor = sequence[0]
        # for every word in the list without first word
        for word in get_permutations(sequence[1:]):
            # put in to different position - len(sequence) ways
            for i in range(len(sequence)):
                answerList.append(word[:i] + insertor + word[i:])

        # make a list

        # return the list
        return answerList





if __name__ == '__main__':

#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations("abc"))


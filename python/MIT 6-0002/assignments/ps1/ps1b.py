###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
import time

def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    if target_weight < egg_weights[0]:
        return 'Not possible to find'

    for egg in egg_weights:
        memo[egg] = 1

    def make_weights(eggs, weight, dictionary):

        if weight in dictionary:
            return dictionary[weight]

        else:
            for i in range(1, weight + 1):
                if i not in dictionary:
                    try:
                        for j in egg_weights:
                            if i - j > 0:
                                result = make_weights(eggs, i - j, dictionary)
                            else:
                                break

                            if type(result) == int:
                                if i not in dictionary:
                                    dictionary[i] = result + 1
                                elif i in dictionary and result < dictionary[i]:
                                    dictionary[i] = result + 1

                    except KeyError:
                        pass
        return dictionary
    final_dict = make_weights(egg_weights, target_weight, memo)
    for i in range(target_weight + 1):
        if i not in final_dict:
            final_dict[i] = 'Not possible to find'
    return final_dict[target_weight]


def dp_make_weight2(arr, sum, memo={}):
    def make_weight(eggs, target, dictionary):
        if target in dictionary: return dictionary[target]
        if target == 0: return []
        if target < 0: return None

        shortestCombination = None

        for i in eggs:
            remainder = target - i
            remainderCombination = make_weight(eggs, remainder, dictionary)
            if remainderCombination != None:
                combination = [*remainderCombination, i]
                if shortestCombination is None or len(combination) < len(shortestCombination):
                    shortestCombination = combination

        dictionary[target] = shortestCombination
        return shortestCombination
    return len(make_weight(arr, sum, memo))

def iterativeSolution(egg_weights, targetSum):
    if len(egg_weights) == 0: return 0
    if targetSum == 0: return 1
    table = (targetSum + 1) * [None]
    table[0] = []
    for i in egg_weights:
        if i <= len(table): table[i] = [i]
    if table[targetSum] is not None:
        return table[targetSum]
    for pos in range(1, len(table)):
        if table[pos] is not None:
            for egg in egg_weights:
                if pos + egg <= targetSum:
                    if table[pos + egg] is None:
                        table[pos + egg] = table[pos].copy() + [egg]
                    else:
                        result = table[pos].copy() + [egg]
                        if len(result) < len(table[pos + egg]):
                            table[pos + egg] = result.copy()

    return table[targetSum]


def anotherSolution(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    if weight_is_in_egg_weights(target_weight, egg_weights):
        return 1

    for weight in range(1, target_weight + 1):

        if weight_is_in_egg_weights(weight, egg_weights):
            memo[weight] = 1
            continue

        qty_eggs = weight
        for egg in egg_weights:
            if egg > weight:
                continue
            if memo[weight - egg] + 1 < qty_eggs:
                qty_eggs = memo[weight - egg] + 1
            memo[weight] = qty_eggs

    return memo[target_weight]


def weight_is_in_egg_weights(weight, egg_weights):
    if weight in egg_weights:
        return True
    else:
        return False


def anotherSolution2(egg_weights, target_weight, memo):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    # First Method
    # egg_list = []
    # for w in sorted(egg_weights, reverse=True):
    #     egg_count = int(target_weight / w)
    #     egg_list += [w, ] * egg_count
    #     target_weight -= w * egg_count
    #
    # return egg_list

    # Second Method
    minEggs = target_weight
    if target_weight in egg_weights:
        memo[target_weight] = 1
        return 1
    elif memo[target_weight] > 0:
        return memo[target_weight]
    else:
        for i in [c for c in egg_weights if c <= target_weight]:
            numEggs = 1 + anotherSolution2(egg_weights, target_weight - i, memo)
            if numEggs < minEggs:
                minEggs = numEggs
                memo[target_weight] = minEggs
    return minEggs

def anotherSolution3(egg_weights, target_weight, memo = {}):

    if target_weight == 0:
        return 0

    try:
        return memo[target_weight]

    except KeyError:
        for egg in egg_weights:
            new_weight = target_weight - egg
            if new_weight >= 0:
                result = 1 + anotherSolution3(egg_weights, new_weight, memo)
                memo[target_weight] = result
    return result


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    # egg_weights = (1, 2)
    # n = 10
    # print("Egg weights = (1, 2)")
    # print("n = 5")
    # print("Expected ouput: 3 (2 * 2 + 1 * 1 = 5)")
    # print("Actual output:", dp_make_weight(egg_weights, n))
    # print()
    egg_weights = (54, 7, 10, 25)
    n = 99999
    # print("Egg weights = (1, 5, 10, 25)")
    # print("n = 99")
    # print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    # start = time.time()
    # print("Actual output:", dp_make_weight2(egg_weights, n))
    # end = time.time()
    # print(start - end)
    # start2 = time.time()
    # end2 = time.time()
    # print(start2 - end2)
    print("Actual output:", dp_make_weight(egg_weights, n)) # moje resenje
    # print("Actual output:", anotherSolution2(egg_weights, n, memo = [0]*(n + 1)))

    # print("Actual output:", iterativeSolution(egg_weights, n))



    # print()

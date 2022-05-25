###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows = {}
    inFile = open(filename, 'r')
    for line in inFile:
        cow = line.strip().split(',')
        cows[cow[0]] = int(cow[1])
    inFile.close()
    return cows


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    list_of_cows = []
    for cow in cows.items():
        list_of_cows.append([cow[0], cow[1]])
    list_of_cows.sort(key=lambda x: x[1], reverse=True)
    transport = []
    trip = []
    for cow in list_of_cows:
        if cow[1] <= limit:
            trip.append(cow[0])
        else:
            if trip != []:
                transport.append(trip)
                trip = []
                limit = 10
                trip.append(cow[0])
        limit -= cow[1]
    if len(trip) !=0: transport.append(trip)
    return transport


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    list_of_cows = []
    for cow in cows.keys():
        list_of_cows.append(cow)

    trip = len(list_of_cows)
    transport = []
    for partition in get_partitions(list_of_cows):
        transport.append(partition)
    available_transports = []
    for i in transport:
        if len(i) < trip:
            total_transport = 0
            for y in i:
                total = 0 # total limit of one transport

                for z in y:
                    total += cows[z]
                if total > limit:
                    break
                else:
                    total_transport += 1
            # print('Total transport is {}, len of i is {}'.format(total_transport, len(i)), end=' and i is: ')
            # print(i)
            if total_transport == len(i):
                available_transports.append(i)
    available_transports.sort(key=lambda x: len(x))
    minimum = len(available_transports[0])
    for k in range(len(available_transports)):
        if len(available_transports[k]) > minimum:
            return available_transports[:k]
    return available_transports


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    greedy_cow_transport(load_cows('ps1_cow_data.txt'))
    end = time.time()
    print('Greedy algorithm runs in: {}'.format(start - end))
    start = time.time()
    brute_force_cow_transport(load_cows('ps1_cow_data.txt'))
    end = time.time()
    print('Brute force algorithm runs in: {}'.format(start - end))

compare_cow_transport_algorithms()



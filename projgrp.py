import random




def pop_maker(n):
    """Creates a population of size n in the from of a list of numbers from 1 to n"""
    pop = range(1, n + 1 , 1)
    return pop


def pop_divider(n, s):
    """Divides the population of size n into partitions of size at least s and maximum s+1"""
    r = n % s
    number_of_grps = (n - r)/s
    first = [s] * number_of_grps
    second = [0] * (number_of_grps - r) + [1] * r
    partition = [i + j for i, j in zip(first, second)]
    return partition
    print partition


def group_maker(pop, s):
    """Randomly picks a group of size s from pop"""
    sample = random.sample(pop, s)
    return sample


def find_dup(pop, sample):
    """Finds the common elements in the list pop and sample, removes common from pop"""
    seen = set(sample)
    uniq = []
    for i in pop:
        if i not in seen:
            uniq.append(i)
    return uniq

def sample_maker(n, s):
    groups = []
    pop = pop_maker(n)
    partition = pop_divider(n, s)
    print 'The groups will be partitioned in ', partition
    j = 1
    for i in partition:
        if i >= len(pop):
            group = pop
        else:
            group = group_maker(pop, i)
            pop = find_dup(pop, group)
        groups.append(group)
        print 'Group %d :' % j, group
        j = j + 1
    return groups


def get_groups():
    """Takes in number of students n and smallest group size s. Returns class
        partition and the groups."""
    n = raw_input('Enter the number of students in your class: ')
    s = raw_input('Enter the smallest size of each group: ')

    n = int(n)
    s= int(s)
    sample_maker(n, s)

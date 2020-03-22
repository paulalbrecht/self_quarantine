

def mysum(*args):
    total = 0
    
    for number in args:
        total = total + number
    
    return total

assert mysum(1, 2, 3) == 6


def myavg(numbers):
    return sum(numbers) / len(numbers)

assert myavg([1, 2, 3]) == 2.0


def word_numbers(words):
    return tuple([len(min(words)), len(max(words)), sum(len(x) for x in words) / len(words)])

assert word_numbers(["a", "bb", "ccc"]) == (1, 3, 2.0)



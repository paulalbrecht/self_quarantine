# 3.1.1
def firstlast(seq):
    return seq[:1] + seq[-1:]

print(firstlast([1, 2, 3]))
print(firstlast('abc'))


# 3.2.1
def mysum(*inputs):
    if not inputs:
        return inputs
    output = inputs[0]
    for input in inputs[1:]:
        output += input
    return output

print('abc', 'def')
print(mysum([1, 2, 3], [4, 5, 6]))


def mysum_bigger_than(*inputs):
    if not inputs:
        return inputs
    output = inputs[0]
    for input in inputs[1:]:
        try:
            if inputs[0] < int(input):
                output += int(input)
        except ValueError:
            pass
    return output
print(mysum_bigger_than(10, 5, 20, 30, 6))
print(mysum_bigger_than(10, 20, 'a', '30', 'bcd'))


def combine_dicts(*dicts):
    if not dicts:
        return {}
    combined = dicts[0]
    for d in dicts[1:]:
        for k, v in d.items():
            if k in combined.keys():
                combined.update({k: [v, d[k]]})
            else:
                combined.update({k: d[k]})
    return combined


dicts = [{ 'x' : 1, 'y' : 2, 'z' : 3 }, { 'u' : 1, 'v' : 2, 'w' : 3, 'x'  : 1, 'y': 2 }]
combined = combine_dicts(*dicts)
print(combined)

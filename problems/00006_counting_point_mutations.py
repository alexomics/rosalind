def hamming_distance(s, t):
    return sum(_s != _t for _s, _t in zip(s, t))

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

assert hamming_distance(s, t) == 7

s, t = open(f"{__file__.split('.')[0]}.input.txt", "r").readlines()
print(hamming_distance(s, t))


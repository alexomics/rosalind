import timeit

def _fmt(num: int, factor: int = 1000, suffix: str = 's') -> str:
    for unit in ['', 'm', 'µ', 'n', 'p', 'f', 'a', 'z']:
        if 1 < num < factor:
            return "{n:,.2f} {u}{s}".format(n=num, u=unit, s=suffix)
        num *= factor
    return "{n:,.2f} {u}{s}".format(n=num, u='y', s=suffix)

def count_nucleotides(s):
    for char in "ACGT":
        yield s.count(char)

# Check against sample input:
s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
res = (20, 12, 17, 21)

assert tuple(count_nucleotides(s)) == res

# Run on actual input:
inp = __file__.split(".")[0] + ".input.txt"
print(f"Input: {inp!r}")
start = timeit.default_timer()
s = open(inp, "r").read().strip()
res = " ".join(str(x) for x in count_nucleotides(s))
print(f"Output: {res}")
end = timeit.default_timer()
print(f"Took: {_fmt(end - start)}")



"""
Other solutions

def dna_counter(s):
    '''Using collections.Counter.'''
    c = Counter(s)
    return c["A"], c["C"], c["G"], c["T"]


def dna_counter(s):
    '''Using just dicts'''
    d = {}
    for char in s:
        if char not in d:
            d[char] = 0
        d[char] += 1

    return d.get("A", 0), d.get("C", 0), d.get("G", 0), d.get("T", 0)
"""

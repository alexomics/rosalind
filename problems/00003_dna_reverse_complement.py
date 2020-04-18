import timeit

def _fmt(num: int, factor: int = 1000, suffix: str = 's') -> str:
    for unit in ['', 'm', 'µ', 'n', 'p', 'f', 'a', 'z']:
        if 1 < num < factor:
            return "{n:,.2f} {u}{s}".format(n=num, u=unit, s=suffix)
        num *= factor
    return "{n:,.2f} {u}{s}".format(n=num, u='y', s=suffix)

def reverse_complement(s, table):
    return s.translate(table)[::-1]

# Check against sample input:
s = "AAAACCCGGT"
res = "ACCGGGTTTT"
table = str.maketrans("ACGT", "TGCA")

assert reverse_complement(s, table) == res

# Run on actual input:
inp = __file__.split(".")[0] + ".input.txt"
print(f"Input: {inp!r}")
start = timeit.default_timer()
s = open(inp, "r").read().strip()
res = reverse_complement(s, table)
print(f"Output: {res}")
end = timeit.default_timer()
print(f"Took: {_fmt(end - start)}")


import timeit

def _fmt(num: int, factor: int = 1000, suffix: str = 's') -> str:
    for unit in ['', 'm', 'µ', 'n', 'p', 'f', 'a', 'z']:
        if 1 < num < factor:
            return "{n:,.2f} {u}{s}".format(n=num, u=unit, s=suffix)
        num *= factor
    return "{n:,.2f} {u}{s}".format(n=num, u='y', s=suffix)

def translate_rna(s, table):
    return s.translate(table)

# Check against sample input:
s = "GATGGAACTTGACTACGTAAATT"
res = "GAUGGAACUUGACUACGUAAAUU"
table = str.maketrans("T", "U")

assert translate_rna(s, table) == res

# Run on actual input:
inp = __file__.split(".")[0] + ".input.txt"
print(f"Input: {inp!r}")
start = timeit.default_timer()
s = open(inp, "r").read().strip()
res = translate_rna(s, table)
print(f"Output: {res}")
end = timeit.default_timer()
print(f"Took: {_fmt(end - start)}")


def read_fasta(fh):
    # Iterate to get first FASTA header        
    for line in fh:
        if line.startswith(">"):
            name = line[1:].strip()
            break

    # This list will hold the sequence lines
    fa_lines = []

    # Now iterate to find the get multiline fasta
    for line in fh:
        if line.startswith(">"):
            # When in this block we have reached 
            #  the next FASTA record

            # yield the previous record's name and
            #  sequence as tuple that we can unpack
            yield name, "".join(fa_lines)

            # Reset the sequence lines and save the
            #  name of the next record
            fa_lines = []
            name = line[1:].strip()

            # skip to next line
            continue

        fa_lines.append(line.strip())

    yield name, "".join(fa_lines)


res = []
with open(f"{__file__.split('.')[0]}.input.txt", "r") as fh:
    for name, seq in read_fasta(fh):
        # gc = seq.count("G") + seq.count("C")
        # gc = sum(1 for base in seq if base.lower() in "gc")
        gc = sum(base.lower() in "gc" for base in seq)
        res.append((name, gc / len(seq) * 100))

result = max(res, key=lambda x: x[1])
print("{}\n{:.6f}".format(*result))


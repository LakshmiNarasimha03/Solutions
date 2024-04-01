def virusIndices(p, v):
    def match_or_mismatch(sub, virus):
        if len(sub) != len(virus):
            return False
        mismatch_count = 0
        for i in range(len(sub)):
            if sub[i] != virus[i]:
                mismatch_count += 1
                if mismatch_count > 1:
                    return False
        return True

    indices = []
    virus_length = len(v)
    for i in range(len(p) - virus_length + 1):
        sub = p[i:i+virus_length]
        if sub == v or match_or_mismatch(sub, v):
            indices.append(str(i))
    if indices:
        print(" ".join(indices))
    else:
        print("No Match!")

test_cases = [
    ("abbab", "ba"),
    ("hello", "world"),
    ("banana", "nan")
]

for p, v in test_cases:
    virusIndices(p, v)

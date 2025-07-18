def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in reversed(seq))

def is_perfect_palindrome(seq):
    return seq == reverse_complement(seq)

def find_perfect_palindromes(seq, min_len=4, max_len=12):
    n = len(seq)
    results = []

    for i in range(n):
        for l in range(min_len, max_len + 1):
            if i + l > n:
                continue
            subseq = seq[i:i + l]
            if is_perfect_palindrome(subseq):
                results.append({
                    "type": "Perfect Palindrome",
                    "sequence": subseq,
                    "start": i + 1,
                    "end": i + l,
                    "length": l
                })
    return results

def find_inverted_repeats(seq, min_len=4, max_len=12, max_spacer=3, max_mismatches=1):
    n = len(seq)
    results = []

    for i in range(n):
        for l in range(min_len, max_len + 1):
            for spacer in range(0, max_spacer + 1):
                left_start = i
                left_end = i + l
                right_start = left_end + spacer
                right_end = right_start + l

                if right_end > n:
                    continue

                left = seq[left_start:left_end]
                right = reverse_complement(seq[right_start:right_end])

                mismatches = sum(1 for a, b in zip(left, right) if a != b)

                if mismatches <= max_mismatches:
                    results.append({
                        "type": "Inverted Repeat",
                        "left_arm": left,
                        "right_arm": seq[right_start:right_end],
                        "start": left_start + 1,
                        "end": right_end,
                        "length": l,
                        "spacer": spacer,
                        "mismatches": mismatches
                    })
    return results

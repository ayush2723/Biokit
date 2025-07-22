def calculate_tm(sequence: str) -> float:
    """Calculate melting temperature (Tm) using Wallace Rule."""
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return 2 * (a_count + t_count) + 4 * (g_count + c_count)

def calculate_gc_content(sequence: str) -> float:
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100 if sequence else 0

def design_optimal_primers(sequence: str, primer_length=20, tm_tolerance=2):
    best_pair = None
    best_tm_diff = float("inf")

    for i in range(len(sequence) - primer_length * 2):
        forward = sequence[i:i+primer_length]
        for j in range(i + primer_length, len(sequence) - primer_length):
            reverse = sequence[j:j+primer_length][::-1].translate(str.maketrans("ATGC", "TACG"))

            tm_f = calculate_tm(forward)
            tm_r = calculate_tm(reverse)
            tm_diff = abs(tm_f - tm_r)

            if tm_diff <= tm_tolerance and tm_diff < best_tm_diff:
                best_tm_diff = tm_diff
                best_pair = {
                    "forward_primer": forward,
                    "reverse_primer": reverse,
                    "forward_tm": tm_f,
                    "reverse_tm": tm_r,
                    "forward_gc": calculate_gc_content(forward),
                    "reverse_gc": calculate_gc_content(reverse),
                    "forward_start": i,
                    "reverse_start": j
                }

    return best_pair

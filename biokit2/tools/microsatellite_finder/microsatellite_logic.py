from typing import List, Dict

def find_microsatellites(sequence: str, min_unit_len: int = 2, max_unit_len: int = 6, min_repeats: int = 5) -> List[Dict]:
    """
    Finds microsatellites (short tandem repeats) in a DNA sequence.
    
    Args:
        sequence (str): Validated, uppercase DNA sequence.
        min_unit_len (int): Minimum motif size (e.g., 2 for dinucleotide).
        max_unit_len (int): Maximum motif size (default 6).
        min_repeats (int): Minimum number of consecutive repeats to qualify.

    Returns:
        List[Dict]: List of STR info with motif, start/end, repeats, strand.
    """
    results = []
    n = len(sequence)
    i = 0

    while i < n:
        found = False
        for unit_len in range(min_unit_len, max_unit_len + 1):
            if i + unit_len * min_repeats > n:
                continue

            motif = sequence[i:i + unit_len]
            if 'N' in motif:
                continue

            repeat_count = 1
            j = i + unit_len

            while j + unit_len <= n and sequence[j:j + unit_len] == motif:
                repeat_count += 1
                j += unit_len

            if repeat_count >= min_repeats:
                results.append({
                    'motif': motif,
                    'start': i + 1,
                    'end': j,
                    'repeats': repeat_count,
                    'strand': '+'
                })
                i = j  
                found = True
                break  

        if not found:
            i += 1

    return results

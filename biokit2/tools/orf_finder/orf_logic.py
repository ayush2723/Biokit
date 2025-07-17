def find_orfs(sequence: str) -> list[tuple[int, int, str]]:
    """
    Identifies all Open Reading Frames (ORFs) in a DNA sequence on the forward strand.

    Parameters:
        sequence (str): A valid, uppercase DNA sequence (A, T, C, G).

    Returns:
        list of tuples: Each tuple contains:
            - start index of ORF (0-based)
            - end index (exclusive)
            - ORF sequence string
    """
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    orfs = []

    for frame in range(3):
        i = frame
        while i < len(sequence) - 2:
            codon = sequence[i:i+3]
            if codon == start_codon:
                j = i + 3
                while j < len(sequence) - 2:
                    next_codon = sequence[j:j+3]
                    if next_codon in stop_codons:
                        if (j - i) % 3 == 0:
                            orfs.append((i, j + 3, sequence[i:j+3]))
                            break
                    j += 3
            i += 3
    return orfs

def highlight_orfs(sequence: str, orf_coords: list[tuple[int, int]]) -> str:
    """
    Highlights ORFs in a DNA sequence using square brackets.

    Parameters:
        sequence (str): Original DNA sequence (valid and uppercase).
        orf_coords (list of tuples): Each tuple has (start_index, end_index)

    Returns:
        str: The original sequence with ORFs wrapped in square brackets.
    """
    # Sort ORFs in reverse so insertions don't shift upcoming positions
    orf_coords = sorted(orf_coords, key=lambda x: x[0], reverse=True)

    for start, end in orf_coords:
        sequence = sequence[:end] + ']' + sequence[end:]
        sequence = sequence[:start] + '[' + sequence[start:]
    return sequence


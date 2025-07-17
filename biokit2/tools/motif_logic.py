"""
Motif Finder Logic

This module provides core logic for finding all occurrences of a given motif in a DNA sequence
using the Z-Algorithm for efficient exact pattern matching.

Biological Significance:
Motif discovery helps identify regulatory elements, binding sites, or conserved regions
across sequences critical for gene expression and function.
"""

def calculate_z_array(s: str) -> list[int]:
    """
    Computes the Z-array for a given string using the Z-algorithm.

    Args:
        s (str): Input string (motif + "$" + sequence)

    Returns:
        list[int]: Z-array where Z[i] represents length of longest substring starting
                   from i which is also a prefix of s.
    """
    n = len(s)
    Z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1
    return Z

def find_motif_positions(sequence: str, motif: str) -> list[int]:
    """
    Finds all positions where the motif occurs exactly in the sequence.

    Args:
        sequence (str): DNA sequence
        motif (str): Motif to search for

    Returns:
        list[int]: Starting indices (0-based) of motif occurrences in the sequence
    """
    combined = motif + "$" + sequence
    Z = calculate_z_array(combined)
    positions = []

    motif_len = len(motif)
    for i in range(len(motif) + 1, len(Z)):
        if Z[i] == motif_len:
            positions.append(i - motif_len - 1)

    return positions

def highlight_motif(sequence: str, positions: list[int], motif_len: int) -> str:
    """
    Highlights motif matches in the sequence with brackets.

    Args:
        sequence (str): Original DNA sequence
        positions (list[int]): Starting indices of matches
        motif_len (int): Length of the motif

    Returns:
        str: Sequence string with matches highlighted
    """
    marked = []
    last = 0
    for pos in positions:
        marked.append(sequence[last:pos])
        marked.append("[" + sequence[pos:pos + motif_len] + "]")
        last = pos + motif_len
    marked.append(sequence[last:])
    return "".join(marked)

# tools/find_palindromes.py

def find_palindromes(seq: str, length: int = 4) -> list:
    """
    Find all palindromic sequences of specified length in DNA.

    Args:
        seq (str): DNA sequence (A, T, G, C)
        length (int): Length of palindrome to search for (default 4)

    Returns:
        list: List of palindromic sequences found
    """
    seq = seq.upper()
    palindromes = []

    for i in range(len(seq) - length + 1):
        segment = seq[i:i+length]
        if segment == segment[::-1]:
            palindromes.append(segment)

    return palindromes

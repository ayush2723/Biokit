def find_splice_sites(seq, window=10):
    """
    Predicts potential splice donor and acceptor sites in a DNA sequence.

    Splice sites are short conserved sequences typically found at exon-intron boundaries:
    - Donor sites: 'GT' (beginning of intron)
    - Acceptor sites: 'AG' (end of intron)

    Args:
        seq (str): DNA sequence to analyze.

    Returns:
        Tuple[List[int], List[int]]: Two lists containing 0-based start indices of:
            - Donor site positions (GT)
            - Acceptor site positions (AG)
    """
    donor_sites = []
    acceptor_sites = []

    for i in range(len(seq) - 1):
        dinuc = seq[i:i+2].upper()
        if dinuc == 'GT':
            donor_sites.append(i)
        elif dinuc == 'AG':
            acceptor_sites.append(i)

    return donor_sites, acceptor_sites

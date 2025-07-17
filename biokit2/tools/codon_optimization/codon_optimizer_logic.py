# codon_optimizer.py
from biokit2.data.genetic_code import GENETIC_CODE
from biokit2.data.codon_usage import CODON_USAGE_TABLES

def optimize_sequence(dna_sequence: str, host: str) -> str:
    """
    Optimize a given DNA sequence for a specific host organism based on codon usage bias.

    This function translates the DNA sequence into codons, identifies the amino acid
    each codon encodes using the standard genetic code, and replaces each codon with
    the most frequently used synonymous codon preferred by the specified host.

    Args:
        dna_sequence (str): A string representing a DNA sequence (must be a multiple of 3 if possible).
        host (str): The name of the host organism whose codon usage table should be used 
                    (e.g., 'E.coli', 'Yeast').

    Returns:
        str: A host-optimized DNA sequence with synonymous codons preferred by the host.

    Raises:
        ValueError: If the specified host is not found in the codon usage table.

    Notes:
        - Incomplete codons (length < 3 at the end) are ignored.
        - Unknown or invalid codons are retained as-is in the output.
        - This function assumes the input DNA is valid and pre-cleaned.
    """
    host_usage = CODON_USAGE_TABLES.get(host)
    if not host_usage:
        raise ValueError(f"Host '{host}' not found in codon usage table.")
    
    optimized_sequence = ""
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        if len(codon) < 3:
            break  # ignore incomplete codon
        amino_acid = None
        # Find which amino acid this codon maps to
        for aa, codons in GENETIC_CODE.items():
            if codon in codons:
                amino_acid = aa
                break
        if not amino_acid:
            optimized_sequence += codon  
            continue
        
        # Get all codons that encode this amino acid
        possible_codons = GENETIC_CODE[amino_acid]
        
        # Find the most preferred one for this host
        best_codon = max(
            possible_codons,
            key=lambda c: host_usage.get(c, 0)
        )
        optimized_sequence += best_codon
    
    return optimized_sequence

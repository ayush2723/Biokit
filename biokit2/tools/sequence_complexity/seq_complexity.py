from collections import Counter
import math

def calculate_shannon_entropy(sequence: str) -> float:
    length = len(sequence)
    if length == 0:
        return 0.0
    freq = Counter(sequence)
    entropy = -sum((count / length) * math.log2(count / length) for count in freq.values())
    return round(entropy, 4)

def calculate_kmer_diversity(sequence: str, k: int) -> float:
    if len(sequence) < k:
        return 0.0
    kmer_counts = Counter(sequence[i:i+k] for i in range(len(sequence) - k + 1))
    total_kmers = sum(kmer_counts.values())
    diversity = len(kmer_counts) / total_kmers if total_kmers else 0
    return round(diversity, 4)

def estimate_sequence_complexity(sequence: str, k: int = 3) -> dict:
    entropy = calculate_shannon_entropy(sequence)
    diversity = calculate_kmer_diversity(sequence, k)
    return {
        "shannon_entropy": entropy,
        "kmer_diversity": diversity,
    }

def sliding_entropy_profile(sequence: str, window_size: int = 20, step: int = 5):
    entropies = []
    positions = []
    for i in range(0, len(sequence) - window_size + 1, step):
        window = sequence[i:i+window_size]
        entropy = calculate_shannon_entropy(window)
        entropies.append(entropy)
        positions.append(i + window_size // 2)
    return positions, entropies

def compute_prefix_sums(mutation_positions: list[int], length: int) -> list[int]:
    prefix = [0] * (length + 1)
    for pos in mutation_positions:
        if 0 <= pos < length:
            prefix[pos + 1] += 1

    for i in range(1, length + 1):
        prefix[i] += prefix[i - 1]

    return prefix


def find_hotspot_windows(mutation_positions: list[int], sequence_length: int, window_size: int, threshold: int) -> list[tuple[int, int, int]]:
    """
    Returns list of (start, end, mutation_count) for windows that have mutation count >= threshold
    """
    prefix = compute_prefix_sums(mutation_positions, sequence_length)
    hotspots = []

    for start in range(0, sequence_length - window_size + 1):
        end = start + window_size
        mutation_count = prefix[end] - prefix[start]
        if mutation_count >= threshold:
            hotspots.append((start, end, mutation_count))

    return hotspots

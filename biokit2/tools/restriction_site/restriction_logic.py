from biokit2.data.restriction_enzyme import restriction_enzymes

def find_restriction_sites(sequence, selected_enzymes):
    results = []

    for enzyme, site in restriction_enzymes.items():
        if enzyme not in selected_enzymes:
            continue

        cut_positions = []
        index = sequence.find(site)
        while index != -1:
            cut_positions.append(index + 1)  
            index = sequence.find(site, index + 1)

        if cut_positions:
            results.append({
                "enzyme": enzyme,
                "site": site,
                "positions": cut_positions,
                "count": len(cut_positions)
            })

    return results

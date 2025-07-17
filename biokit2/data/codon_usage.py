# codon usage(change according to host) standard table from kazusa codon usage database 

CODON_USAGE_TABLES = {
    "E_coli": { #bacteria specimen
        'TTT': 0.44, 'TTC': 0.56, 'TTA': 0.13, 'TTG': 0.13, 'CTT': 0.13, 'CTC': 0.10,
        'CTA': 0.04, 'CTG': 0.47, 'ATT': 0.49, 'ATC': 0.39, 'ATA': 0.11, 'ATG': 1.00,
        'GTT': 0.18, 'GTC': 0.24, 'GTA': 0.17, 'GTG': 0.41, 'TCT': 0.21, 'TCC': 0.22,
        'TCA': 0.16, 'TCG': 0.11, 'AGT': 0.14, 'AGC': 0.16, 'CCT': 0.31, 'CCC': 0.18,
        'CCA': 0.28, 'CCG': 0.22, 'ACT': 0.24, 'ACC': 0.36, 'ACA': 0.28, 'ACG': 0.11,
        'GCT': 0.27, 'GCC': 0.40, 'GCA': 0.23, 'GCG': 0.11, 'TAT': 0.44, 'TAC': 0.56,
        'TAA': 0.30, 'TAG': 0.24, 'TGA': 0.46, 'CAT': 0.42, 'CAC': 0.58, 'CAA': 0.34,
        'CAG': 0.66, 'AAT': 0.47, 'AAC': 0.53, 'AAA': 0.76, 'AAG': 0.24, 'GAT': 0.63,
        'GAC': 0.37, 'GAA': 0.68, 'GAG': 0.32, 'TGT': 0.46, 'TGC': 0.54, 'TGG': 1.00,
        'CGT': 0.36, 'CGC': 0.36, 'CGA': 0.07, 'CGG': 0.11, 'AGA': 0.05, 'AGG': 0.06,
        'GGT': 0.34, 'GGC': 0.37, 'GGA': 0.13, 'GGG': 0.16
    },

    "Human": {
        'TTT': 0.46, 'TTC': 0.54, 'TTA': 0.07, 'TTG': 0.13, 'CTT': 0.13, 'CTC': 0.20,
        'CTA': 0.07, 'CTG': 0.40, 'ATT': 0.36, 'ATC': 0.47, 'ATA': 0.17, 'ATG': 1.00,
        'GTT': 0.18, 'GTC': 0.24, 'GTA': 0.11, 'GTG': 0.47, 'TCT': 0.18, 'TCC': 0.22,
        'TCA': 0.15, 'TCG': 0.06, 'AGT': 0.15, 'AGC': 0.24, 'CCT': 0.28, 'CCC': 0.32,
        'CCA': 0.27, 'CCG': 0.13, 'ACT': 0.24, 'ACC': 0.36, 'ACA': 0.28, 'ACG': 0.12,
        'GCT': 0.27, 'GCC': 0.40, 'GCA': 0.23, 'GCG': 0.11, 'TAT': 0.43, 'TAC': 0.57,
        'TAA': 0.30, 'TAG': 0.24, 'TGA': 0.46, 'CAT': 0.42, 'CAC': 0.58, 'CAA': 0.25,
        'CAG': 0.75, 'AAT': 0.47, 'AAC': 0.53, 'AAA': 0.43, 'AAG': 0.57, 'GAT': 0.46,
        'GAC': 0.54, 'GAA': 0.42, 'GAG': 0.58, 'TGT': 0.46, 'TGC': 0.54, 'TGG': 1.00,
        'CGT': 0.08, 'CGC': 0.19, 'CGA': 0.11, 'CGG': 0.20, 'AGA': 0.21, 'AGG': 0.21,
        'GGT': 0.16, 'GGC': 0.34, 'GGA': 0.25, 'GGG': 0.25
    },

    "Yeast": { #fungus specimen
        'TTT': 0.57, 'TTC': 0.43, 'TTA': 0.29, 'TTG': 0.13, 'CTT': 0.17, 'CTC': 0.07,
        'CTA': 0.04, 'CTG': 0.10, 'ATT': 0.47, 'ATC': 0.36, 'ATA': 0.17, 'ATG': 1.00,
        'GTT': 0.21, 'GTC': 0.27, 'GTA': 0.11, 'GTG': 0.41, 'TCT': 0.29, 'TCC': 0.17,
        'TCA': 0.21, 'TCG': 0.07, 'AGT': 0.13, 'AGC': 0.13, 'CCT': 0.31, 'CCC': 0.18,
        'CCA': 0.28, 'CCG': 0.23, 'ACT': 0.22, 'ACC': 0.31, 'ACA': 0.31, 'ACG': 0.16,
        'GCT': 0.29, 'GCC': 0.34, 'GCA': 0.22, 'GCG': 0.15, 'TAT': 0.43, 'TAC': 0.57,
        'TAA': 0.35, 'TAG': 0.15, 'TGA': 0.50, 'CAT': 0.38, 'CAC': 0.62, 'CAA': 0.34,
        'CAG': 0.66, 'AAT': 0.44, 'AAC': 0.56, 'AAA': 0.42, 'AAG': 0.58, 'GAT': 0.45,
        'GAC': 0.55, 'GAA': 0.43, 'GAG': 0.57, 'TGT': 0.42, 'TGC': 0.58, 'TGG': 1.00,
        'CGT': 0.10, 'CGC': 0.18, 'CGA': 0.07, 'CGG': 0.12, 'AGA': 0.21, 'AGG': 0.32,
        'GGT': 0.18, 'GGC': 0.37, 'GGA': 0.22, 'GGG': 0.23
    },

    "Mouse": { #mammal specimen
        'TTT': 0.45, 'TTC': 0.55, 'TTA': 0.08, 'TTG': 0.13, 'CTT': 0.13, 'CTC': 0.21,
        'CTA': 0.07, 'CTG': 0.38, 'ATT': 0.36, 'ATC': 0.47, 'ATA': 0.17, 'ATG': 1.00,
        'GTT': 0.18, 'GTC': 0.24, 'GTA': 0.11, 'GTG': 0.47, 'TCT': 0.19, 'TCC': 0.22,
        'TCA': 0.15, 'TCG': 0.06, 'AGT': 0.15, 'AGC': 0.23, 'CCT': 0.28, 'CCC': 0.32,
        'CCA': 0.27, 'CCG': 0.13, 'ACT': 0.24, 'ACC': 0.36, 'ACA': 0.28, 'ACG': 0.12,
        'GCT': 0.27, 'GCC': 0.40, 'GCA': 0.23, 'GCG': 0.11, 'TAT': 0.44, 'TAC': 0.56,
        'TAA': 0.30, 'TAG': 0.24, 'TGA': 0.46, 'CAT': 0.41, 'CAC': 0.59, 'CAA': 0.26,
        'CAG': 0.74, 'AAT': 0.47, 'AAC': 0.53, 'AAA': 0.43, 'AAG': 0.57, 'GAT': 0.46,
        'GAC': 0.54, 'GAA': 0.42, 'GAG': 0.58, 'TGT': 0.45, 'TGC': 0.55, 'TGG': 1.00,
        'CGT': 0.08, 'CGC': 0.19, 'CGA': 0.11, 'CGG': 0.20, 'AGA': 0.21, 'AGG': 0.21,
        'GGT': 0.16, 'GGC': 0.34, 'GGA': 0.25, 'GGG': 0.25
    },

    "Arabidopsis": { #plant specimen
        'TTT': 0.46, 'TTC': 0.54, 'TTA': 0.07, 'TTG': 0.13, 'CTT': 0.13, 'CTC': 0.21,
        'CTA': 0.07, 'CTG': 0.38, 'ATT': 0.35, 'ATC': 0.47, 'ATA': 0.18, 'ATG': 1.00,
        'GTT': 0.17, 'GTC': 0.24, 'GTA': 0.12, 'GTG': 0.47, 'TCT': 0.19, 'TCC': 0.21,
        'TCA': 0.16, 'TCG': 0.07, 'AGT': 0.14, 'AGC': 0.23, 'CCT': 0.27, 'CCC': 0.32,
        'CCA': 0.28, 'CCG': 0.13, 'ACT': 0.24, 'ACC': 0.35, 'ACA': 0.29, 'ACG': 0.12,
        'GCT': 0.27, 'GCC': 0.39, 'GCA': 0.23, 'GCG': 0.11, 'TAT': 0.44, 'TAC': 0.56,
        'TAA': 0.30, 'TAG': 0.24, 'TGA': 0.46, 'CAT': 0.42, 'CAC': 0.58, 'CAA': 0.25,
        'CAG': 0.75, 'AAT': 0.47, 'AAC': 0.53, 'AAA': 0.43, 'AAG': 0.57, 'GAT': 0.46,
        'GAC': 0.54, 'GAA': 0.42, 'GAG': 0.58, 'TGT': 0.46, 'TGC': 0.54, 'TGG': 1.00,
        'CGT': 0.08, 'CGC': 0.19, 'CGA': 0.11, 'CGG': 0.20, 'AGA': 0.21, 'AGG': 0.21,
        'GGT': 0.16, 'GGC': 0.33, 'GGA': 0.26, 'GGG': 0.25
    }
}

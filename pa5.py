"""
PA5:
Gene Sequencing

EXAMPLE INPUT:
CCTGATGCGGTA

EXAMPLE OUTPUT:
The DNA strand is:CCTGATGCGGTA
The complimentary strand is:GGACTACGCCAT
The reverse of the complimentary strand is:TACCGCATCAGG
The mRNA strand of the reverse of the complimentary strand is:AUGGCGUAGUCC
The Codons are:
['AUG', 'GCG', 'UAG', 'UCC']
The Index of the START primer is: 0
the Index of the first STOP codon is: 2
The Protein is:
['START', 'Ala', 'STOP']
The steps reversed are:
['AUG', 'GCG', 'UAG', 'UCC']
AUGGCGUAGUCC
TACCGCATCAGG
GGACTACGCCAT
CCTGATGCGGTA
The original strand is:CCTGATGCGGTA
The final strand is:CCTGATGCGGTA

There is no test function provided. I provide a simple set of print statements at the bottom. You have freedom for what you name things, and how you structure your code, with the exception of the DNAReplicator(). You will need to test your code yourself. YOUR OUTPUT SHOULD MATCH THE SAMPLE OUTPUT!

You have a few hints and limiatations to help you out:
- In your main function, you will need to call your functions in the correct order.
- You can ONLY USE 5 VARIABLES IN YOUR MAIN FUNCTION. You can use as many variables as you want in your various functions, but you can only use 5 variables in your main function.
    - You need to have an ogStrand variable that holds the original strand. This is to preserve the original strand, so you can compare it to the final strand.
    - You will need to have a temp variable that initially holds the original strand. Call it what you want, but most functions will update this variable. You will need to update this variable as you go through the steps. MOST of your functions will return a value, and you will need to update the temp variable to hold that value.
    - startIndex
    - endIndex
    - proteinList 

I will use the following sequences to test your code:
"CCTGATGCGGTA"
"CCTGATGCGGA" >> invalid
"CGATCGATCGATCGATCGATCGATCGATCGATCGATAATCCGATCGATCGATCTGATCGATCGATCGATCGATCGATGACTGGCGTAATCGATAGCTGA"


"""
AminoAcidChart = {"UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu", "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP", "UAG": "STOP", "UGU": "Cys", "UGC": "Cys", "UGA": "STOP", "UGG": "Trp", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro", "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "START", "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr", "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg", "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val", "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala", "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu", "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
                  }

print("-. .-.   .-. .-.   .-. .-.   .\n||\|||\ /|||\|||\ /|||\|||\ /|\n|/ \|||\|||/ \|||\|||/ \|||\||\n~   `-~ `-`   `-~ `-`   `-~ `-")

# DO NOT EDIT ABOVE THIS LINE
# DO YOUR WORK BELOW


def isValidDNASequence(sequence):

    valid_nucleotides = set(['A', 'T', 'G', 'C'])
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            return False
    if len(sequence) < 9:
        return False
    if len(sequence) % 3 != 0:
        return False
    return True


def DNAReplicator(dna_sequence):
    if not isValidDNASequence(dna_sequence):
        print("Invalid DNA Sequence")
    else:
        return dna_sequence


def getComplementarySequence(dna_sequence):
    dna_sequence = dna_sequence.upper()
    rna_sequence = ""
    for nucleotide in dna_sequence:
        if nucleotide == "T":
            rna_sequence += "A"
        elif nucleotide == "A":
            rna_sequence += "T"
        elif nucleotide == "G":
            rna_sequence += "C"
        elif nucleotide == "C":
            rna_sequence += "G"
    if isValidDNASequence(dna_sequence) == False:
        return ""
    return rna_sequence


def reverse_complement(dna_sequence):
    return getComplementarySequence(dna_sequence[::-1])


def getmRNASequence(dna_sequence):
    dna_sequence = reverse_complement(dna_sequence)
    rna_sequence = ""
    for nucleotide in dna_sequence:
        if nucleotide == "A":
            rna_sequence += "U"
        elif nucleotide == "T":
            rna_sequence += "A"
        elif nucleotide == "C":
            rna_sequence += "G"
        elif nucleotide == "G":
            rna_sequence += "C"
    return rna_sequence


def breakIntoCodons(mrna_sequence):
    mrna_sequence = getmRNASequence(mrna_sequence)
    codons = ''

    codons = [mrna_sequence[i:i+3] for i in range(0, len(mrna_sequence), 3)]
    return codons


def getIndexStartCodon(codon):
    return (breakIntoCodons(codon).index('AUG'))


def getIndexStopCodon(codon):
    stop_codons = breakIntoCodons(codon)
    stop = (["UAA", "UAG", "UGA"])
    for i in stop:
        if i in stop_codons:
            return stop_codons.index(i)


def getAminoAcidSequence(codons):
    codons = breakIntoCodons(codons)
    amino_acids = []
    for codon in codons:
        amino_acid = AminoAcidChart[codon]
        amino_acids.append(amino_acid)

    return amino_acids


def getSequence(sequence):
    acids = getAminoAcidSequence(sequence)
    start = getIndexStartCodon(sequence)
    stop = getIndexStopCodon(sequence)
    newSeq = []

    newSeq = acids[start:stop+1]

    return newSeq


def returnDna(sequence):
    codons = breakIntoCodons(sequence)
    print(codons)

    print("".join(codons))

    print(reverse_complement(sequence))
    print(getComplementarySequence(sequence))

    replica = DNAReplicator(sequence)

    return replica


# DO NOT MODIFY BELOW THIS LINE, BUT YOU MAY COMMENT IT OUT TO TEST YOUR CODE
ogStrand = "CGATCGATCGATCGATCGATCGATCGATCGATCGATAATCCGATCGATCGATCTGATCGATCGATCGATCGATCGATGACTGGCGTAATCGATAGCTGA"
finalStrand = DNAReplicator(ogStrand)

print("The original strand is:" + ogStrand)
print("The final strand is:" + finalStrand)

assert finalStrand == ogStrand, "The final strand is not the same as the original strand"
print("The final strand is the same as the original strand")

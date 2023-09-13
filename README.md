[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10784233)
# PA5:
## Gene Sequencing

For this assignment, you will use code to simulate the process of replicating DNA.

# BACKGROUND
Some videos to watch to help you understand the process:
- https://www.youtube.com/watch?v=TNKWgcFPHqw&ab_channel=yourgenome >> DNA Replication
- https://www.youtube.com/watch?v=gG7uCskUOrA&ab_channel=yourgenome >> From DNA to Protein

If you haven't already, watch this video on how DNA works: https://www.youtube.com/watch?v=zwibgNGe4aY&ab_channel=StatedClearly

The (very simplified) process of DNA replication is as follows:

1. DNA is a double helix, with 2 strands of DNA. Each strand has a 3' end and a 5' end. The 3' end is the end of the strand that has the first nucleotide in the sequence. The 5' end is the end of the strand that has the last nucleotide in the sequence. The strands run in opposite directions. DNA sequences are read from the 3' end to the 5' end. 

    Beginning of the strand, so this is the 5' strand -->  5' - - - - - - - - - - - - - 3'  <-- This is the strand you are given
    Beginning of the strand, so this is the 3' strand -->  3' - - - - - - - - - - - - - 5'  <-- You will need to make this strand
    

    5' - T A G C T A G A C C A G T G - 3'  <-- This is the strand you are given
    3' - A T C G A T C T G G T C A C - 5'  <-- You will need to make this strand
      


2. The DNA strand is split into two strands by an enzyme called helicase.
    - The DNA sequence you are given already splits the strand into two strands
                
                 / - - - - - - - 3' <-- This is the strand you are given
                /
        5' -----
        3' -----
                \
                 \ - - - - - - - 5' <-- You will need to make this strand 
      

    - THE INITIAL SEQUENCE IS GIVEN WITH THE 5' ON THE LEFT, AND 3' ON THE RIGHT. REMEMBER: THE 5' END IS THE END OF THE STRAND THAT HAS THE LAST NUCLEOTIDE IN THE SEQUENCE. 
    - FOR ALL OTHER DNA SEQUENCES IN THIS ASSIGNMENT, ASSUME THE LEFT SIDE IS THE 3' END, AND THE RIGHT SIDE IS THE 5' END.
    
    The DNA sequence you are given what starts at the 5' end of the DNA sequence. You will need to match base pairs to get the complimentary strand, and then you will then need to reverse it.
        - For example, if the DNA sequence you are given is "ATCG", you reverse it to put the 3' end on the left side, and the 5' end on the right side. This gets you "GCTA". Then, you match the base pairs to get the complimentary strand. This gets you "CGAT"

            5' - A T C G  - 3' <-- This is the strand you are given
            3' - T A G C  - 5' <-- You will need to make this strand 
                                    (but you will need to reverse it so it reads from the 3' end on the left to the 5' end on the right)

        - You can reverse a string by using the [::-1] slice. For example, "house"[::-1] will return "esuoh". 
        - The CREATED strand will be the one you use going forward.

3. Primase adds a short RNA primer to the 3' end of each strand. It is a short sequence of RNA that is used to start the replication process. This sequence is called a primer. This isn't always the case, but the most common primer is 3 nucleotides long, and it is usually "AUG". This is called the Start Codon. Notice that AUG is RNA, not DNA... So pay attention to where you are using RNA and where you are using DNA. 
4. An enzyme called DNA polymerase binds to the primer and adds nucleotides from the 3' end to the 5' end. 
    - In reality, there is a "Leading Strand" and a "Lagging Strand" but we aren't going to worry about that for this assignment. 
5. This process continues until the entire sequence is replicated. Before you can start replication, you need to know when to stop. The replication ends when the DNA polymerase reaches a STOP codon. The STOP codon is a sequence of 3 nucleotides that tells the DNA polymerase to stop replicating. The most common STOP codons are UAA, UAG, or UGA. Again, notice that AUG is RNA, not DNA...
    - You will need to write a stopCodon() function that takes in a string, and returns the INDEX of the first STOP codon in the string.


# PROJECT STEPS:
1. Copy your isValidDNASequence(). You will need to use it in this part.
2. Create a function called DNAReplicator(). This function will take in a DNA sequence and return the strand after replication. Check if the strand passed in is valid. If not, return "NOT A VALID STRAND OF DNA"
3. Get the complimentary strand. Use your previous functions to get the complimentary strand. This is the only time you will need to call isValidDNASequence() in this part. 
4. Reverse the complimentary strand. Use the [::-1] slice to reverse the complimentary strand. Return the reversed complimentary strand.
5. Get the mRNA strand, using previously written functions. 
6. Break the resulting strand into codons. NOTE: You will have to make sure you are not checking if it's a valid DNA sequence, it will be RNA at this point.
7. Get the index of the AUG primer (Start Codon) from your codon list. Create a primase() [ or getIndexStartCodon()] function to get the index of the AUG primer. 
8. Get the index of the first STOP codon encountered. Write a getIndexStopCodon() function to get the index of the first STOP codon. 
9. Get the amino acid list (including the Start and Stop amino acids). Use previously written functions to get the amino acid list.  NOTE: this is technically a different process then replication, but it's the same idea. You are taking a strand of DNA, and you are converting it to a strand of amino acids. THIS SHOULD INCLUDE THE START AND STOP AMINO ACIDS, AND EVERYTHING IN BETWEEN. It should not include amino acids outside of that range.
10. Convert the codon list back into the original DNA strand. You will need to create a new function for this.
    - Merge the codon list into a string.
    - convert from mRNA back to DNA (you may need to create a new function for this)
    - reverse the strand to get the initial complimentary strand
    - convert from complimentary strand BACK to the original DNA strand
        - You will need to make a new dictionary called nucleotides_for_RNA_to_DNA
        - You will need to make a new function called getDNASequencefromRNA()

Exampe output can be found in the project file.

# REQUIREMENTS
There is no test function provided. I provide a simple set of print statements at the bottom. You have freedom for what you name things, and how you structure your code, with the exception of the DNAReplicator(). You will need to test your code yourself. YOUR OUTPUT SHOULD MATCH THE SAMPLE OUTPUT!

### You have a few hints and limiatations to help you out:
- In your main function, you will need to call your functions in the correct order. You will need to print after each step
- You can ONLY USE 4 VARIABLES IN YOUR MAIN FUNCTION. You can use as many variables as you want in your various functions, but you can only use 4 variables in your main function.
    - You will need to have a temp variable that initially holds the original strand. Call it what you want, but most functions will update this variable. You will need to update this variable as you go through the steps. MOST of your functions will return a value, and you will need to update the temp variable to hold that value.
    - startIndex
    - endIndex
    - proteinList 

I will use the following sequences to test your code:
"CCTGATGCGGTA"

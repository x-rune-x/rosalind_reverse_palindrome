class DnaSeq:
    def __init__(self, fasta_id, seq):
        self.fasta_id = fasta_id
        self.seq = seq.lower()
        self.length = len(seq)


def rev_complement(dna_input):
    # Create the complement then reverse slice it to get the reverse complement of the DNA.
    nuc_pairs = {
        "a": "t",
        "t": "a",
        "c": "g",
        "g": "c"
    }
    complement = ""
    for base in dna_input:
        complement += nuc_pairs[base]

    reverse_complement = complement[::-1]

    return reverse_complement


def find_palindrome(dna_input):
    dna_input = dna_input.lower()
    palindrome_positions = []
    for position in range(len(dna_input)):
        # Go through each position in the sequence and check if there is a palindrome in the bases downstream of it.
        test_lengths = [12, 10, 8, 6, 4]
        # Number of bases downstream to check for palindromes. Rosalind set the lengths between 12 and 4.
        # We only need to check even numbers since palindromes must be even in length.
        for length in test_lengths:
            test_seq = dna_input[position: position+length]
            if test_seq == rev_complement(test_seq) and len(test_seq) == length:
                palindrome_positions.append([position+1, length])
                # Want to prioritise the longest possible palindrome so move on to the next position as soon as one is
                # found. E.g. if a palindrome is found at 8, one will also exist at 6 and 4 but we only care about 8.
                break

    return palindrome_positions


def process_file(input_file):
    file = open(input_file)
    fasta_id = file.readline().strip()
    lines = file.readlines()
    fasta_seq = ''
    for line in lines:
        fasta_seq += line.strip()
    seq_obj = DnaSeq(fasta_id, fasta_seq)
    file.close()

    palindrome_list = find_palindrome(seq_obj.seq)

    solution = ''
    for palindrome in palindrome_list:
        solution += str(palindrome[0]) + " " + str(palindrome[1]) + '\n'

    solution_file = open('solution_file.txt', 'w')
    solution_file.write(solution)
    solution_file.close()
    print(solution)


process_file('rosalind_revp.txt')

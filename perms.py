def calculate_permutations_manual(file_path):
    permutations = set()

    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)

        line_num = 0
        for line in file:
            line_num += 1

            # Split the line by tabs
            columns = line.strip().split('\t')
            
            # Extract columns 3 to 19 (index 2 to 18 in 0-based indexing)
            relevant_columns = columns[3:19]
            
            # Convert the relevant columns to a string
            row_string = ''.join(relevant_columns)
            if line_num < 5:
                print(f"Permutation at line {line_num+1}: {row_string}")

            # Add the row string to the set of permutations
            permutations.add(row_string)

    print(f"Number of unique permutations: {len(permutations)}")
    return permutations

if __name__ == "__main__":
    file_path = './VoterFile_byRace-Table 1.tsv'
    calculate_permutations_manual(file_path)

#!/usr/bin/env python3

import sys
import os

def read_directory(input_dir):
    """
    Reads all the files in the input directory and sorts the file names
    
    Returns: sorted list of file names 
    """

    files = os.listdir(input_dir)
    sorted_files = sorted(files)
    return sorted_files


def read_term_frequencies(filename):
    """
    Reads a file containing the term and its frequencies
    
    Returns: dictionary containing the terms as the key and their
    frequencies as the value
    """

    terms = {}

    files = open(filename, 'r')
    for line in files:
        term, frequency = line.strip().split()
        terms[term] = int(frequency)
    files.close()

    return terms


def create_matrix(files, terms, input_dir):
    """
    Creates a term-document  matrix where the rows represent the terms 
    and the columns represent the documents

    Returns: 2D matrix representing the term-document matrix
    """
    
    # Create an empty 2D matrix (list of list) initialized with zeros
    # Number of rows = number of unique terms
    # Number of columns = number of files
    matrix = [[0 for _ in range(len(files))] for _ in range(len(terms))]

    for i, filename in enumerate(files): # Iterate over the files list
        term_frequencies = read_term_frequencies(os.path.join(input_dir, filename)) 

        for j, term in enumerate(terms): # Iterate over the terms in the term-frequency dict
            if term in term_frequencies:
                matrix[j][i] = term_frequencies[term] # If the term is in the dict, set the corresponding cell in the matrix to its frequency

    return matrix


def save_output(output_dir, sorted_files, sorted_terms, matrix):
    """
    Save the sorted documents, sorted terms and term-document matrix to
    an output directory

    Returns: None
    """

    os.makedirs(output_dir) # Make the output directory to put the respective files inside

    # Save sorted terms to a file called: sorted_terms.txt
    terms_file = open(os.path.join(output_dir, 'sorted_terms.txt'), 'w')
    for term in sorted_terms: # Iterate through each term in the sorted_terms list
        terms_file.write(term + '\n') # Write the current term in sorted_terms.txt followed by a newline
    terms_file.close() # Close sorted_terms.txt to save changes

    # Save the sorted documents to a file called sorted_documents.txt
    files_file = open(os.path.join(output_dir, 'sorted_documents.txt'), 'w')
    for files in sorted_files:
        files_file.write(files + '\n')
    files_file.close()

    # Save the term-document matrix to a file called: td_matrix.txt
    matrix_file = open(os.path.join(output_dir, 'td_matrix.txt'), 'w')
    # Write the dimensions of the term-document matrix to td_matrix.txt: number of rows + number of columns + newline
    matrix_file.write(str(len(sorted_terms)) + " " + str(len(sorted_files)) + "\n")
    for row in matrix:
        row_data = " ".join(map(str, row)) # Convert the values in the current row to a string separated by spaces
        matrix_file.write(row_data + '\n')
    matrix_file.close()


def main():
    """
    Calls helper functions to read documents, sort the terms in the
    documents, create a term-document matrix and save the respective
    files in the output directory
    """  

    if len(sys.argv) != 3: # Checks if the command-line arguments are correctly provided
        sys.exit(1)
     
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    sorted_files = read_directory(input_dir)

    terms = set()
    for filename in sorted_files:
        terms.update(read_term_frequencies(os.path.join(input_dir, filename))) # Update the terms set with terms from the current file
 
    sorted_terms = sorted(terms)

    matrix = create_matrix(sorted_files, sorted_terms, input_dir)

    save_output(output_dir, sorted_files, sorted_terms, matrix)

if __name__ == "__main__":
    main()

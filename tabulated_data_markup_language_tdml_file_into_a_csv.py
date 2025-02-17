# create data
def write_data_to_tdml_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)

files_tdml = ["f1.tdml", "f2.tdml", "f3.tdml"] 

data_01 = """
Type
Procedure
Adversary control(s)
Objective
"""

data_02 = """
IND-CPA
Challenger: KE, KD = KG(security parameter)
Adversary: m0, m1 = choose 2 messages of the same length. Send m0, m1 to challenger. Perform additional operations in polynomial time including calls to the encryption oracle.
Challenger: b = randomly choose between 0 and 1
Challenger: C := E(KE, mb). Send C to adversary.
Adversary: perform additional operations in polynomial time including calls to the encryption oracle. Output guess.
If guess = b, the adversary wins.
Restriction: Messages to be of the same length aim to prevent adversary from trivially winning the game by just comparing the length of ciphertexts. However, this requirement is weak, especially because it assumes only a single interaction between adversary and challenger.
Plaintext messages.
Ciphertext messages.
e.g. adversary has Mark’s public key.
Adversary tries to guess which of the messages was encrypted.
"""

data_03 = """
IND-CPA1
Challenger: KE,KD = KG(security parameter)
Adversary (a polynomially-bounded number of times): call the encryption or decryption oracle for arbitrary plaintexts or ciphertexts, respectively
Adversary: m0,m1= choose 2 messages of the same length
Challenger: b= randomly choose between 0 and 1
Challenger: C:=E(KE,mb)Send C to adversary.
Adversary: perform additional operations in polynomial time. Output guess
If guess=b, the adversary wins
Use / abuse service as decryption oracle (but cannot depend on the challenge y).
Adversary tries to guess which of the messages was encrypted.
"""

data_list = [data_01, data_02, data_03]

for file, data in zip(files_tdml, data_list):
    write_data_to_tdml_file(file, data)

# converts a Tabulated Data Markup Language (TDML) file into a CSV file, stitching data column by column. This assumes TDML is structured as tabular data in a clear text format, rather than an XML-based format.

import csv
import argparse
import glob

def read_tdml(file_path):
    """
    Reads a TDML file and returns the parsed data as a list of lists.
    Assumes each section is separated by new lines.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def write_csv(headers, data, output_file):
    """Writes the given tabulated data to a CSV file."""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(zip(*data))

def tdml_to_csv(tdml_files, output_file):
    """
    Converts multiple TDML files into a single CSV by extracting headers and columns.
    """
    all_data = []
    headers = []
    
    for tdml_file in tdml_files:
        tdml_data = read_tdml(tdml_file)
        if tdml_data:
            headers.append(tdml_data[0])  # First line as header
            all_data.append(tdml_data[1:])  # Rest as column data
    
    write_csv(headers, all_data, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert TDML files to CSV format.")
    parser.add_argument('-o', '--output', default='output.csv', help="Output CSV file")
    # Use parse_known_args to ignore any unknown arguments like the kernel's default args
    args, unknown = parser.parse_known_args()
    
    tdml_files = sorted(glob.glob("f*.tdml"))  # Pick up all f1.tdml, f2.tdml, etc.
    tdml_to_csv(tdml_files, args.output)
    print(f"CSV saved as {args.output}")




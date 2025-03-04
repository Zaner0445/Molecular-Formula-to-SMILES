# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:05:58 2025
"""

import pubchempy as pcp
import pandas as pd
import time

# Set file paths
input_file = r"path_to_input_file.csv"
output_file = r"path_to_output_file.csv"
error_log = r"path_to_error_log.txt"

# Read the input CSV
df = pd.read_csv(input_file)

# Add empty columns for SMILES and InChI
df['SMILES'] = ""
df['InChI'] = ""

# Process each molecular formula
for index, row in df.iterrows():
    formula = row['Molecular_Formula']  # Adjust column name if necessary
    try:
        # Query PubChem for the molecular formula
        compounds = pcp.get_compounds(formula, "formula")
        if compounds:
            # Extract SMILES and InChI
            df.at[index, 'SMILES'] = compounds[0].isomeric_smiles
            df.at[index, 'InChI'] = compounds[0].inchi
        else:
            print(f"No match found for formula {formula}")
    except Exception as e:
        print(f"Error for formula {formula}: {e}")
        with open(error_log, "a") as log:
            log.write(f"{formula}: {e}\n")
    time.sleep(1)  # Prevent overloading the PubChem API

# Save the updated dataframe
df.to_csv(output_file, index=False)
print("SMILES and InChI retrieval completed!")

# Convert the CSV to TSV
output_tsv = r"path_to_output_file.tsv"

df.to_csv(output_tsv, sep='\t', index=False)
print(f"CSV successfully converted to TSV and saved at: {output_tsv}")

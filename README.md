PubChem SMILES and InChI Retriever
Description
This script fetches SMILES and InChI data from PubChem based on molecular formulas provided in input CSV files. The output is a CSV file with added columns for SMILES and InChI corresponding to each molecular formula.

Features
Fetches chemical information (SMILES and InChI) from PubChem using the molecular formula.
Supports batch processing of CSV files.
Logs any errors encountered while fetching data to an error log file.
Requirements
Python 3.x
pubchempy: A Python wrapper for the PubChem PUG REST API
pandas: For data manipulation and CSV handling
Install the required libraries via pip:

bash
Copy
Edit
pip install pubchempy pandas
Usage
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/repository-name.git
cd repository-name
Update the file paths in the script (input_file, output_file, error_log) to point to your input CSV, desired output CSV, and error log location.

Run the script:

bash
Copy
Edit
python fetch_smiles_inchi.py
After execution, the output CSV will contain two new columns: SMILES and InChI. An error log will also be created if any issues are encountered.

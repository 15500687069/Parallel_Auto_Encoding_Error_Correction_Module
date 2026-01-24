import nbformat
import os
import argparse

def fix_notebook_metadata(file_path):
    """
    Cleans invalid widget metadata and escape sequences from the notebook 
    to ensure compatibility with Google Colab and standard nbconvert.
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return

    print(f"Processing notebook: {file_path}...")

    try:
        # Load the notebook content
        with open(file_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)

        # 1. Remove widget metadata that causes State Key errors
        if 'widgets' in nb.metadata:
            print("Detected 'widgets' metadata. Cleaning...")
            del nb.metadata['widgets']
            metadata_fixed = True
        else:
            print("No problematic widget metadata found.")
            metadata_fixed = False

        # 2. Fix potential invalid escape sequences in cell source code
        # This prevents 'SyntaxWarning: invalid escape sequence'
        sequences_fixed = 0
        for cell in nb.cells:
            if cell.cell_type == 'code':
                # Replace Windows-style backslashes in paths with forward slashes
                if 'D:\\' in cell.source or 'C:\\' in cell.source:
                    cell.source = cell.source.replace('\\', '/')
                    sequences_fixed += 1

        if metadata_fixed or sequences_fixed > 0:
            # Write the cleaned notebook back to disk
            with open(file_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            print(f"Success: File '{file_path}' has been repaired.")
            if sequences_fixed > 0:
                print(f"Fixed {sequences_fixed} path/escape sequences.")
        else:
            print("Notebook is already clean. No changes made.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Setup command line argument parsing
    parser = argparse.ArgumentParser(description="Repair Notebook Metadata for PAER Reproduction")
    parser.add_argument("file", help="Path to the .ipynb file")
    
    args = parser.parse_args()
    fix_notebook_metadata(args.file)

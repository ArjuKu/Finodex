"""
================================================================================
CSV TO EXCEL CONVERTER
================================================================================

This script converts CSV files to properly formatted Excel files.

USAGE:
    1. Install required libraries: pip install pandas openpyxl
    2. Run: python csv_to_excel.py
    3. Excel files will be created in the same folders

The CSV files work fine when opened in Excel, but this creates
proper .xlsx files with better formatting.
================================================================================
"""

import os
import pandas as pd

def convert_csv_to_excel():
    """Convert all CSV files to Excel format"""
    
    # Find all CSV files
    csv_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    
    print(f"Found {len(csv_files)} CSV files")
    
    for csv_file in csv_files:
        # Read CSV
        df = pd.read_csv(csv_file, header=None)
        
        # Create Excel filename
        excel_file = csv_file.replace('.csv', '.xlsx')
        
        # Write to Excel
        df.to_excel(excel_file, index=False, header=False)
        
        print(f"Created: {excel_file}")
    
    print("\nConversion complete!")
    print("You can now use the .xlsx files")

if __name__ == "__main__":
    print("CSV to Excel Converter")
    print("=" * 50)
    convert_csv_to_excel()

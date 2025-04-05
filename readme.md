# Tabulated Data Markup Language (TDML) file into a CSV 

[Method 01]
✅ 1. Text File Format (Before CSV)
Instead of spaces (which can appear inside data), we'll use a custom delimiter such as | or ; or any character `[delimiter]` stored in a variable delimiter.

🧪 Example Usage: ![method_01](method_01/tdml_file_into_csv.py)

![data.txt.png](method_01/data.txt.png) ➡️➡️➡️ ![data.csv.png](method_01/data.csv.png) 

[Method 02]
Converts a Tabulated Data Markup Language (TDML) file into a CSV file, stitching data column by column. This assumes TDML is structured as tabular data in a clear text format, rather than an XML-based format.

The script processes multiple TDML files (f1.tdml, f2.tdml, f3.tdml, etc.), automatically detecting them and converting them into a single CSV file. 🚀

![tabulated_data_markup_language_tdml_file_into_a_csv](tabulated_data_markup_language_tdml_file_into_a_csv.png)


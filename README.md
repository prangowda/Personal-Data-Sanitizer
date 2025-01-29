# Personal-Data-Sanitizer

 This Python tool helps users detect and redact personally identifiable information (PII) from text files, CSVs, or documents before sharing them.


#Features

1.Detect PII: Identifies sensitive data like names, emails, phone numbers, addresses, and credit card details.

2.Redact PII: Replaces detected PII with masked values (e.g., **** or [REDACTED]).

3.File Support: Works with text files (.txt), CSVs (.csv), and JSON (.json).

4.Export Cleaned Data: Saves a sanitized version of the input file.

5.Simple CLI and GUI: Command-line usage with an optional graphical interface.

_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#Code Implementation

We will use Python with the re (regex), pandas, tkinter, and fpdf libraries.

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#How to Run

1.Install dependencies:

    pip install pandas fpdf
    
2.Save the script as pii_sanitizer.py.

3.Run it

    python pii_sanitizer.py

4.Select a text or CSV file containing sensitive data, and the tool will create a sanitized version


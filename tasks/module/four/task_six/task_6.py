"""
The implementation of task 6 from module 4. Brute-Force PDF Password Breaker which uses given dictionary
"""
import PyPDF4

PDF_FILE = 'SecretFile.pdf'
POSSIBLE_PASSWORDS = 'dictionary.txt'

file_text = open(POSSIBLE_PASSWORDS, 'r').read()
list_of_possible_passwords = file_text.split()

pdfReader = PyPDF4.PdfFileReader(open(PDF_FILE, 'rb'))

print('The password is:')
for word in file_text.split():
    if pdfReader.decrypt(word.lower()) == 1:
        print(word.lower())
        break
    if pdfReader.decrypt(word) == 1:
        print(word)
        break

"""
  Implementation of task 7 from module four
  Code is responsible for converting xlsx files to csv
"""

import openpyxl

XLSX_FILE_NAME = 'spam'
XLSX_EXTENSION = '.xlsx'

wb = openpyxl.load_workbook(f'{XLSX_FILE_NAME}{XLSX_EXTENSION}')
list_of_sheets = wb.sheetnames

for sheetName in list_of_sheets:
    sheet = wb[sheetName]
    csv = open(f'{XLSX_FILE_NAME}_{sheet.title}.csv', "w+")

    for row in sheet.rows:
        for element in row:
            csv.write(element.value + ',')
        csv.write('\n')

csv.close()

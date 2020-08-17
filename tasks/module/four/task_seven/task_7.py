"""
  Implementation of task 7 from module four
  Code is responsible for converting xlsx files to csv
"""

import openpyxl
import csv

XLSX_FILE_NAME = 'spam'
XLSX_EXTENSION = '.xlsx'

wb = openpyxl.load_workbook(f'{XLSX_FILE_NAME}{XLSX_EXTENSION}')
list_of_sheets = wb.sheetnames

for sheetName in list_of_sheets:
    sheet = wb[sheetName]
    with open(f'{XLSX_FILE_NAME}_{sheet.title}.csv', mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        for row in sheet.rows:
            elements = []
            for element in row:
                elements.append(element.value)
            csv_writer.writerow(elements)

csvfile.close()

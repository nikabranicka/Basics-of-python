"""
  Implementation of task 5 from module four
  Code is responsible for finding invalid row where sum is not calculated correctly
"""
import ezsheets

MAX_NUMBER_OF_ROWS = 15001
HEADERS_ROW_INDEX = 0
SPREADSHEET_INDEX = 0

BEANS_PER_JAR_COLUMN_INDEX = 0
JARS_COLUMN_INDEX = 1
TOTAL_BEANS_COLUMN_INDEX = 2

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss.sheets[SPREADSHEET_INDEX]

for index, value in enumerate(sheet.getRows()):
    if index == HEADERS_ROW_INDEX:
        continue
    if index >= MAX_NUMBER_OF_ROWS:
        break

    if int(value[BEANS_PER_JAR_COLUMN_INDEX]) * int(value[JARS_COLUMN_INDEX]) != int(value[TOTAL_BEANS_COLUMN_INDEX]):
        print(f'row nr: {index} is not correct')

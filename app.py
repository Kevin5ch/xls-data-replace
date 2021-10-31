import os
from openpyxl import Workbook

dir_search = "./Archivos_vinculados"
string_match = ""
string_replace = ""
extensions = [".xls",".xlsx"]

for root, dirs, files in os.walk(dir_search, True):
  if files:
    for file in files:
      filename, file_extension = os.path.splitext(file)
      print(f"Path -> {root}: ")
      print(f"File: {file} con extension: {file_extension}")

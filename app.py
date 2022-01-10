import os
from openpyxl import load_workbook

dir_search = "./Archivos_vinculados"
string_match = ""
string_replace = ""
extensions = [".xls",".xlsx"]
files_procesed = 0


for root, dirs, files in os.walk(dir_search, True):
  if files:
    for file in files:
      filename, file_extension = os.path.splitext(file)
      if file_extension in extensions:
        book = load_workbook(os.path.join(root,file))
        for sheet in book:
          for row in sheet:
            for cell in row:
              if cell.value is not None:
                print(cell.value)
                print(cell.hyperlink)
          # print(f"Book -> {book.sheetnames}: ")
          # print(f"Path -> {root}: ")
          # print(f"File: {file} con extension: {file_extension}")

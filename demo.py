import openpyxl

f = openpyxl.load_workbook("E:\\0905\\demo1.xlsx")
s = f.active
cell = s.cell(row=10, column=10)
cell.value = "today"
f.save("E:\\0905\\demo1.xlsx")

import openpyxl
wb = openpyxl.load_workbook(r'C:\Users\48231\Desktop\pythonPratice\0814\huihui.xlsx')
# wb = openpyxl.workbook()
sheet = wb.worksheets[0]
# print(sheet['A1'].value)
l1 = []
l1.append(sheet['A1'].value)
print(l1)

# for row in sheet.rows():
for cell in sheet.rows:
    l2 = (cell.coordinate,cell.value)
    print(l2)

# for cols in sheet.iter_cols(0):
#     for cell in cols:
#         l3 = (cell.coordinate,cell.value)
#         print(l3)
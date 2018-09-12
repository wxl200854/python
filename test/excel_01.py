import xlrd
data = xlrd.open_workbook('excel.xls')
table = data.sheets()[0]

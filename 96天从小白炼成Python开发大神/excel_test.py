import xlrd

xlsx = xlrd.open_workbook('E:/桌面备份-20201209/附件-2021年天翼云池资源需求收集-20201021.xlsx')
table = xlsx.sheet_by_index(0)

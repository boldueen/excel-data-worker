import openpyxl


def make_report(file):
    wb = openpyxl.load_workbook(filename=file)
    sheet = wb.active

    val = sheet['A2'].value

    return val

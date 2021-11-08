import io

from openpyxl import Workbook


def make_daily_xl(data):
    bytes = io.BytesIO()
    wb = Workbook()

    # Edit your presentation here

    wb.save(bytes)
    bytes.seek(0)
    return bytes
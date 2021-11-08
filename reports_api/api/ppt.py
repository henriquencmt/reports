import io

from pptx import Presentation


def make_monthly_ppt(data):
    bytes = io.BytesIO()
    prs = Presentation()

    # Edit your presentation here

    prs.save(bytes)
    bytes.seek(0)
    return bytes


def make_daily_ppt(data):
    bytes = io.BytesIO()
    prs = Presentation()

    # Edit your presentation here

    prs.save(bytes)
    bytes.seek(0)
    return bytes
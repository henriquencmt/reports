import json

from flask import Flask, request, send_file, abort
from flask_cors import CORS

import db
import ppt
import xl


app = Flask(__name__)
CORS(app)


def get_current_user():
    return 1


def download_report(file, report, data, filetype):
    try:
        return send_file(
            path_or_file=file,
            as_attachment=True,
            download_name=f"{report}_{data['reference_year']}-{data['reference_month']}.{filetype}"
        )
    except FileNotFoundError:
        abort(404)


@app.route("/report/<report>/")
def report_api(report):
    id = request.args.get('id', None)
    if id:
        response = db.read_report(report, id)
        return json.dumps(response)

    response = db.read_all_reports(report)
    return json.dumps(response)


@app.route("/file/<report>/<filetype>/<id>/")
def file_api(report, filetype, id):
    try:
        data = db.read_report(report, id)
        if data:
            if filetype == 'xlsm':
                file_bytes = xl.make_daily_xl(data)
                return download_report(file_bytes, report, data, filetype)
            if filetype == 'pptx' and report == 'daily':
                file_bytes = ppt.make_daily_ppt(data)
                return download_report(file_bytes, report, data, filetype)
            if filetype == 'pptx' and report == 'monthly':
                file_bytes = ppt.make_monthly_ppt(data)
                return download_report(file_bytes, report, data, filetype)
            abort(404)
    except:
        raise

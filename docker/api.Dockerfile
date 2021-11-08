FROM python

COPY ./reports_api/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /reports_api

COPY ./reports_api/api .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]

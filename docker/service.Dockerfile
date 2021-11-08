FROM python

COPY ./reports_service/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /reports_service

COPY ./reports_service/service .

CMD [ "python3", "daemon.py" ]

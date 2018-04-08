FROM python:3.6.5

ADD . /

RUN pip install -e .

CMD [ "python", "bin/fetch_forecasts.py" ]


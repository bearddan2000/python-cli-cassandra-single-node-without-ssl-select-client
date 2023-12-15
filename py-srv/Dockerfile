# We downgraded python from latest to 3.8 to get
# cassandra drives to work. The alpine version is missing
# some system dependcies for pandas so we use bullseye.
 
FROM python:3.8-bullseye

WORKDIR /code

COPY bin/ .

RUN pip install -r requirements.txt

ENV WAIT_VERSION 2.7.2

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait

RUN chmod +x /wait

CMD ["python", "app.py"]

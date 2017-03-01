FROM python:3.5.3

RUN mkdir /app

WORKDIR /app

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD . .

CMD ["/bin/bash"]

FROM python:3

WORKDIR /hankey-pub-sub

COPY [".", "/hankey-pub-sub"]

RUN #!/bin/bash python3 -m venv env
RUN #!/bin/bash source env/bin/activate
RUN #!/bin/bash python3 -m pip install --upgrade pip
RUN #!/bin/bash python3 -m pip install -r requirements.txt




EXPOSE 3000

CMD ["python3", "PubSub/manage.py", "runserver","0.0.0.0:8000"]




FROM python:3.9
COPY  ./app ./

ENTRYPOINT ["python", "./app", -p]
FROM python:3.9
WORKDIR /
COPY  ./app /
CMD [ "./app" ]
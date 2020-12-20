FROM python:3

RUN pip3 install psutil
WORKDIR /usr/src/app
COPY . .
CMD ["metrics"]
ENTRYPOINT ["python3"]

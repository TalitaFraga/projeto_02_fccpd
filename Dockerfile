FROM python:3.9
WORKDIR /app
COPY app /app
RUN pip install flask mysql-connector-python
CMD ["flask", "run", "--host=0.0.0.0"]
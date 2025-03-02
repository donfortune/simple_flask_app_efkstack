FROM python:3.10.11 //base image
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 5001
CMD ["python3", "app.py"]

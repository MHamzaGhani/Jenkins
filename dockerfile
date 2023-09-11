FROM python:3.8doc
COPY . /opt/app
WORKDIR /opt/app
RUN apt-get update
RUN apt-get install -y python3-pip 
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

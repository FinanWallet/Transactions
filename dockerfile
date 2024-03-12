FROM python:3.11.5
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
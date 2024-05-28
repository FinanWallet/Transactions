FROM python:3.9-alpine

WORKDIR /app

# 
COPY requirements.txt ./
# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY . .


EXPOSE 7002

# 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7002", "--reload"]

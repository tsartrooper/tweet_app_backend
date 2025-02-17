FROM python:3.11.8
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install pip install -r requirements.txt
COPY . .
CMD ["flask","run","--host","0.0.0.0"]
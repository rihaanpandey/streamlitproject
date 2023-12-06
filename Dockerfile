FROM python:3.8

WORKDIR /streamlit

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["streamlit", "run", "--server.port", "8000", "index.py"]

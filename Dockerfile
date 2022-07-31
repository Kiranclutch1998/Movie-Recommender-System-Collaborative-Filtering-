FROM python:3.7.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
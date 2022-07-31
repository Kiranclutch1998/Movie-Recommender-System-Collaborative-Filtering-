FROM python:3.7.10
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD streamlit run app.py
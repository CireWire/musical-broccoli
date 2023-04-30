FROM python:3
COPY . /app
WORKDIR /app
RUN pip install pandas numpy scikit-learn
CMD ["python", "predict.py"]

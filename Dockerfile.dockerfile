FROM python:3.9-slim

COPY app/ /app

EXPOSE 5000

WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["bills_app.py"]
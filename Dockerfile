FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENTRYPOINT ["bash"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]

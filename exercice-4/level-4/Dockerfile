FROM python:3.12
WORKDIR /usr/local/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY model_2025-05-28_10-54_valacc0.8134.keras .
COPY server.py .
CMD ["fastapi", "run", "server.py", "--port", "5042"]

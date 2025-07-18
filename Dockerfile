FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y pandoc && pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "gui_app_main.py", "--server.port=8501", "--server.address=0.0.0.0"]

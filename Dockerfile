FROM mcr.microsoft.com/quantum/iqsharp-base:latest
WORKDIR . /app
COPY . /app
RUN pip install -r /app/requirements.txt
CMD ["streamlit run /app/qrng_final.py", "run"]

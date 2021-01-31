FROM mcr.microsoft.com/quantum/iqsharp-base:latest
WORKDIR . /app
COPY . /app

# Add 3.7 to the available alternatives
RUN /usr/bin/sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

# Set python3.7 as the default python
RUN /usr/bin/sudo update-alternatives --set python /usr/bin/python3.7

RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit run /app/qrng_final.py", "run"]

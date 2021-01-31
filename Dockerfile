FROM python:3.7-alpine
WORKDIR . /app
COPY . /app
RUN pip install -r requirements.txt
RUN apt update -y && apt dotnet tool install -g Microsoft.Quantum.IQSharp
RUN dotnet iqsharp install
EXPOSE 8501
CMD ["streamlit run app/qrng_final.py", "run"]
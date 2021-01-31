dotnet tool install -g dotnet-format

dotnet tool install -g Microsoft.Quantum.IQSharp

dotnet iqsharp install


mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml


echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

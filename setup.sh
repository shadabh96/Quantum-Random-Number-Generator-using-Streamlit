mkdir -p ~/.streamlit/

dotnet tool install -g Microsoft.Quantum.IQSharp
dotnet iqsharp install


/path/to/dotnet-iqsharp install --user --path-to-tool="/path/to/dotnet-iqsharp"


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
sudo add-apt-repository universe
sudo apt-get install apt-transport-https
sudo apt-get update

export PATH="$PATH:$HOME/.dotnet"

dotnet tool update -g Microsoft.Quantum.IQSharp
dotnet iqsharp install

dotnet iqsharp --version

pip install qsharp --upgrade

python -c "import qsharp; qsharp.reload()"

%workspace reload

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

wget https://packages.microsoft.com/config/ubuntu/20.10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb

sudo apt-get update; \
  sudo apt-get install -y apt-transport-https && \
  sudo apt-get update && \
  sudo apt-get install -y dotnet-sdk-5.0
  
sudo apt-get update; \
  sudo apt-get install -y apt-transport-https && \
  sudo apt-get update && \
  sudo apt-get install -y aspnetcore-runtime-5.0
  
sudo apt-get install -y dotnet-runtime-5.0

export PATH="$PATH:$HOME/.dotnet"

dotnet tool install --global Microsoft.Quantum.IQSharp --version 0.15.2101126940
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

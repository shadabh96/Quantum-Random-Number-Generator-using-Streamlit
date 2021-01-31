mkdir -p ~/.streamlit/

conda create -n qsharp-env -c quantum-engineering qsharp notebook

conda activate qsharp-env

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
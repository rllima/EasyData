mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"rlo@cin.ufpe.br\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
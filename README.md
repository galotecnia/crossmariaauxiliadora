Web del Cross María Auxiliadora en pelican
==========================================

### Instalacion

    git clone --recursive https://github.com/galotecnia/crossmariaauxiliadora.git
    cd crossmariaauxiliadora
    virtualenv virtualenv
    . virtualenv/bin/activate
    pip install -r requirements.txt
    ./develop_server.sh start # o bien "pelican content" para generar el html
    # visitar http://localhost:8000/


FROM python:3-alpine
# Toma como base un linux de alpine con python3

RUN apk add --no-cache git
# Instala git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-v-perassiferrara.git 
# clona mi repositorio

WORKDIR /ajedrez-2024-v-perassiferrara
# setea carpeta de trabajo

RUN pip install -r requirements.txt
# instala dependencias y requirements

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python -m juego.interfaz"]


# comandos para ejecutar el programa en una imagen de docker
    # docker buildx build --no-cache -t ajedrez_vpf .
    # docker run -i ajedrez_vpf

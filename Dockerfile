#Obtenermos la imagen base
FROM python:3.12.2-slim-bullseye

#Seteamos las variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Seteamos el directorio de trabajo
WORKDIR /code

#Instalamos las dependencias 
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copiamos el projecto 
COPY . . 
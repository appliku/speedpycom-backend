FROM python:3.10.10-bullseye
SHELL ["/bin/bash", "--login", "-c"]
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 0
ENV COLUMNS 80
RUN apt-get update \
 && apt-get install -y --force-yes \
 curl nano python3-pip gettext chrpath libssl-dev libxft-dev \
 libfreetype6 libfreetype6-dev  libfontconfig1 libfontconfig1-dev\
  && rm -rf /var/lib/apt/lists/*
WORKDIR /code/
COPY requirements.txt /code/
COPY requirements-dev.txt /code/
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
COPY . /code/
#RUN useradd -ms /bin/bash code
#USER code

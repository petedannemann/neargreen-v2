FROM ubuntu:16.04

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

WORKDIR /usr/src/app

COPY requirements.txt .

RUN set -ex \
    && buildDeps=' \
    python3-dev \
    build-essential \
    ' \
    && apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
    $buildDeps \
    python3 \
    python3-pip \
    netcat \
    libgdal-dev \
    libgeos-dev \
    binutils \
    libproj-dev \
    gdal-bin \
    libspatialindex-dev \
    libpq-dev \
    && python3 -m pip install -U pip \
    && pip3 install -U setuptools \
    && pip3 install -r requirements.txt \
    && apt-get remove --purge -yqq $buildDeps \
    && apt-get clean 

COPY backend ./backend
COPY manage.py .
COPY Healthy_Corner_Stores.geojson .
COPY scripts/entrypoint.sh .

RUN chmod +x ./entrypoint.sh \
    && chmod +x ./manage.py \
    && chmod +x ./backend/*.py 

ENTRYPOINT ["./entrypoint.sh"]

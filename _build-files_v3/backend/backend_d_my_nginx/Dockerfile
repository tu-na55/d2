# FROM python:3.8
FROM python:3.8-alpine
# FROM ubuntu:20.04
# SHELL ["/bin/bash", "-c"]
####################
#Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
#Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1
# ENV DEBIAN_FRONTEND=noninteractive
####################
# alpine: use apk
RUN apk update && apk upgrade \
 && apk add --no-cache linux-headers \
 && apk add --no-cache mariadb-dev build-base
####################
# RUN apt-get update && apt-get install -y \
    # && apt-get install -y --no-install-recommends \
    # && apt-get upgrade -y \
    # build-essential \
    # ca-certificates \

    # git \
    # && apt-get clean && \
    # rm -rf /var/lib/apt/lists/*

    # && apt-get -y install vim

    # && apt-get install -y python3.8 python3.8-dev \
    # && source ~/.bashrc \
####################
    # libblas-dev \
    # liblapack-dev\
    # libatlas-base-dev \
    # libsm6 \
    # libxext6 \
    # libxrender-dev
####################

RUN mkdir /app
WORKDIR /app
# WORKDIR /usr/src/app
####################
# 17 deploy
# RUN addgroup -g 1000 django \
#  && adduser -S -u 1000 django -G django
# RUN echo "export SECRET_KEY=\"\$(cat /dev/urandom | tr -dc 'a-zA-Z0-9%&@+\-*/=^~|' | fold -w 80 | head -n 1)\"" >> ~django/.profile
####################
# COPY requirements.txt .
# COPY requirements.txt /code/
# ADD requirements.txt /code/

RUN pip install --upgrade pip
#  && pip install --no-cache-dir -r requirements.txt
####################
# RUN apt-get install -y curl \
#     && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
#     && apt-get install -y python3.8-distutils \
#     && python3.8 get-pip.py \
#     && pip install -U pip \
#     && apt-get install -y build-essential libssl-dev libffi-dev python-dev python3-dev libpq-dev
####################
RUN pip install pipenv
# RUN pipenv install --dev
# CMD ["pipenv", "run" ,"./teamfinder/manage.py", "migrate"]

# ローカルマシンののPipfileをコンテナにコピー
COPY Pipfile ./
# COPY ./Pipfile /usr/src/app/Pipfile

# Pipfile.lockを無視してPipfileに記載のパッケージをシステムにインストール
# その後、pipenvをアンインストール
RUN pipenv install --system --skip-lock
RUN pip uninstall -y pipenv virtualenv-clone virtualenv

# pipfileからパッケージをインストールしてDjango環境を構築
# RUN pipenv install --skip-lock --system --dev
####################
# 地理空間ライブラリをインストールする際の依存関係
# RUN apt-get update -y \
#     && apt-get upgrade -y \
#     && apt-get install -y libgeos-dev binutils libproj-dev gdal-bin libgdal-dev \
#     && apt-get install -y python3-gdal

# RUN apt-get install -y netcat \
#     && apt-get install -y expect

####################
# activate
# RUN echo "if [[ -z \"\${VIRTUAL_ENV}\" ]]; then" >> /root/.bashrc && \
#     echo "source \$(pipenv --venv)/bin/activate" >> /root/.bashrc && \
#     echo "fi"                                    >> /root/.bashrc
####################
#17 deploy
# COPY django/ /app/
# COPY backend/ /code/

# RUN django-admin compilemessages

# COPY entrypoint.sh /usr/local/bin/
# Sentryに登録されたリリース内容
# ADD https://github.com/getsentry/sentry-cli/releases/latest/download/sentry-cli-Linux-x86_64 /usr/local/bin/sentry-cli
# RUN chmod 755 /usr/local/bin/sentry-cli /usr/local/bin/entrypoint.sh

# USER django

# EXPOSE 3031
# ENTRYPOINT [ "entrypoint.sh" ]
# CMD [ "webapp" ]
####################
# シェルスクリプトをコピー
# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY ./entrypoint_env.sh /app/entrypoint_env.sh

# COPY . /usr/src/app/
COPY . /app/

# シェルスクリプトを実行
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint_env.sh"]
####################
# ADD . /code/
# 02
# COPY . /code/

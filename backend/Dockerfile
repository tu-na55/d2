# FROM python:3.8
FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

####################
# alpine: use apk
RUN apk update && apk upgrade \
 && apk add --no-cache linux-headers \
 && apk add --no-cache mariadb-dev build-base
####################

# RUN apt-get update && apt-get install -y
    # libblas-dev \
    # liblapack-dev\
    # libatlas-base-dev \
    # libsm6 \
    # libxext6 \
    # libxrender-dev
####################

RUN mkdir /code
WORKDIR /code

####################
# 17 deploy
# RUN addgroup -g 1000 django \
#  && adduser -S -u 1000 django -G django
# RUN echo "export SECRET_KEY=\"\$(cat /dev/urandom | tr -dc 'a-zA-Z0-9%&@+\-*/=^~|' | fold -w 80 | head -n 1)\"" >> ~django/.profile

# COPY requirements.txt .
COPY requirements.txt /code/
# ADD requirements.txt /code/

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

####################
# 01 pipenv
# RUN pip install pipenv
# RUN pipenv install --dev
# CMD ["pipenv", "run" ,"./teamfinder/manage.py", "migrate"]
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
ADD . /code/
# 02
# COPY . /code/

FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
####################
# 01
# RUN apt-get update && apt-get install -y mysql-client
# 03
RUN apt-get update && apt-get install -y \
    # libblas-dev \
    # liblapack-dev\
    # libatlas-base-dev \
    # libsm6 \
    # libxext6 \
    # libxrender-dev
####################
RUN pip install --upgrade pip
# 01
# RUN pip install pipenv
# RUN pipenv install --dev
# CMD ["pipenv", "run" ,"./teamfinder/manage.py", "migrate"]

####################
COPY requirements.txt /code/
ADD requirements.txt /code/

# RUN pip install --upgrade pip

# RUN pip3 install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


####################
ADD . /code/
# 02
# COPY . /code/

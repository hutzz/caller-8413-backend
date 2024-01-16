FROM tensorflow/tensorflow:2.10.1-gpu 

WORKDIR /caller8413backend

COPY . /caller8413backend/

RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m pip install mysql-connector

EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]

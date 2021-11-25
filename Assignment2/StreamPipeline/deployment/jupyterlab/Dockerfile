FROM bitnami/jupyterhub:1.4.2
USER root
RUN apt-get update -y && \
    apt-get -y install openjdk-11-jdk

RUN apt-get install npm -y && \
    npm install -g configurable-http-proxy
USER 1001
RUN pip3 install --upgrade pip && \
    pip3 install pyspark==3.1.2
ENV PATH="/usr/lib/jvm/java-11-openjdk-amd64:$PATH"
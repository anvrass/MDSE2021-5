FROM bitnami/python:3.9.0 as build

FROM bitnami/spark:3.1.1

COPY --from=build /opt/bitnami/python/ /opt/bitnami/python/
# Update the guava library needed by gcs connector
RUN mv /opt/bitnami/spark/jars/guava-14.0.1.jar /opt/bitnami/spark/jars/guava-14.0.1.jar.bk
COPY *.jar /opt/bitnami/spark/jars/
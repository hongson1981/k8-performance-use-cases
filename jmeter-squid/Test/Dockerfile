# Use a minimal base image with OpenJDK installed
FROM openjdk:8-jre

# Install packages
RUN apt-get update && \
    apt-get -y install python-pip && \
    pip install awscli && \
    apt-get -y install python3.7 && \
    apt-get -y install python3-pip && \
    pip3 install boto3

# Set variables
ENV JMETER_HOME=/usr/share/apache-jmeter \
    JMETER_VERSION=5.3 \
    JMETER_BIN=${JMETER_HOME}/bin \
    PATH=$PATH:$JMETER_BIN \
    JVM_ARGS="-Xms2048m -Xmx4096m -XX:NewSize=1024m -XX:MaxNewSize=2048m -Duser.timezone=UTC"

WORKDIR ${JMETER_HOME}

# Install Apache JMeter
RUN wget http://archive.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz && \
    tar zxvf apache-jmeter-${JMETER_VERSION}.tgz && \
    rm -f apache-jmeter-${JMETER_VERSION}.tgz && \
    mv apache-jmeter-${JMETER_VERSION} ${JMETER_HOME}
FROM maven:3.8.5-openjdk-17 as build

WORKDIR /app

COPY ./deploy/ImageApp .

# Package the application
RUN mvn clean package -DskipTests

# Use Tomcat image for runtime
FROM tomcat:11.0-jdk17

RUN useradd -m -d /usr/local/tomcat -s /bin/bash tomcat
RUN chown -R tomcat:tomcat /usr/local/tomcat

RUN apt update -y && apt upgrade -y && \
    apt install -y gcc

COPY ./deploy/check.sh /tmp
RUN chown tomcat:tomcat /tmp/check.sh && \
    chmod 555 /tmp/check.sh

## Add FLAG
COPY ./deploy/flag.c /flag.c
RUN gcc /flag.c -o /flag \
    && chmod 111 /flag && rm /flag.c

RUN rm -rf /usr/local/tomcat/webapps/*

USER tomcat

# Copy the packaged WAR file from the build stage
COPY --from=build /app/target/*.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080

CMD ["catalina.sh", "run"]

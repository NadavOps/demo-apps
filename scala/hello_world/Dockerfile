FROM openjdk:17-jdk-alpine3.14 AS builder

ENV SCALA_VERSION=2.13.10 \
    SCALA_HOME=/usr/share/scala

RUN apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \
    apk add --no-cache bash curl jq && \
    cd "/tmp" && \
    wget --no-verbose "https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz" && \
    tar xzf "scala-${SCALA_VERSION}.tgz" && \
    mkdir "${SCALA_HOME}" && \
    rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat && \
    mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib" "${SCALA_HOME}" && \
    ln -s "${SCALA_HOME}/bin/"* "/usr/bin/" && \
    apk del .build-dependencies && \
    rm -rf "/tmp/"*

WORKDIR /
COPY . .
RUN scalac Hello.scala -d Hello.jar

FROM openjdk:17-jdk-alpine3.14 AS runner

WORKDIR /scala_app

COPY --from=builder /usr/share/scala/lib/scala-library.jar scala-library.jar
COPY --from=builder /Hello.jar Hello.jar

USER 5001

CMD ["java", "-cp", "scala-library.jar:Hello.jar", "Hello"]

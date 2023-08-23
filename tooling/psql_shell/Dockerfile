FROM postgres:latest

RUN apt-get update -y && \
    apt-get install -y postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PGHOST=localhost
ENV PGPORT=5432
ENV PGUSER=myuser
ENV PGPASSWORD=mypassword
ENV PGDATABASE=""

CMD ["pg_isready"]

# had some issues to do it in the container, from the container while it sleeped it worked
# password is only exported not supplied at command
#  -d $PGDATABASE
# -c 'command'
# CMD ["psql", "-h", "$PGHOST", "-p", "$PGPORT", "-U", "$PGUSER", "-l"]

FROM ubuntu:18.10

RUN apt update && apt install -y python3 \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r analysis && useradd -m --no-log-init --gid analysis analysis

USER analysis
COPY src /analyzer

WORKDIR /
CMD ["/analyzer/analyze.sh"]

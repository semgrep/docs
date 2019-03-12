FROM ubuntu:17.10

RUN apt update && apt install -y jq gawk bc

RUN groupadd -r analysis && useradd --no-log-init --system --gid analysis analysis
USER analysis

COPY --chown=analysis:analysis src /analyzer
WORKDIR /
CMD ["/analyzer/analyze.sh"]
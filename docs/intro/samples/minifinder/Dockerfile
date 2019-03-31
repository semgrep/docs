FROM ubuntu:17.10

RUN apt update && apt install -y python3

ARG UNAME
ARG UID
ARG GID

RUN groupadd -o $UNAME -g $GID
RUN useradd -m -u $UID -g $GID -o $UNAME
USER $UNAME
COPY src /analyzer

WORKDIR /
CMD ["/analyzer/analyze.sh"]

FROM blang/latex:ubuntu

RUN apt-get update && apt-get install -y python3-sphinx
RUN apt-get update && apt-get install -y texlive-latex-extra
COPY . /makeme

RUN cd /makeme && ls -al && make html && make latexpdf

RUN echo "output PDF in: /makeme/_build/latex/r2c.pdf"

CMD ["bash"]
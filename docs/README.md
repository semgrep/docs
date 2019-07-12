## building documentation

    git submodule update --init
    make clean && make html

## building documentation as a PDF

    docker build Dockerfile -t sphinx-pdf
    docker run sphinx-df

find the container id of the running container from the previous step:

    docker cp <container_id>:/makeme/_build/latex/r2c.pdf r2c.pdf

#!/bin/bash
docker build -t complice-notebook .
docker run -p 8888:8888 -v "$(pwd):/home/jovyan/work" complice-notebook

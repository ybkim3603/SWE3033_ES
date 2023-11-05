#!/bin/bash

# change permission of notebooks
chmod -R 777 notebooks

# change permission of certs at swe3003_es-jupyter-1
docker exec -it --user root swe3003_es-jupyter-1 /bin/bash -c "chmod -R 777 certs"

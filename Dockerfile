FROM pycaret/full

#USER root
#
#RUN apt-get update && apt-get install -y swig curl
#
#RUN curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip install --default-timeout=100
#
#RUN pip install --default-timeout=100 auto-sklearn
#
#USER $NB_UID

#docker pull alfranz/automl
#docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work automl:v1
FROM jupyter/minimal-notebook:notebook-6.5.2

COPY ./jupyter_notebook_config.py /etc/jupyter/
# Install the libraries specified in the requirements.txt
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
RUN rm requirements.txt

RUN jupyter serverextension enable nbgitpuller --sys-prefix

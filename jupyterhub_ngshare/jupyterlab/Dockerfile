FROM jupyter/minimal-notebook:notebook-6.5.2

COPY ./jupyter_notebook_config.py /etc/jupyter/
COPY ./nbgrader_config.py /etc/jupyter/

# Install the libraries specified in the requirements.txt
COPY ./requirements.txt .

RUN pip install -r ./requirements.txt
# jupyter nbextension install --symlink --sys-prefix --py nbgrader && \
# jupyter nbextension enable --sys-prefix --py nbgrader && \
# jupyter serverextension enable --sys-prefix --py nbgrader

RUN rm requirements.txt

#RUN jupyter serverextension enable nbgitpuller --sys-prefix

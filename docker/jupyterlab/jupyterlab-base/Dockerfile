FROM jupyter/minimal-notebook:notebook-6.5.2

# Install the libraries specified in the requirements.txt
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt --no-cache-dir &&\
  rm requirements.txt

# Enable extensions
RUN jupyter nbextension install --symlink --sys-prefix --py nbgrader && \
  jupyter nbextension enable --sys-prefix --py nbgrader && \
  jupyter serverextension enable --sys-prefix --py nbgrader &&\
  jupyter serverextension enable nbgitpuller --sys-prefix

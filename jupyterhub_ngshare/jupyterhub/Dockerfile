FROM jupyterhub/jupyterhub:3

RUN pip install --no-cache-dir \
    dockerspawner==12.1.0 \
    jupyterhub-idle-culler==1.2.1 \
    psycopg2-binary==2.9.5 \
    jupyterhub-jwtauthenticator-v2==2.0.3 \
    nbgrader \
    ngshare

COPY ./jupyterhub_config.py .

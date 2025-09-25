# Image de base avec JupyterLab et Python
FROM jupyter/scipy-notebook

# Installation des dépendances
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Dossier de travail par défaut (JupyterLab pointe ici)
WORKDIR /home/jovyan/work

# Pas besoin de COPY . ici, car tu montes ton dossier local


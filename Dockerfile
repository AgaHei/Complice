# Image de base avec JupyterLab et Python
FROM jupyter/scipy-notebook:latest

# Passer en utilisateur root pour les installations système
USER root

# Installation des dépendances système si nécessaire (ajoute ici si tu en as besoin)
# RUN apt-get update && apt-get install -y \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# Revenir à l'utilisateur jovyan
USER jovyan

# Copier et installer les requirements Python
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Installer des extensions JupyterLab utiles pour le dev (optionnel)
RUN pip install --no-cache-dir \
    jupyterlab-git \
    jupyterlab_widgets \
    ipywidgets

# Créer le dossier de travail
WORKDIR /home/jovyan/work

# Port pour JupyterLab et Streamlit
EXPOSE 8888 8501

# Commande par défaut - JupyterLab avec auto-reload et sans authentification pour le dev
CMD ["start.sh", "jupyter", "lab", "--LabApp.token=''", "--LabApp.password=''", "--LabApp.allow_root=True", "--LabApp.ip='0.0.0.0'"]
#from local
#   git add .
#   git commit -m "timecode"
#   git push

#from server
#   git pull --force
#   reload app


import subprocess
from datetime import datetime


def deploy():
    # Chemin local vers votre projet Bottle
    projet_path = "/home/olinger/PycharmProjects/pythonAnyWhere"

    # Message de commit avec le timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Déploiement automatique - {timestamp}"

    # Commandes Git pour ajouter, commettre et pousser les modifications
    subprocess.run(["git", "add", "."], cwd=projet_path)
    subprocess.run(["git", "commit", "-m", commit_message], cwd=projet_path)
    subprocess.run(["git", "push"], cwd=projet_path)

    # # Connexion SSH à PythonAnywhere et rechargement de l'application
    # subprocess.run(["ssh", "CharlyOlinger@pythonanywhere.com", "git", "pull", "--force"], cwd=projet_path)
    # subprocess.run(["ssh", "CharlyOlinger@pythonanywhere.com", "reload-web-app"], cwd=projet_path)

if __name__ == "__main__":
    deploy()

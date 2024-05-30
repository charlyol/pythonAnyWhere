
import subprocess
import requests
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

    # # Informations d'authentification
    # username = 'CharlyOlinger'
    # api_token = '6c662ac265f1f9a47fa07f027bc52313e809e636'
    #
    # # Endpoints de l'API PythonAnywhere
    # git_pull_url = f"https://www.pythonanywhere.com/api/v0/user/{username}/gitpull/"
    # reload_app_url = f"https://www.pythonanywhere.com/api/v0/user/{username}/webapps/CharlyOlinger.pythonanywhere.com/reload/"
    #
    # # En-têtes de requête avec l'authentification
    # headers = {
    #     "Authorization": f"Token {api_token}"
    # }
    #
    # # Effectuer une requête POST pour mettre à jour le dépôt Git
    # git_pull_response = requests.post(git_pull_url, headers=headers)
    #
    # # Effectuer une requête POST pour recharger l'application
    # reload_app_response = requests.post(reload_app_url, headers=headers)
    #
    # # Vérifier les réponses
    # if git_pull_response.status_code == 200:
    #     print("Dépôt Git mis à jour avec succès")
    # else:
    #     print(f"Échec de la mise à jour du dépôt Git : {git_pull_response.text}")
    #
    # if reload_app_response.status_code == 200:
    #     print("Application rechargée avec succès")
    # else:
    #     print(f"Échec du rechargement de l'application : {reload_app_response.text}")

if __name__ == "__main__":
    deploy()

import subprocess
import requests
from datetime import datetime


def deploy():
    deployOnGit()
    git_pull_response, headers, reload_app_url = deployOnAnyWhere()

    # Vérifier les réponses
    if git_pull_response.status_code == 200:
        print("Dépôt Git mis à jour avec succès")
        reload_app_response = deployReload(headers, reload_app_url)
        if reload_app_response.status_code == 200:
            print("Application rechargée avec succès")
        else:
            print(f"Échec du rechargement de l'application : {reload_app_response.text}")
    else:
        print(f"Échec de la mise à jour du dépôt Git : {git_pull_response.text}")


def deployReload(headers, reload_app_url):
    # Effectuer une requête POST pour recharger l'application
    reload_app_response = requests.post(reload_app_url, headers=headers)
    return reload_app_response


def deployOnAnyWhere():
    # Informations d'authentification
    username = 'CharlyOlinger'
    api_token = '6c662ac265f1f9a47fa07f027bc52313e809e636'
    id = 34020282
    # Endpoints de l'API PythonAnywhere
    git_pull_url = f"https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/"
    reload_app_url = f"https://www.pythonanywhere.com/api/v0/user/{username}/webapps/CharlyOlinger.pythonanywhere.com/reload/"
    # En-têtes de requête avec l'authentification
    headers = {
        "Authorization": f"Token {api_token}"
    }
    # Corps de la requête avec la commande
    payload = {
        "input": "git pull\ntouch /var/www/CharlyOlinger_pythonanywhere_com_wsgi.py\n"
    }
    # Effectuer une requête POST pour mettre à jour le dépôt Git
    git_pull_response = requests.post(git_pull_url, headers=headers, data=payload)
    return git_pull_response, headers, reload_app_url


def deployOnGit():
    # Chemin local vers votre projet Bottle
    projet_path = "/home/olinger/PycharmProjects/pythonAnyWhere"

    # Message de commit avec le timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Déploiement automatique - {timestamp}"

    # Commandes Git pour ajouter, commettre et pousser les modifications
    subprocess.run(["git", "add", "."], cwd=projet_path)
    subprocess.run(["git", "commit", "-m", commit_message], cwd=projet_path)
    subprocess.run(["git", "push"], cwd=projet_path)


if __name__ == "__main__":
    deploy()

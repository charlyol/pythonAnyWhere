import os
import subprocess
import requests
from datetime import datetime
import time
from dotenv import load_dotenv

load_dotenv()

def deploy():
    # Deploy changes to local Git repository
    deployOnGit()
    deployChangeOnPythonAnyWhere()


def deployChangeOnPythonAnyWhere():
    # Deploy changes to PythonAnywhere
    git_pull_response, headers, reload_app_url = deployOnAnyWhere()
    # Check responses
    if git_pull_response.status_code == 200:
        # Git repository updated successfully
        print("Git repository updated successfully")

        # Wait for Git to finish updating (adjust delay as needed)
        time.sleep(10)  # Wait for 10 seconds

        # Reload the application
        reload_app_response = deployReload(headers, reload_app_url)
        if reload_app_response.status_code == 200:
            # Application reloaded successfully
            print("Application reloaded successfully")
        else:
            # Reload application failed
            print(f"Failed to reload the application: {reload_app_response.text}")
    else:
        # Failed to update Git repository
        print(f"Failed to update Git repository: {git_pull_response.text}")


def deployReload(headers, reload_app_url):
    # Reload the application on PythonAnywhere
    reload_app_response = requests.post(reload_app_url, headers=headers)
    return reload_app_response


def deployOnAnyWhere():
    # Authentication information
    username = os.environ.get('USER_GIT')
    print(username)
    api_token = '6c662ac265f1f9a47fa07f027bc52313e809e636'
    id = 34020282
    # PythonAnywhere API endpoints
    git_pull_url = f"https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/"
    reload_app_url = f"https://www.pythonanywhere.com/api/v0/user/{username}/webapps/CharlyOlinger.pythonanywhere.com/reload/"
    # Request headers with authentication
    headers = {
        "Authorization": f"Token {api_token}"
    }
    # Request body with command
    payload = {
        "input": "git pull\ntouch /var/www/CharlyOlinger_pythonanywhere_com_wsgi.py\n"
    }
    # Send POST request to update Git repository
    git_pull_response = requests.post(git_pull_url, headers=headers, data=payload)
    return git_pull_response, headers, reload_app_url


def deployOnGit():
    # Local path to your Bottle project
    projet_path = "/home/olinger/PycharmProjects/pythonAnyWhere"

    # Commit message with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Automatic deployment - {timestamp}"

    # Git commands to add, commit, and push changes
    subprocess.run(["git", "add", "."], cwd=projet_path)
    subprocess.run(["git", "commit", "-m", commit_message], cwd=projet_path)
    subprocess.run(["git", "push"], cwd=projet_path)


if __name__ == "__main__":
    deploy()

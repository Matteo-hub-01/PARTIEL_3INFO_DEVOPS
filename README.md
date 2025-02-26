# Partiel DEVOPS - Exemple avec Python et GitHub Actions

Ce dépôt contient un projet Python simple avec :

- Des fonctions simples
- Des tests unitaires pour valider le comportement de la fonction.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/<votre-organisation>/<votre-repo>.git
   cd <votre-repo>

2. Installez les dépendances :
```pip install -r requirements.txt```

3. Exécutez les tests localement :
```pytest```

4. Ajouter un .gitignore pour ne pas commit __pycache__ et autre dossiers non pertinents à commit 

4. Creez un github workflow pour éxécuter des tests et  un github workflow pour éxécuter le linter 

5. Ajouter des badges de réussite d'execution de vos tests et de votre linter dans le readme (voir ***GITHUB_BADGES_GUIDE.md***)

6. Améliorer le code pour réussir le linter

7. Rendre le lien de votre répository contenant les github actions que vous aurez implémenté. 

***Attention à bien mettre votre repository en PUBLIC !***


## Test Results


![Test Status](https://img.shields.io/github/workflow/status/Matteo-hub-01/PARTIEL_3INFO_DEVOPS/Run%20Tests)
![Linter Status](https://img.shields.io/github/workflow/status/Matteo-hub-01/PARTIEL_3INFO_DEVOPS/Run%20Linter)


## Available Badges

* **License** ![License](https://img.shields.io/badge/license-MIT-green) - Github license (`gh_license`)
* **Version** ![Version](https://img.shields.io/badge/version-v1.1.0-blue) - Package.json version (`gh_version`)
* **Stars** ![Stars](https://img.shields.io/badge/stars-3-blue) - Stars (`gh_stars`)
* **Forks** ![Forks](https://img.shields.io/badge/Fork-2-blue) - Fork counts (`gh_forks`)
* **Followers** ![Followers](https://img.shields.io/badge/Followers-29-blue) - Followers count (`gh_followers`)
* **Open Issues** ![Open Issues](https://img.shields.io/badge/open%20issues-0-brightgreen) - Open issues (`gh_open_issues`)
* **Closed Issues** ![Closed Issues](https://img.shields.io/badge/closed%20issues-1-yellow) - Closed issues (`gh_closed_issues`)
* **Pull Requests** ![Pull Requests](https://img.shields.io/badge/pull%20requests-1%20open-orange) - Open pull requests (`gh_open_pr`)
* **Dependencies** ![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen) - All dependencies (`gh_dependencies`)
* **Repo Size** ![Repo Size](https://img.shields.io/badge/repo%20size-2.31%20MB-blue) - Repo size (`gh_repo_size`)
* **Code Size** ![Code Size](https://img.shields.io/badge/code%20size-4.81%20KB-blue) - Code size (`gh_code_size`)
* **Build Status** ![Build](https://img.shields.io/badge/build-passing-brightgreen) - TravisCI.com (`travis_com`)
* **Build Status** ![Build](https://img.shields.io/badge/build-passing-brightgreen) - TravisCI.org key (`travis_org`)
# Image Q&A

Image Q&A est un programme Python d'extraction d'informations écrites à partir de scan de documents. Il s'appuie sur [Donut](https://huggingface.co/docs/transformers/model_doc/donut), un modèle associant vision et langage, capable de répondre à une question en fonction d'un document, sans OCR direct).

## Structure

- `image_q_and_a.py` : chargement du modèle Donut et processing de l'input et de l'output du modèle, en fonction d'une image et d'une question
- `question_directory.py` : applique une liste de questions à un dossier d’images et renvoie un JSON
- `dataset/` : dossier comprenant les fichiers images

## Installation

```bash
git clone <URL_DU_REPO>
cd image_q_and_a

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

- Placer les fichiers dans le dossier `dataset`
- Modifier le fichier `questions.txt` avec un prompt par ligne
- lancer le script, l'option `save_args` sauvegarde les résultats dans `results.json`

```bash
python question_directory.py [--save_args]
```

## Exemple de sortie

```json
{
    "filename": "/Users/john/Desktop/dataset/testing_data/images/82252956_2958.png",
    "Q&A": [
        {"Get who this is from": " d. j. landro"},
        {"Get who this is to": " k. a. sparrow"}
        ]
}

## POC

Nous testons le programme sur la database [FUNSD](https://guillaumejaume.github.io/FUNSD/) constituée de formulaires scannés de natures différentes. Nous voulons récupérer deux informations :
- Le champ "FROM"
- Le champ "TO"
Bien sûr, tous les documents n'ont pas ces champs.

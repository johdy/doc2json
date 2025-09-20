# Image Q&A multimodal

Image Q&A (multimodal) est un programme Python d'extraction d'informations écrites à partir de scan de documents. Il s'appuie sur [Donut](https://huggingface.co/docs/transformers/model_doc/donut), un modèle associant vision et langage, capable de répondre à une question en fonction d'un document, sans OCR direct).

## Structure

- `src/image_q_and_a_multimodal.py` : chargement du modèle Donut et processing de l'input et de l'output du modèle, en fonction d'une image et d'une question.
- `src/question_directory.py` : applique une liste de questions à un dossier d’images et renvoie un JSON.
- `dataset/` : dossier comprenant les fichiers images.
- `output/` : dossier contenant les json de sortie.

## Installation

```bash
git clone <URL_DU_REPO>
cd image_q_and_a_multimodal

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

- Placer les fichiers dans le dossier `dataset`.
- Modifier le fichier `questions.txt` avec un prompt par ligne.
- lancer le script, l'option `save_json` sauvegarde les résultats dans `outputs/results.json`.

```bash
python question_directory.py [-h] [--save_json] [--name_output NAME_OUTPUT]
                             [--verbose]
```

## Exemple de sortie

```json
[
    {
        "filename": "./dataset/82573104.png",
        "Q&A": [
            {
                "Get who this is from": " david h. remes"
            },
            {
                "Get who this is to": " haney h. bell, esq."
            }
        ]
    }
]
```

## POC

Nous testons le programme sur la database [FUNSD](https://guillaumejaume.github.io/FUNSD/) constituée de formulaires scannés de natures différentes. Nous voulons récupérer deux informations :
- Le champ "FROM"
- Le champ "TO".

### Pipeline

- Chaque image est passée au modèle Donut avec une question spécifique.
- Donut renvoie la réponse sous forme d'une variable `text_sequence`, contenant la question et la réponse.
- Chaque réponse est extraite, normalisée et convertie en JSON pour chaque document.

### Résultats et limites

- Les champs FROM et TO sont correctement extraits dans la grande majorité des documents qui montrent ces champs.
- Cependant le modèle ne peut discener entre une extraction correcte et une hallucination, qui peut arriver si l'information est difficilement lisible ou si, de manière plus problématique, elle est absente du document.

### What's next

- Pour des documents standardisés, un recadrage de l'image sur la zone de l'information requise permettrait de diminuer le bruit.
- Une approche OCR + regex complémentaire pourrait solidifier les résultats.



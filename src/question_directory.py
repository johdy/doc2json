from typing import List, Dict
from glob import glob
import pprint
import argparse
import json
import unicodedata

from PIL import Image

from image_q_and_a import image_q_and_a, load_donut

def normalize(s: str) -> str:
    return unicodedata.normalize("NFKC", s).strip().lower()

def question_directory(directory: List[str], questions: List[str], save_json: bool, name_output: str, verbose: bool) -> Dict:
    """Réponds pour chaque image du répertoire à la liste de questions posées
        Prends un path de répertoire d'image en argument, et 
    """
    processor, model = load_donut(verbose)
    results = []
    for file in directory:
        try:
            image = Image.open(file).convert("RGB")
        except Exception as e:
            print(f"Échec {file}: {e}")
            continue
        q_a = []
        for q in questions:
            q = q.strip()
            answer = image_q_and_a(image, q, processor, model)
            answer_text = normalize(answer["text_sequence"])
            q_a.append({q: answer_text.split(normalize(q))[1]})
        new_line = {"filename": file, "Q&A": q_a}
        results.append(new_line)
        if verbose:
            pprint.pp(new_line)
    if save_json:
        with open("./outputs/" + name_output, "w") as f:
            json.dump(results, f, indent=4)
    else:
        pprint.pp(results)
    return results

if __name__ == "__main__":
    directory = glob("./dataset/*")
    with open('./questions.txt', 'r') as f:
        questions = f.readlines()

    parser = argparse.ArgumentParser()
    parser.add_argument("--save_json", action="store_true")
    parser.add_argument("--name_output", type=str, default="results.json")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    results = question_directory(directory, questions, save_json=args.save_json, name_output=args.name_output, verbose=args.verbose)

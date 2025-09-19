from typing import List, Dict
from glob import glob
import pprint
import argparse
import json

from PIL import Image

from image_q_and_a import image_q_and_a, load_donut

def question_directory(directory: List[str], questions: List[str], save_json: bool) -> Dict:
    """Réponds pour chaque image du répertoire à la liste de questions posées
        Prends un path de répertoire d'image en argument, et 
    """
    processor, model = load_donut()
    results = []
    for file in directory:
        image = Image.open(file).convert("RGB")
        q_a = []
        for q in questions:
            answer = image_q_and_a(image, q, processor, model)
            q_a.append({q: answer["text_sequence"].split(q)[1]})
        new_line = {"filename": file, "Q&A": q_a}
        results.append(new_line)
        if save_json:
            with open("./results.json", "a") as f:
                json.dump(new_line, f)
        else:
            pprint.pp(new_line)
    return results

if __name__ == "__main__":
    directory = glob("./dataset/*")
    with open('./questions.txt', 'r') as f:
        questions = f.readlines()

    parser = argparse.ArgumentParser()
    parser.add_argument("--save_json", action="store_true")
    args = parser.parse_args()

    results = question_directory(directory, questions, save_json=args.save_json)
    pprint.pp(results)

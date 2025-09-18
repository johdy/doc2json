from typing import List, Dict
from glob import glob
import pprint

from PIL import Image

from doc2json import doc2json

def question_directory(directory: List[str], questions: List[str]) -> Dict:
    results = []
    for file in directory:
        image = Image.open(file).convert("RGB")
        q_a = []
        for q in questions:
            results.append(q)
            answer = doc2json(image, q)
            q_a.append({q: answer})
        results.append({"filename": file, "Q&A": q_a})
        pprint.pp(results)
    return results

if __name__ == "__main__":
    directory = glob("/Users/john/Desktop/dataset/testing_data/images/*")
    questions = ["From : ", "To : "]
    results = question_directory(directory, questions)

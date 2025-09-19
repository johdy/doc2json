from typing import List, Dict
from glob import glob
import pprint

from PIL import Image

from img_q_and_a import img_q_and_a

def question_directory(directory: List[str], questions: List[str]) -> Dict:
    results = []
    for file in directory:
        image = Image.open(file).convert("RGB")
        q_a = []
        for q in questions:
            answer = img_q_and_a(image, q)
            q_a.append({q: answer})
        results.append({"filename": file, "Q&A": q_a})
        pprint.pp(results)
    return results

if __name__ == "__main__":
    directory = glob("/Users/john/Desktop/dataset/testing_data/images/*")
    questions = ["Get who this is sent to"]
    results = question_directory(directory, questions)

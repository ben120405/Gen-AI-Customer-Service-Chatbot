import os
import xml.etree.ElementTree as ET

def load_data(data_folder):
    texts = []

    for root_dir, _, files in os.walk(data_folder):

        for file in files:
            if file.endswith(".xml"):

                file_path = os.path.join(root_dir, file)

                try:
                    for event, elem in ET.iterparse(file_path, events=("end",)):

                        if elem.tag == "QAPair":

                            question = elem.findtext("Question")
                            answer = elem.findtext("Answer")

                            if question and answer:
                                text = f"Question: {question.strip()}\nAnswer: {answer.strip()}"
                                texts.append(text)

                            elem.clear()

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return texts
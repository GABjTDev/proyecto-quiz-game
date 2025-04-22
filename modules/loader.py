import json

def load_questions(level):
  
  # Leemos el archivo preguntas.json
  with open("./data/preguntas.json", "r") as p:
    my_data = json.load(p)
    return my_data[level]
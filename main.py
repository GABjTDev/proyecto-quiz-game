from modules.loader import load_questions

def main():
  # Pedimos la dificulta de las preguntas
  level = input("Ingrese el nivel de las preguntas? Facil, Medio, Dificilisimo: ")
  questions = load_questions(level)
  print(questions)

# Iniciamos el codigo
if __name__ == "__main__": 
  main()
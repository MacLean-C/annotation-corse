import re
import sys

def tokenize(input_file, output_file):
    """Séparez le texte en mots et en signes de ponctuation, 
    garder les apostrophes au sein des mots.

    Args:
        input_file (txt): texte à tokéniser
        output_file (txt): texte tokenisé
    """
    with open(input_file, 'r', encoding="utf-8") as file:
        text = file.read()
        text = text.strip()
    
    # regex pour tous les contextes et apostrophes possibles
    tokens = re.findall(r"\b\w+(?:['’ʼʽʾʿˈˊˋˍ̧̄]*\w+)*\b|[^\w\s']|\n", text)

    with open(output_file, 'w', encoding="utf-8") as file:
        for token in tokens:
            if token == "\n":
                continue
            else:
                file.write(token + '\n')

#exécutable en ligne de commande
if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    tokenize(file1, file2)

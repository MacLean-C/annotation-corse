import spacy

#il faut mettre le chemin vers le dossier contenant le modèle
nlp = spacy.load('chemin/vers/le/modèle')

# Créer un objet de type document
# Il est également possible d'utiliser un fichier
doc = nlp("Fighjulu, ed eccu, ùn ci hè omu ; È tutti l' acelli di u celu sò fughjiti. ")

for token in doc:
        print(token.text, token.tag_)


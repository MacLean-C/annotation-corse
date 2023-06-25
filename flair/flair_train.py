
from flair.embeddings import WordEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from flair.data import Corpus
from flair.datasets import ClassificationCorpus
from flair.datasets import ColumnCorpus
from flair.embeddings import FlairEmbeddings
from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings, FastTextEmbeddings
import gensim
from fasttext_custom_embeddings_with_flair import FastTextEmbeddings 

# dossier contenant les fichiers train/test/dev
data_folder = 'data'
columns = {0: "text", 1:"upos"}

# a noter, dev et test sont les mêmes données
# Ceci peut créer des biais et donnera une exactitude plus élevée

corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              test_file='test.txt',
                              dev_file='valid.txt')

#le type d'étiquette à prédire
label_type = 'upos'

#création d'un dictionnaire contenant les catégories à prédire
label_dict = corpus.make_label_dictionary(label_type=label_type)

#initialiser les plongements lexicaux
stacked_embeddings = StackedEmbeddings([
                                        FlairEmbeddings('multi-forward'),
                                        FlairEmbeddings('multi-backward'),
                                       ])

# les plongements lexicaux peuevent être changés ici
model = SequenceTagger(hidden_size=256,
                        embeddings=stacked_embeddings,
                        tag_dictionary=label_dict,
                        tag_type=label_type)

# initialiser le 'trainer'
trainer = ModelTrainer(model, corpus)

# commencer l'entraînement
# nous avons changé uniquement le paramètre "max epochs"
trainer.train('resources/taggers/pos-multi',
              learning_rate=0.1,
              mini_batch_size=32,
              max_epochs=100)
import random
import re
import os
import nltk
from nltk.corpus import gutenberg
import cPickle as pickle

from gensim.models import Word2Vec


nltk.data.path.append('./my_nltk_data/')

class Edi(object):
    def __init__(self, file="austen-persuasion.txt"):

        writepath="save.p"
        mode = 'r' if os.path.exists(writepath) else 'wb'
        # check if model already saved
        with open(writepath, mode) as f:
            if mode =='r':
                self.model = pickle.load(f)
                print "loaded model"
            else:
                self.model = Word2Vec(gutenberg.sents())
                pickle.dump(self.model, f)
                print "saved model"
    
            

    def respond_to(self, message):
        # Find similar wordss
        input_tokens = nltk.word_tokenize(message)
        ans = []
        for inp in input_tokens:
            if len(inp)>2:
                try:
                    ans.append(self.model.most_similar(inp,topn=1)[0][0])
                except:
                    ans.append(inp)
            else:
                ans.append(inp)

        return " ".join(ans)

   
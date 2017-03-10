import random
import re
import os
import nltk
from nltk.corpus import gutenberg, brown, wordnet
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
                self.model = Word2Vec(gutenberg.sents()+brown.sents())
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

    def lemmalist(self,str):
        syn_set = []
        for synset in wordnet.synsets(str):
            for item in synset.lemma_names():
                if item!=str:
                    syn_set.append(item)
        return syn_set

    def lemmalist(self,str):
        syn_set = []
        for synset in wordnet.synsets(str):
            for item in synset.lemma_names():
                if item!=str:
                    syn_set.append(item)
        return syn_set 

    def definitionlist(self,str):
        def_set= []
        for synset in wordnet.synsets(str):
            def_set.append(synset.definition())
        return def_set

    def get_synonyms_or_def(self,message,get_syn=True):
        input_tokens = nltk.word_tokenize(message)
        ans = []
        for inp in input_tokens:
            if(len(inp)<3):
                ans.append(inp)
                continue
            ans_set = []
            if get_syn:
                ans_set=self.lemmalist(inp)
            else:
                ans_set=self.definitionlist(inp)
            if len(ans_set)>0:
                ans.append(random.choice(ans_set))
            else:
                ans.append(inp)
        return " ".join(ans)        

    def handle_message(self,message_text):
        answer="I don't know"
        print message_text
        if "hi" in message_text.lower() or "hello" in message_text.lower():
            answer = "Hello to you too. Type a message or a message beginning with 'syn' or a message beginning with 'def'."
        if "syn" in message_text[:3]:
            answer = self.get_synonyms_or_def(message_text[3:])
        elif "def" in message_text[:3]:
            answer = self.get_synonyms_or_def(message_text[3:],False)
        else:
            answer = self.respond_to(message_text)

        return answer


   
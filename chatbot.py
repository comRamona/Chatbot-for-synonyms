import random
import re
import os
import nltk
from nltk.corpus import gutenberg
import cPickle as pickle

from gensim.models import Word2Vec
from nltkx import NgramModel

nltk.data.path.append('./my_nltk_data/')

class Edi(object):
    def __init__(self, file="austen-persuasion.txt"):

        #tokens = gutenberg.words(file)
        #print "tokenized"
        writepath="save.p"
        mode = 'r' if os.path.exists(writepath) else 'wb'
        with open(writepath, mode) as f:
            if mode =='r':
                self.model = pickle.load(f)
                print "loaded model"
            else:
                self.model = Word2Vec(gutenberg.sents())
                pickle.dump(self.model, f)
                print "saved model"
    
            

    def respond_to(self, message):
        # Pick a random word from the incoming message
        input_tokens = nltk.word_tokenize(message)
        ans = []
        #input_tokens = filter(lambda x: len(x)>2, input_tokens)
        for inp in input_tokens:
            if len(inp)>2:
                try:
                    ans.append(self.model.most_similar(inp,topn=1)[0][0])
                except:
                    ans.append(inp)
            else:
                ans.append(inp)
        # keyword = random.choice(input_tokens)

        # # Use keyword and input length to seed a response
        # input_length = len(input_tokens)
        # num_response_words = int(random.gauss(input_length, input_length / 2)) + 1
        # print "Basing response on keyword %s and length %d" % (keyword, num_response_words)
        # content = self._model.generate(num_response_words, (keyword,))
        # return self._format_response(content)
        return " ".join(ans)

    def _format_response(self, content):
        
        def to_unicode(x):
            if isinstance(x, str):
                return x.decode('utf-8')
            return x

        print content
        s = u' '.join([to_unicode(c) for c in content])
        s = re.sub(r' ([\?,\.:!])', r'\1', content)  # Remove spaces before separators
        return content
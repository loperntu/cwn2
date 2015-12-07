d=dict()

for line in open('cwn_dirty.uniq'):
    lemma_name,definition=line.split()
    if lemma_name not in d:d[lemma_name]=[definition]
    else:d[lemma_name].append(definition)

all_lemma_names=[lemma_name for lemma_name in d]

class Synset:
    def __init__(self,lemma_name,index):
#        lemma_name,index=lemma_name_index.split('.')
        self.lemma_name=lemma_name
        self.definition=d[lemma_name][int(index)]
        self._name='%s.%d' % (lemma_name,index)
    def __repr__(self):
        return "%s('%s')" % ('cwn.Synset',self._name)

def synset(lemma_name,index):
    return Synset(lemma_name,index)

def synsets(lemma_name):
    synset_list=[]
    for i in range(len(d[lemma_name])):
        synset_list+=[synset(lemma_name,i)]
    return synset_list

if __name__=='__main__':
    for synset in synsets(all_lemma_names[0]):
        print synset,synset.definition

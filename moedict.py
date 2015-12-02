d=dict()
for line in open('dict-revised.csv'):
    lemma_name,definition=line.split(',')
    lemma_name,definition=lemma_name.strip(),definition.strip()
    if lemma_name not in d:d[lemma_name]=set([definition])
    else:d[lemma_name].add(definition)

all_lemma_names=set()
for lemma_name,definitions in d.items():
    all_lemma_names.add(lemma_name)

def definitions(lemma_name):
    return d[lemma_name]

# cwn2
## Chinese Wordnet v.2
<ol>
<li>移除和教育部辭典相似的詞意：  
distance.py
<li>合併教育部辭典詞意並選出分離詞意：  
pop.py
</ol>
## 萌典詞意年代排序
sort_moe_by_cwn.py
## cwn.sqlite 資料庫 (http://lope.linguistics.ntu.edu.tw/cwnvis/data/cwn_dirty.sqlite) 主要有三個資料表：
<ol>
<li>cwn_lemma: 記錄 6 碼的 lemma_id 以及 lemma_type
<li>cwn_sense: 在原 lemmaid 擴增 2 碼成為 8 碼的 sense_id，以及 sense_def
<li>cwn_goodSynset: 記錄 synset member 的 sense_id
</ol>
## Chinese Wordnet Python Module
from cwn import synset

s=synset('打')
print ' '.join(s.synonyms)
print ' '.join(s.antonyms)
print ' '.join(s.hyponyms)
print ' '.join(s.hypernyms)


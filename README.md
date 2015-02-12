# cwn2
Chinese Wordnet v.2
<ol>
<li>移除和萌典相似的詞意：  
distance.py
<li>合併萌典詞意並選出分離詞意：  
pop.py
</ol>
##
======
SQLite 資料庫主要有三個資料表：
<ol>
<li>cwn_lemma: 記錄 6 碼的 lemma_id 以及 lemma_type
<li>cwn_sense: 在原 lemmaid 擴增 2 碼成為 8 碼的 sense_id，以及 sense_def
<li>cwn_goodSynset: 記錄 synset member 的 sense_id
</ol>

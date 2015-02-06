# cwn2
Chinese Wordnet v.2 的 SQLite 資料庫
======
資料檔位於 http://lope.linguistics.ntu.edu.tw/cwnvis/data/cwn_dirty.sqlite

主要有三個資料表：
<ol>
<li>cwn_lemma: 記錄 6 碼的 lemma_id 以及 lemma_type
<li>cwn_sense: 在原 lemmaid 擴增 2 碼成為 8 碼的 sense_id，以及 sense_def
<li>cwn_goodSynset: 記錄 synset member 的 sense_id
</ol>

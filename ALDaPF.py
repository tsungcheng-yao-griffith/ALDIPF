dataset = "datasetfinal_no_message.csv"
index = "index.csv"
founta = "hatespeech_text_label_vote_RESTRICTED_100K.csv"

_founta = [L.split("\t")[0].strip() for L in open(founta, encoding="utf-8")]
_index = [L.strip() for L in open(index, encoding="utf-8")]
label = [L.split("\t")[0].strip() for L in open(dataset, encoding="utf-8")]
SGABS = [L.split("\t")[1].strip() for L in open(dataset, encoding="utf-8")]

f = open('ALDaPF.csv', 'w', encoding='utf-8')

for i in range(len(label)):
    f.write(label[i] + '\t')
    f.write(_founta[int(_index[i])] + '\t')
    f.write(SGABS[i] + '\n')
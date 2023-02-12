# Abusive Messages and Personal Perceptions 

Repository for "ALDaPF: An Abusive Language Dataset with Psychological Features". Full text of the paper can be found here

_**About the ALDPF**_

ALDaPF is a abusive language dataset includes three features to denote labels and messages, as well as the psychological features of the annotators who gave the label of each message. This dataset contains 114,027 unfolded messages (38,009 uniqle messages) and psychological features, annotated by 505 MTurk workers.
* Labels: 1 refers to neutral, and 2 refers to harmful
* Message: Tweets selected from Founta's dataset
* Psychological Features: Shortened General Attitude and Belief Scale (SGABS) was used, and the results are presented in the same sequence as they are in the original SGBAS. 



_**Access the ALDPF**_

 You can duplicate the dataset with the following steps.

* Access [Founta's Zenodo page](https://zenodo.org/record/3706866#.YjzZfDUReUk) and request access.
* Put ALDPF.py, datasetfinal_no_message.csv, index.csv, and hatespeech_text_label_vote.csv in the same folder.
* Execute ALDPF.py and obtain ALDPF.csv


_**Appendix**_

* datasetfinal_no_message.csv: a dataset contains new labels and corresponding psychological features. 
* ALDaPF.py: a python script to extract tweets from Founta's dataset and merge them with 'datasetfinal_no_message.csv'.
* index.csv: a supporting document helps ALDaPF.py to pull tweets.
* hatespeech_text_label_vote.csv: the full version of Founta's dataset, which can be acquired from Founta's Zenodo page. (MD5: 0be93b76748d4e0ad9675c73267e69e4)
* ALDaPF.csv : the full version of ALDPF (MD5: 9c03a37d21c1e47489d76e1738bb3698)

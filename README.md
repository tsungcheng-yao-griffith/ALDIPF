# Abusive Messages and Personal Perceptions 

Repository for "ALDaPF: An Abusive Language Dataset with Psychological Features". Full text of the paper can be found here

_**About the ALDaPF**_

ALDaPF is a abusive language dataset includes three features to denote class labels, messages, and the psychological features of the annotators who tagged the messages. This dataset contains 114,027 unfolded messages (38,009 uniqle messages) and psychological features, annotated by 505 MTurk workers.
* Labels: 1 refers to neutral, and 2 refers to harmful
* Message: Tweets selected from Founta's dataset
* Psychological Features: Shortened General Attitude and Belief Scale (SGABS) was used, and the results are presented in the same sequence as they are in the original [SGBAS](https://opal.latrobe.edu.au/articles/educational_resource/Shortened_General_Attitude_and_Belief_Scale_SGABS_/14869962).



_**Access the ALDaPF**_

 You can duplicate the dataset with the following steps.

* Access [Founta's Zenodo page](https://zenodo.org/record/3706866#.YjzZfDUReUk) and request access.
* Put ALDaPF.py, datasetfinal_no_message.csv, index.csv, and hatespeech_text_label_vote_RESTRICTED_100K.csv in the same folder.
* Execute ALDaPF.py and obtain ALDaPF.csv


_**Appendix**_

* datasetfinal_no_message.csv: a dataset contains new labels and corresponding psychological features. 
* ALDaPF.py: a python script to extract messages from Founta's dataset and merge them with 'datasetfinal_no_message.csv'.
* index.csv: a supporting document helps ALDaPF.py to select the right messages in the right sequence.
* hatespeech_text_label_vote_RESTRICTED_100K.csv: the full version of Founta's dataset, which can be acquired from Founta's Zenodo page. (MD5: 0be93b76748d4e0ad9675c73267e69e4)
* ALDaPF.csv : the full version of ALDaPF (MD5: 9c03a37d21c1e47489d76e1738bb3698) 

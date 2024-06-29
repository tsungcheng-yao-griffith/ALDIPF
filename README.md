Repository for "ALDIPF: An Abusive Language Dataset Includes Psychological Features".

_**About the ALDIPF**_

ALDIPF is an abusive language dataset includes three features to denote class labels, messages, and the psychological features of the annotators who tagged the messages. This dataset contains 114,027 unfolded messages (38,009 uniqle messages) and psychological features, annotated by 505 MTurk workers.
* Labels: 1 refers to neutral, and 2 refers to harmful
* Message: Tweets selected from Founta's dataset
* Psychological Features: Shortened General Attitude and Belief Scale (SGABS) was used, and the results are presented in the same sequence as they are in the original [SGBAS](https://opal.latrobe.edu.au/articles/educational_resource/Shortened_General_Attitude_and_Belief_Scale_SGABS_/14869962).



_**Access the ALDIPF**_

 You can duplicate the dataset with the following steps.

* Access [Founta's Zenodo page](https://zenodo.org/record/3706866#.YjzZfDUReUk) and request access.
* Put ALDIPF.py, datasetfinal_no_message.csv, index.csv, and hatespeech_text_label_vote_RESTRICTED_100K.csv in the same folder.
* Execute ALDIPF.py and obtain ALDIPF.csv


_**Appendix**_

* datasetfinal_no_message.csv: a dataset contains new labels and corresponding psychological features. 
* ALDIPF.py: a python script to extract messages from Founta's dataset and merge them with 'datasetfinal_no_message.csv'.
* index.csv: a supporting document helps ALDIPF.py to select the right messages in the right sequence.
* hatespeech_text_label_vote_RESTRICTED_100K.csv: the full version of Founta's dataset, which can be acquired from [Founta's Zenodo page](https://zenodo.org/record/3706866#.YjzZfDUReUk).
* ALDIPF.csv : the full version of ALDIPF (MD5: 9c03a37d21c1e47489d76e1738bb3698) 


_**Cite this Dataset**_
@misc{yao2022aldipf,
  author = {Tsuncheng Yao and Sebastian Binnewies and Ernest Foo and Macie Alavi},
  title = {{ALDIPF}: An Abusive Language Dataset Includes Psychological Features},
  year = {2022},
  howpublished = {\url{https://github.com/tsungcheng-yao-griffith/ALDIPF}},
  note = {Accessed June 29, 2024}
}

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


_**Dataset Description**_

ALDIPF is an abusive language dataset comprising 38,009 unique messages or a total of 114,027 annotated
messages. This dataset is built on the Founta dataset and enhanced with additional psychological features. These
features – Messages, Psychological Features, and Class labels denote the essential components of the ABC model.
Messages are Triggers; the Psychological Features refer to one’s Beliefs and Attitudes; the Class Labels indicate the
emotional Consequences the Messages provoke. An introduction of each feature is as follows.
ALDIPF collected messages from the Founta dataset that satisfied two criteria: (i) messages that were originally
annotated as “normal”, and (ii) messages that did not reach full consensus on a voting scheme. This selection of
messages was based on a hypothesis that the impact of the psychological features may be more substantial on these
contested messages.

ALDIPF categorised messages into two Class Labels: Neutral and Harmful. These labels were tagged based on
annotators’ perceptions (or feelings) about messages after reading them. 65.6% of the messages were tagged as Neutral,
and the rest were labelled as Harmful. In addition, if a voting scheme aggregates these Class Labels, the Neutral Labels
count 73.5%.

Psychological Features were measured by “Five-point Shortened General Attitude and Belief Scale (SGABS)”.
SGABS measures ones’ psychological features from seven aspects that can be transferred to several clinical indicators.
These clinical indicators can either help predict one’s general well-being or differentiate particular groups of individuals
from others.

Lastly, ALDIPF allows one message to be associated with
more than one Class Label. That is because, according to the ABC model, annotators with different psychological
features can feel the same messages in different ways. Additionally, the psychological Features comprise eight SGABS
items that follow the same sequence as shown in Table 1. Lastly, the Source column is not provided in the open-accessed
ALDIPF.


_**Appendix**_

* datasetfinal_no_message.csv: a dataset contains new labels and corresponding psychological features. 
* ALDIPF.py: a python script to extract messages from Founta's dataset and merge them with 'datasetfinal_no_message.csv'.
* index.csv: a supporting document helps ALDIPF.py to select the right messages in the right sequence.
* hatespeech_text_label_vote_RESTRICTED_100K.csv: the full version of Founta's dataset, which can be acquired from [Founta's Zenodo page](https://zenodo.org/record/3706866#.YjzZfDUReUk).
* ALDIPF.csv : the full version of ALDIPF (MD5: 9c03a37d21c1e47489d76e1738bb3698) 


_**Cite this Dataset**_

@article{YAO2025127188,
title = {See the words through my eyes: The role of personal traits in abusive language detection},
journal = {Expert Systems with Applications},
volume = {276},
pages = {127188},
year = {2025},
issn = {0957-4174},
doi = {https://doi.org/10.1016/j.eswa.2025.127188},
url = {https://www.sciencedirect.com/science/article/pii/S0957417425008103},
author = {Tsungcheng Yao and Sebastian Binnewies and Ernest Foo and Masoumeh Alavi},
}

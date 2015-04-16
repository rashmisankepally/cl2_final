This repo contains the code for the final project for CMSC773 (Computational Linguistics II), Spring 2015.

#### Instructions to setup the repo

1. Clone the repo to a suitable folder
2. Unpack project_materials.zip (not included) into the project_materials folder
3. Download the necessary GloVe vectors (http://www-nlp.stanford.edu/data/glove.twitter.27B.25d.txt.gz 
and http://www-nlp.stanford.edu/data/glove.840B.300d.txt.gz) and unpack them inside other_data.
3. In scripts/config.sh, change the PROJECT_HOME environment variable to point to where the repo was cloned. For example,
if it was cloned in "/Documents/773", then PROJECT_HOME should point to "/Documents/773/cl2_final"

#### External dependencies

* Python libraries - gensim


#### Instructions to run scripts

1. Source the config file by doing 
	   . scripts/config.sh
2. Run any script


#### What do the scripts do?

* get_depressed.sh - Create user_info_dict.p pickle



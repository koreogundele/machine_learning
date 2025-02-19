# I can't get the deepchem package to work due to dependency issues. I am working it out within the jupyter notebook.
# In the meantime, I guess it's valuable to type out the full code here? Idk, just learning as I go.

import numpy as np
import deepchem as dc

# load data and split into datasets
tox21_tasks, tox21_datasets, transformers = dc.molnet.load_tox21()
train_dataset, valid_dataset, test_dataset = tox21_datasets

# build and train model

# evaluate on training and test sets
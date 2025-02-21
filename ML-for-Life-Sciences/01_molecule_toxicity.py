# I can't get the deepchem package to work due to dependency issues. I am working it out within the jupyter notebook.
# In the meantime, I guess it's valuable to type out the full code here? Idk, just learning as I go.

import numpy as np
import deepchem as dc

# load data and split into datasets
tox21_tasks, tox21_datasets, transformers = dc.molnet.load_tox21()
training_dataset, validation_dataset, test_dataset = tox21_datasets

# build and train model
model = dc.models.MultitaskClassifier(n_tasks=12, n_features=1024, layer_sizes=[1000]) # using textbook numbers right now, might mess with these a bit
model.fit(training_dataset, nb_epoch=10)

# evaluate model
metric = dc.metrics.Metric(dc.metrics.roc_auc_score, np.mean)

training_scores = model.evaluate(training_dataset, [metric], transformers)
test_scores = model.evaluate(test_dataset, [metric], transformers)

print(f"Training dataset scores are: {training_scores}")
print(f"Test dataset scores are: {test_scores}")
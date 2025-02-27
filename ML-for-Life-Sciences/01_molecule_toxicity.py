# This short script builds and evaluates a model that predicts molecule toxicity.

import numpy as np
import deepchem as dc

# load data from Tox21 dataset. Split into tasks, datasets & transformers
tox21_tasks, tox21_datasets, transformers = dc.molnet.load_tox21()
training_dataset, validsation_dataset, test_dataset = tox21_datasets


# DeepChem's dc.models contains many different life science-specific models. Here we use MultitaskClassifier
model = dc.models.MultitaskClassifier(n_tasks=12, n_features=1024, layer_sizes=[1000]) # using textbook numbers right now, might mess with these a bit
model.fit(training_dataset, nb_epoch=10)

# evaluate performance using ROC (receiver opeating characteristic) AUC across all tasks
metric = dc.metrics.Metric(dc.metrics.roc_auc_score, np.mean)

# get scores using model.evaluate
training_scores = model.evaluate(training_dataset, [metric], transformers)
test_scores = model.evaluate(test_dataset, [metric], transformers)

print(f"Training {training_scores}")
print(f"Test {test_scores}")
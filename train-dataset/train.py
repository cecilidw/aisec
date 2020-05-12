
import os
import math
import string
import numpy as np

from azureml.core import Dataset, Run
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score 
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.externals import joblib


run = Run.get_context()

# get input dataset by name
dataset = run.input_datasets['SecBugDataset']

df = dataset.to_pandas_dataframe()


# create column used as target

df['Label'] = [1 if x =='Integrity/Security' else 0 for x in df['L2']]

# do the vectorization - tf-idf

vectorizer = TfidfVectorizer(min_df=2)
tfidf = vectorizer.fit_transform(df['summary'])
tfidf = tfidf.toarray()

# create our feature column
df['summary_vec'] = list(tfidf)

#dividing X,y into train and test data
X_train, X_test, y_train, y_test = train_test_split(df['summary_vec'].tolist(), df['Label'].tolist(), test_size=0.2, random_state=66)


# create our classifier & train it
model = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr')
model.fit(X=X_train, y=y_train)

# make predictions to see how well it does
y_pred = model.predict(X=X_test)

# measure it with to different metrics
auc_weighted = roc_auc_score(y_test, y_pred,average="weighted")
accuracy = accuracy_score(y_test, y_pred)

# log the metrics we want to track and measure on to the Run
run.log("AUC_Weighted", auc_weighted)
run.log("Accuracy", accuracy)

model_file_name = 'LogRegModel.pkl'


# The training script saves the model into a directory named ‘outputs’. Files saved in the 
# outputs folder are automatically uploaded into experiment record. Anything written in this 
# directory is automatically uploaded into the workspace.
os.makedirs('./outputs', exist_ok=True)
with open(model_file_name, 'wb') as file:
    joblib.dump(value=model, filename='outputs/' + model_file_name)

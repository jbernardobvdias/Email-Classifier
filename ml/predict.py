from sklearn.model_selection import train_test_split
from lazypredict.Supervised import LazyClassifier
from data.helper import read
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = read("../dataset/emails.json", True)

# Vectorize the text content
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Split and run LazyPredict
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LazyClassifier(verbose=1)
models, predictions = clf.fit(X_train.toarray(), X_test.toarray(), y_train, y_test)


# View results
print(models)

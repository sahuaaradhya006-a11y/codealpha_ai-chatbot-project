import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

with open("intents.json") as file:
    data = json.load(file)

patterns = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern.lower())
        tags.append(intent["tag"])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

model = LogisticRegression()
model.fit(X, tags)

def get_response(user_input):
    X_test = vectorizer.transform([user_input.lower()])
    
    probs = model.predict_proba(X_test)
    max_prob = max(probs[0])

    # Confidence check
    if max_prob < 0.3:
        return None

    tag = model.predict(X_test)[0]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "I’m not sure I understand. Could you please rephrase?"
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder, FunctionTransformer
import nltk
import pickle
import pandas as pd
from helpers import get_activity_text, get_wbs_text, get_combined_text, preprocess_text


# Train the model
def train_model(version):
    #Necessary downloads for nltk, only need to download once, or download to update them
    nltk_packages = [('tokenizers/punkt', 'punkt'), ('corpora/stopwords', 'stopwords'), ('corpora/wordnet', 'wordnet')]
    for package_path, package_name in nltk_packages:
        try:
            nltk.data.find(package_path)
        except LookupError:
            nltk.download(package_name)
            
    df = pd.read_hdf('training_data_V4.h5', key='df')

    # Get the WBS
    df['WBS'] = df['Name']
    df['WBS'] = df['WBS'].apply(preprocess_text)

    df['ActivityName'] = df['ActivityName'].apply(preprocess_text)
    df['WBS'] =df['WBS'].apply(preprocess_text)

    df['combined'] = df['WBS'] + ' ' + df['ActivityName']
    df['combined'] = df['combined'].apply(preprocess_text)

    label_encoder = LabelEncoder()
    df['RESP_encoded'] = label_encoder.fit_transform(df['MergedActivityCodeValue'])

    maxFeatures = 30000

    ngram = (1,2)

    tfidf_vectorizer_activity = TfidfVectorizer(max_features=maxFeatures, ngram_range=ngram)
    tfidf_vectorizer_wbs = TfidfVectorizer(max_features=maxFeatures, ngram_range=ngram)
    tfidf_vectorizer_combined = TfidfVectorizer(max_features=maxFeatures, ngram_range=ngram)

    # Replace the lambda functions with the top-level functions
    get_activity_text_transformer = FunctionTransformer(get_activity_text, validate=False)
    get_wbs_text_transformer = FunctionTransformer(get_wbs_text, validate=False)
    get_combined_text_transformer = FunctionTransformer(get_combined_text, validate=False)

    rf_classifier = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42, n_jobs=-1)

    pipeline = Pipeline([
        ('features', FeatureUnion([
            ('activity', Pipeline([
                ('selector', get_activity_text_transformer),
                ('tfidf', tfidf_vectorizer_activity),
            ])),
            ('wbs', Pipeline([
                ('selector', get_wbs_text_transformer),
                ('tfidf', tfidf_vectorizer_wbs),
            ])),
            ('combined', Pipeline([
                ('selector', get_combined_text_transformer),
                ('tfidf', tfidf_vectorizer_combined),
            ])),
        ])),
        ('clf', rf_classifier),
    ])
    
    # X = df['ActivityName']  # Features
    X = df[['ActivityName', 'WBS', 'combined']]  # Features
    y = df['RESP_encoded']  # Target labels

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    with open(f'X_train{version}.pkl', 'wb') as f:                                
        pickle.dump(X_train, f)

    with open(f'y_train{version}.pkl', 'wb') as f:                
        pickle.dump(y_train, f)

    with open(f'X_test{version}.pkl', 'wb') as f:
        pickle.dump(X_test, f)

    with open(f'y_test{version}.pkl', 'wb') as f: 
        pickle.dump(y_test, f)

    # Train the model
    pipeline.fit(X_train, y_train)

    # Predictions
    y_pred = pipeline.predict(X_test)

    with open('y_pred{version}.pkl', 'wb') as f:                
        pickle.dump(y_pred, f)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    unique_labels = sorted(list(set(y_test)))  # Unique labels in y_test
    classification_rep = classification_report(y_test, y_pred, labels=unique_labels, target_names=[str(x) for x in label_encoder.inverse_transform(unique_labels)])

    print("Accuracy:", accuracy)
    print("Classification Report:", classification_rep)

    # Saving the model files
    with open(f'RF_model_V{version}.pkl', 'wb') as f:
        pickle.dump(pipeline, f)
    with open(f'label_encoder_V{version}.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)
    return df
            
if __name__ == "__main__":
    print(train_model(version=9))

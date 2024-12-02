import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import shap
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint


def train_model(x, y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Hyperparameters distribution for Random Forest to test during CV
    param_dist = {'n_estimators': randint(50, 500),
                  'max_depth': randint(5, 20),
                  'min_samples_split': randint(2, 5),
                  'min_samples_leaf': randint(2, 5),
                  'bootstrap': [True, False],
                  'max_features': ['sqrt', 'log2', 0.2, 0.5]}


    # Tuning Random Forest with RandomSearchCV
    rf = RandomForestClassifier()
    tuned_forest = RandomizedSearchCV(rf,
                                     param_distributions=param_dist,
                                     n_iter=50,
                                     cv=5,
                                     n_jobs=-1)
    tuned_forest.fit(X_train, y_train)
    best_rf = tuned_forest.best_estimator_

    # Adding HistGradientBoostingClassifier
    gradient_boost = HistGradientBoostingClassifier()
    gradient_boost.fit(X_train, y_train)

    # VotingClassifier with best models
    vote = VotingClassifier([('rf', best_rf), ('gb', gradient_boost)], voting='soft')
    vote.fit(X_train, y_train)

    # Predict and review accuracy
    y_pred = best_rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Accuracy: {accuracy}")

    joblib.dump(vote, 'models/rf_model.pkl')

    return vote
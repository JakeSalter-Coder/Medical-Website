import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.ensemble import RandomForestClassifier
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
    print("Best hyperparameters:", tuned_forest.best_params_)

    # Predict and review accuracy
    y_pred = best_rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Create visualizations of model
    create_visualizations(best_rf, x)

    print(f"Accuracy: {accuracy}")

    joblib.dump(best_rf, 'models/rf_model.pkl')

    return best_rf

def create_visualizations(model, x):
    feature_importances = model.feature_importances_
    plt.figure(figsize=(8, 6))
    sns.barplot(x=feature_importances, y=x.columns)
    plt.title('Feature Importance')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.savefig('static/images/feature_importance.png')
    plt.close()
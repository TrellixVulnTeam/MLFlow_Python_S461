from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import mlflow
import mlflow.sklearn

SPLIT_PROP = 0.25
RAND_STATE = 123

# Create data 
data = load_iris()
print(data.target)
print(data.target_names)
print(data.feature_names)

# Create X and Y data
X = data.data
y = data.target

# Create simple train and test split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=SPLIT_PROP, random_state=RAND_STATE)

# MLFlow routine start 

with mlflow.start_run():
    dtc = DecisionTreeClassifier(random_state=RAND_STATE)
    dtc.fit(X_train, y_train)
    y_pred_class = dtc.predict(X_test)
    acc = metrics.accuracy_score(y_test, y_pred_class)
    roc = metrics.roc_auc_score(y_test, y_pred_class)

    # Log those bad boy metrics in MLFlow
    mlflow.log_param('random_state', RAND_STATE)
    mlflow.log_metric('accuracy', acc)
    mlflow.log_metric('roc_auc', roc)
    # Log the model
    mlflow.sklearn.log_model(dtc, "model")
    mdl_path= '/dbfs/mlflow/iris/model-%s-%f' % ('decision_tree',1)
    mlflow.sklearn.save_model(dtc, mdl_path)
    # Could save a confusion matrix here
    #mlflow.log_artifact('image.png')




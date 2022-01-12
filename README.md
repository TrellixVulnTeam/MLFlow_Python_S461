# ML Flow Examples in Python

![](MLFlow_Examples/figures/images/mlflow_logo.png)

This contains a repository of all the **MLFlow** examples in Python. The project structure currently contains:

1. [**Basic ML Flow - checking ML flow version**](https://github.com/StatsGary/MLFlow_Python/blob/main/MLFlow_Examples/01_MLFlow_Basics.py)
2. [**Basic Metric Logging**](https://github.com/StatsGary/MLFlow_Python/blob/main/MLFlow_Examples/02_Basic_Metric_Logging.py)
3. [**Logging a Sci-Kit Learn project, alongide model registration with **log_model****](https://github.com/StatsGary/MLFlow_Python/blob/main/MLFlow_Examples/03_Logging_SCIKIT_Learn_Experiment.py)
4. [**Conda packaging**](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/04_PackagingModelCode) - deploy your model in a package and pass to other users, or deploy in the cloud with Azure or GCP
5. [**Specifying additional pip installs**]() - this shows how to build additional requirements into your script
6. [**Working with PyTorch**](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/06_PyTorchWithMLFlow/MNIST) - to create, and package, a MNIST computer vision classification algorithm and s
7. [**Working with Tensorflow 2 model**](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/07_Tensorflow_MLFlow/tf2) and packaging it up to work with MLFlow
8. [**XGBoost native**](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/08_XGBoost_MLFlow/xgboost_native) and [**XGBoost Scikit Learn**](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/08_XGBoost_MLFlow/xgboost_sklearn) - shows different approachesd to packaging these models up
9. [**Dockerising MLFlow**](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/09_Dockerising_MLFlow) - uses MLFlow guides to show how the model can be packages up into Docker and ran as a microservice.
10. [**FastAI Example with MLFlow**](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/10_FastAIExample) - how to work with FastAI
11. [Experiment tracking](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/11_TrackingModel_Metrics) - shows how to track experiments in MLFlow
12. [**Multiple workstep example in MLFlow**](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/12_MultiWorkstep_MLFlow) - how to work with multiple workflow steps, as you may want to log metrics from data prep, training and evaluation phases.
13. [**Hyperparameter tuning and MLFlow**](https://github.com/StatsGary/MLFlow_Python/tree/main/MLFlow_Examples/13_Deploy_with_HP_tuning) - this shows how to log multiple runs when capturing the hyperparameters.


## Still to come
I aim to add a couple more modules on model registration, experiment creation and doing all the steps in script. Watch this space for future additions to this repository.
import os 
from mlflow import log_metric, log_param, log_artifact
# python train.py
#pip install mlflow[extras]

if __name__ == '__main__':
    # Log a parameter
    log_param("param1", 5)

    # Log metrics
    log_metric("foo", 1)
    log_metric("foo", 2)
    log_metric("foo", 3)


    # Log artifact
    with open('output.txt', 'w') as f:
        f.write('Hello World!')
    log_artifact('output.txt')
# mlflow_example
This repository contains example code to show the usage of the open source program mlflow: https://www.mlflow.org
## Why mlflow?
Mlflow helps to maintain **TRACEABILITY** and **REPRODUCIBILITY**  of your experiments.
* **TRACEABILITY**: You should be able to trace back each artifact to an exact experiment setting. 
Example: For a trained model you must know, which data and parameters were used.
* **REPRODUCIBILITY**: You must be able to reproduce each experiment in exactly the same way in the future.

These two principles are super important in software engineering companies (and academics as well!).

## Installation
### Setup
You need a python environment with python and pip installed. With [miniconda](https://docs.conda.io/en/latest/miniconda.html) you can do for example:
* `conda create -n 'mlflow_test' python==3.8`
* `conda activate mlflow_test`
### Installation
`pip install mlflow` - it's that simple :)


## How to run the example
The python file acts as an example for an experiment you want to track. Run it with:
* `python mlflow_example.py`

You should now see an `mlruns` folder which contains the logs. 
Now in the same directory, run the graphical interface of mlflow with:
* `mlflow ui`

The graphical interface can be viewed in the browser under the default link http://127.0.0.1:5000 

## Some tips to run it on the server
On a bigger scale, you would set up an mlflow tracking server: https://www.mlflow.org/docs/latest/tracking.html#tracking-server.
If this is not set up, you can anyway use mlflow with a workaround:
* After your experiments are finished, you can copy the mlruns folder to your local pc or synchronize it (f.e. via rsync)
* or: you can run 
    * `mlflow ui --port 1234` on the server (instead of 1234 you can use any free port number) and 
    * forward the port to your local pc with: `ssh -L 5000:127.0.0.1:1234 username@server_url.es`.
    * Now, the ui is available under https://localhost:5000 on your local pc.

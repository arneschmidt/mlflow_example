import mlflow

mlruns_folder = 'mlruns'
experiment_name = 'test_experiment'
run_name = 'test_run'

mlflow.set_tracking_uri(mlruns_folder)
experiment_id = mlflow.set_experiment(experiment_name)
mlflow.start_run(experiment_id=experiment_id, run_name=run_name)

config = {'learning_rate': 0.01,
          'batch_size':32,
          'image_size':[1024, 1024]}

train_accuracy = 0.05
loss = 10.0
for i in range(10):
    print("Iteration: ", i)
    train_accuracy = train_accuracy * 1.2
    loss = loss * 0.9

    mlflow.log_metric('train_accuracy', train_accuracy, step=i)
    mlflow.log_metric('loss', loss, step=i)

test_result = {'test_accuracy': 0.5, 'f1_score': 0.4}
mlflow.log_metrics(test_result)

mlflow.log_artifact('test_artifact.txt')


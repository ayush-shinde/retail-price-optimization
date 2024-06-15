from zenml import pipeline
from zenml.config import DockerSettings
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.constants import MLFLOW
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step

from steps.data_splitter import split_data
from steps.deployment_trigger_step import deployment_trigger
from steps.evaluator import evaluate
from steps.ingest_data import ingest
from steps.process_data import categorical_encode, feature_engineer
from steps.train_model import re_train, train

docker_settings = DockerSettings(required_integrations=[MLFLOW])

@pipeline(enable_cache=False, settings={"docker": docker_settings})
def continuous_deployment_pipeline(
    min_accuracy: float = 0.9,
    workers: int = 1,
    timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
):
    df = ingest("retail_prices")
    df_processed = categorical_encode(df)
    df_transformed = feature_engineer(df_processed)  
    X_train, X_test, y_train, y_test = split_data(df_transformed) 
    model, predictors = train(X_train, y_train)
    
    mlflow_model_deployer_step(
        model=model,
        workers=workers,
        timeout=timeout,
    )

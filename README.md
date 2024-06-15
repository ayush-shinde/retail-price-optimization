# Retail Price Optimization - Enhancing Sales

In the highly competitive retail market of today, determining the right price for products is critical. This project leverages machine learning techniques for retail price optimization to predict customer satisfaction scores, a key component in developing dynamic pricing strategies that boost sales and customer satisfaction.

**Problem statement:** Our goal is to create a model that predicts the optimal price for a product based on various factors. This prediction enables informed pricing decisions, ultimately maximizing sales and enhancing customer satisfaction.

The dataset encompasses a range of features such as product details, order specifics, review information, pricing, competition, time, and customer demographics, providing a comprehensive foundation for our price optimization efforts.

By analyzing these data points, we aim to predict the optimal retail prices, aiding strategic pricing decisions and effectively optimizing retail prices.

The sample dataset includes various details about each order, such as:

- Product details: ID, category, weight, dimensions, and more.
- Order details: Approved date, delivery date, estimated delivery date, and more.
- Review details: Score and comments.
- Pricing and competition details: Total price, freight price, unit price, competitor prices, and more.
- Time details: Month, year, weekdays, weekends, holidays.
- Customer details: ZIP code, order item ID.

## 🐍 Python Requirements

To get started with the required Python packages, run the following commands within your preferred Python environment:

```python
git clone git@github.com:ayush-shinde/retail-price-optimization.git
pip install -r requirements.txt
```

Starting with ZenML 0.20.0, ZenML includes a React-based dashboard to monitor your stacks, stack components, and pipeline DAGs. To access this dashboard, you need to launch the ZenML Server and Dashboard locally. First, install the optional dependencies for the ZenML server:

```python
pip install zenml["server"]
zenml up
```

If you are running the `run_cid_pipeline.py` script, you will also need to install some integrations using ZenML:

```
zenml integration install mlflow -y
zenml integration install bentoml
```

The project can only be executed with a ZenML stack that has an MLflow experiment tracker and BentoML model deployer as a component. Configuring a new stack with the two components are as follows:

```
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register bentoml_deployer --flavor=bentoml
zenml stack register local_bentoml_stack \
  -a default \
  -o default \
  -d bentoml_deployer \
  -e mlflow_tracker
  --set
```

## 🚀 Training Pipeline

Our standard training pipeline consists of several steps:

- `ingest`: Ingests the data from the databas into the ZenML repository.
- `categorical_encoder`: Encodes the categorical features of the dataset.
- `feature_engineer`: Create new features from the existing features.
- `split`: Splits the dataset into train and eval splits.
- `train`: Trains the model on the training split.
- `evaluate`: Evaluates the model on the eval split.
- `decision`:
<<<<<<< HEAD
- `deploy`: Deploys the model to a BentoML endpoint.
=======
- `deploy`: Deploys the model to a BentoML endpoint.
>>>>>>> b4278b612d733f2af48e6917cad2592e8df3d770

import os
from datetime import datetime

DATABASE_NAME = "US_Visa"
COLLECTION_NAME = "Visa_dataA"
MONGODB_URL_KEY  = "MONGODB_URL"

PIPELINE_NAME: str = "us_visa_pipeline"
ARTIFACT_DIR: str = "artifact"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
FILE_NAME: str = "usvisa.csv"

MODEL_FILE_NAME: str = "model.pkl"

"""
Data Ingestion related constant start with DATA_INGESTION VARIBLE NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "Visa_dataA"
DATA_INGESTION_DIR_NAME: str = "data_ingestion" 
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


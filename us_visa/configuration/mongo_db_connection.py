import sys
from us_visa.exception import USVISAException
from us_visa.logger import logging
import os
from us_visa.constants import DATABASE_NAME,MONGODB_URL_KEY
import pymongo
import certifi


ca = certifi.where()

class MongoDBClient:
    """
    class name : export_data_into_feature_store
    description : This method exports the data from mongodb to feature store as dataframe
    output: connection to mongodb database
    on failure : raise exception
    """
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise USVISAException(f"Environment key : {MONGODB_URL_KEY} not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("Connected to Mongodb database successfully")
        except Exception as e:
            raise USVISAException(e, sys)
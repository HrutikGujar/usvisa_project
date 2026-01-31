#from us_visa.logger import logging
#from us_visa.exception import USVISAException
#import sys

#logging.info("Demo file is run")
#logging.info("Another info log from demo file")


#try:
#    a = 5 / 0
#except Exception as e:   
#    raise USVISAException(e, sys)
#import os

#mongo_db_url = os.getenv("MONGODB_URL")
#print(mongo_db_url)

from us_visa.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()


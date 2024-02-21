'''
@Author : Sumit Ranjan
'''

import time
import Log

#from settings import AUTH_USERNAME, AUTH_PASSWORD, openai_key, rhea_url
from settings import AUTH_USERNAME, AUTH_PASSWORD

#openai.api_key = openai_key
logger = Log.get_logger()

def get_completions(data):
    logger.info("===============================================================================================================")
    logger.info("get_completions called........ ")
    answer = [{
                "output": "answer........."
                
            }]
    return answer
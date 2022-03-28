import pandas
import requests

class MoviesETL(object):
    """
    This is a blueprint etl pipeline
    """
    
    def __init__(self,config):
        """
        Constractor wth parameters initialization 
        """
        self.api_key = config["api_key"]
        

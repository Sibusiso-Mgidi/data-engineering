import re
import pandas as pd
import requests
import json

class MoviesETLPipeline(object):
    """
    This is a blueprint etl pipeline
    """
    
    def __init__(self,config):
        """
        Constractor wth parameters initialization 
        """
        self.api_key = config["api_key"]
        self.movie_id = config["movie_id"]
        

    def get_extract(self):
        """
        This is a method for getting data from the movies DB.
        """

        # create a lopp 
        response_list = []
        for self.movie_id in range(550, 556):
            
            url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(self.movie_id, self.api_key)
        
            #send a get request
            meta_data = requests.get(url).json()
            response_list.append(meta_data)
        
        df = pd.DataFrame.from_dict(response_list)

        return df

if __name__ == "__main__":

    with open("config.json") as config_file:
        # get API authentication/configurations
        data = json.load(config_file)

    # get movies ETL pipeline object
    api_object = MoviesETLPipeline(data)

    # call the extract  method to source 3rd party data.
    df =  api_object.get_extract()
    print(df)



    



    



        


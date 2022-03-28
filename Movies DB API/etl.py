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

    def get_transform(self, df):
        """
        This is a method for structuring the raw data from the source.
        """

        df_columns = ['budget', 'genres', 'id', 'imdb_id', 'original_title', 'release_date', 'revenue', 'runtime']
        genres_list = df['genres'].tolist()
        
        # here we expand this column out so we can easily see and make use of the internal records.
        flat_list = [item for sublist in genres_list for item in sublist]
        
        # the idea: we want to create a separate table for genres and a column of lists to explode out.
        result = []
        for l in genres_list:
            r = []
            for d in l:
                r.append(d['name'])
            result.append(r)
        df = df.assign(genres_all = result)
        
        # here we create the genres table.
        df_genres = pd.DataFrame.from_records(flat_list).drop_duplicates()
        
        return df_genres


if __name__ == "__main__":

    with open("config.json") as config_file:
        # get API authentication/configurations
        data = json.load(config_file)

    # get movies ETL pipeline object
    api_object = MoviesETLPipeline(data)

    # call the extract  method to source 3rd party data.
    df =  api_object.get_extract()

    # call the transform method
    transformed_df = api_object.get_transform(df)
    print(transformed_df)





    



        


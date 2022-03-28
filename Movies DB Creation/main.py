__author__ = "Sibusiso Mgidi"
__version__ = "1.0.0"
__email__ = "mgiditercy@gmail.com"
__status__ = "Development"

from etl import *

with open("config.json") as config_file:
    # get database login credintials.
    data = json.load(config_file)

# get an automated database object 
    moviesdb_object = MoviedDB(data)
    conn, cur =  moviesdb_object.get_establish_connection()
    
    
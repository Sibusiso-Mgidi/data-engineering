import sys
import pymysql
import csv
import json

class MoviedDB():
    """
    This is a blueprint for establishing connection between the correct database and run queries.
    """
    def __init__(self, data):
        """
        Constractor with parameters initialization
        """
        self.host_name =  data["host_name"]
        self.port_number = data["port_number"]
        self.user_name = data["user_name"]
        self.token = data["token"]
        self.database = data["database_name"]

    def get_establish_connection(self):
        """
        This method stablish connection to the database.
        :returns: 
        -- conn: network connection to the database.
        -- cur: connectin cursor object.
        """
        conn =  pymysql.connect(host = self.host_name, port = self.port_number, user = self.user_name, passwd = self.token, db = self.database)
        cur = conn.cursor()

        return conn, cur



with open("config.json") as config_file:
    # get database login credintials.
    data = json.load(config_file)

# get an automated database object 
    moviesdb_object = MoviedDB(data)
    conn, cur =  moviesdb_object.get_establish_connection()
    
    
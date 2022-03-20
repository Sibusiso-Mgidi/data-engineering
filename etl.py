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



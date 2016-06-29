# -​*- coding: utf-8 -*​-

from bitoolbox.dbtools import dbtools as db


def get_data():
    with open('./queries/alpha.sql') as query_file:
        query = query_file.read()
    data = db.df_from_mysql(query, "ESCALERDS")
    return data

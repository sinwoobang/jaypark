from datetime import datetime

from neomodel import db as graphdb


def cypher_query_as_dict(query, params):
    """
    Run a cypher query and change its type from List to Dictionary.
    :param query: Cypher Query
    :param params: Parameters of the query
    :return: A list whose type of each element is Dictionary.
    """
    query_result = graphdb.cypher_query(query, params=params)
    data_raw = query_result[0]  # The result data of the query
    field_names = query_result[1]

    data = []  # a return data
    for row in data_raw:  # iterates a raw data and changes its type to Dict.
        element = {}
        for idx, field_name in enumerate(field_names):
            element[field_name] = row[idx]
        data.append(element)
    return data


def timestamp2datetime(timestamp):
    """
    Convert Timestamp to Datetime
    :param timestamp:
        Timestamp(ex. 1554908239776).
        Please NOTE you should multiply * 1000 if you've used the default timestamp in Python.
    :return Datetime object:
    :rtype: datetime.datetime
    """
    return datetime.utcfromtimestamp(timestamp // 1000)
import os
from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename = "Fremont.csv", url = URL, force_download = False):
    """
    Download and cache fremont date
    Parameters
    -----------
    filename: string (optional)
        location to save the data
    url: string (optional)
        web location of the data
    force_download: bool (optional)
        if True force download the data
    Returns
    -----------
    data: pd.DataFrame
        the Fremont bridge bike data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)

    data = pd.read_csv(filename, index_col="Date")
    
    try:
        data.index = pd.to_datetime(data.index, format="%m/%d/%Y %I:%M:%S %p")
    except ValueError:
        data.index = pd.to_datetime(data.index)

    data.columns = ['West', 'East']
    data['Total'] = data.sum(axis = 1)
    return data

import numpy as np
import pandas as pd

from logger_class import App_Logger
app_logger = App_Logger("../logs/load_data.log").get_app_logger()


def load_data(path: str):
    try:
        df = pd.read_csv(path)
    except BaseException:
        app_logger.warning('file not found or wrong file format')
    return df

def data_shape(df):
    print(f" There are {df.shape[0]} rows and {df.shape[1]} columns")

"""how many missing values exist or better still what is the % of missing values in the dataset?"""


def data_types(df):
    t = df.dtypes.value_counts()
    return t

def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The dataset contains", round(
        ((totalMissing/totalCells) * 100), 2), "%", "missing values.")

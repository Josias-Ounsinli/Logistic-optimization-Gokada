# from tkinter.filedialog import test
import unittest

import pandas as pd

import sys, os

sys.path.append(os.path.abspath(os.path.join("../scripts")))

import data_loader
# import preprocess

from logger_class import App_Logger
app_logger = App_Logger("../logs/tests.log").get_app_logger()


class TestGetInformations(unittest.TestCase):
    # def setUp(self):
    
    def test_load_data1(self):
       self.assertIsInstance(data_loader.load_data(
           '../data/nb.csv'),pd.DataFrame)
    
    def test_load_data2(self):
       self.assertIsInstance(data_loader.load_data(
           '../data/driver_locations_during_request.csv'),pd.DataFrame)
    
        
if __name__ == "__main__":
    unittest.main()
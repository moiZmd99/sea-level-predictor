import unittest
import pandas as pd
from sea_level_predictor import draw_plot

class TestSeaLevel(unittest.TestCase):
    def test_data_loaded(self):
        data = pd.read_csv("epa-sea-level.csv")
        self.assertTrue(len(data) > 0)

    def test_draw_plot_runs(self):
       
        draw_plot()

if __name__ == "__main__":
    unittest.main()

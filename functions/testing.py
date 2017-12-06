import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import shelve
import os
from itertools import combinations
from find_indices_with_value  import find_indices_with_value
from two_sample_t_test import two_sample_t_test


class MyTests(unittest.TestCase):

     #Test find_indices_with_value

    def test_multiple_missing_indices(self):
        row0 = [">", "", "!"]
        row1 = ["3", "1", "?"]
        row2 = ["?", "10", "hello"]
        row3 = ["my", "name", "is"]
        df = pd.DataFrame([row0, row1, row2, row3])
        missing = find_indices_with_value(df, "?")
        np.testing.assert_equal(missing, np.array([1, 2]))
    def test_no_missing_indices(self):
        row0 = [">", "", "!"]
        row1 = ["3", "1", "4"]
        row2 = ["6", "10", "hello"]
        row3 = ["my", "name", "is"]
        df = pd.DataFrame([row0, row1, row2, row3])
        missing = find_indices_with_value(df, "?")
        np.testing.assert_equal(missing, np.array([]))
        
    def test_one_missing_index(self):
        row0 = [">", "", "!"]
        row1 = ["3", "1", "4"]
        row2 = ["6", "10", "hello"]
        row3 = ["my", "name", "?"]
        df = pd.DataFrame([row0, row1, row2, row3])
        missing = find_indices_with_value(df, "?")
        np.testing.assert_equal(missing, np.array([3]))
        
    def test_multiple_missing_on_one_index(self):
        row0 = [">", "", "!"]
        row1 = ["3", "1", "4"]
        row2 = ["6", "10", "hello"]
        row3 = ["my", "?", "?"]
        df = pd.DataFrame([row0, row1, row2, row3])
        missing = find_indices_with_value(df, "?")
        np.testing.assert_equal(missing, np.array([3]))
        
    def test_multiple_missing_on_multiple_indices(self):
        row0 = [">", "", "!"]
        row1 = ["?", "?", "4"]
        row2 = ["6", "10", "hello"]
        row3 = ["my", "?", "?"]
        df = pd.DataFrame([row0, row1, row2, row3])
        missing = find_indices_with_value(df, "?")
        np.testing.assert_equal(missing, np.array([1, 3]))
        
        
    def test_one_row_df(self):
        row0 = [">", "?", "!"]
        df = pd.DataFrame([row0])
        missing = find_indices_with_value(df, "?")
        np.testing.assert_equal(missing, np.array([0]))

    # Test two-sample t-test

    def test_same_population(self):
        group1 = [1, 2, 3]
        group2 = group1
        t, p, reject = two_sample_t_test(group1, group2, "group1", "group2")
        self.assertAlmostEqual(0, t)
        self.assertAlmostEqual(1, p)
        self.assertTrue(not reject)
    def test_obvious_difference(self):
        group1 = [1, 2, 3]
        group2 = [1000, 1001, 1001]
        t, p, reject = two_sample_t_test(group1, group2, "group1", "group2")
        self.assertAlmostEqual(0, p)
        self.assertTrue(reject)
    def test_significance_level(self):
        t, p, reject = two_sample_t_test([1, 2, 3], [4,9, 5], "group1", "group2", 0.1)
        self.assertAlmostEqual(0.1, p, places = 1)
        self.assertTrue(reject)
        t, p, reject = two_sample_t_test([1, 2, 3], [4,9, 5], "group1", "group2")
        self.assertAlmostEqual(0.1, p, places = 1)
        self.assertTrue(not reject)
    def test_same_population_different_order(self):
        group1 = [1, 2, 4]
        group2 = [2, 4, 1]
        t, p, reject = two_sample_t_test(group1, group2, "group1", "group2")
        self.assertAlmostEqual(0, t)
        self.assertAlmostEqual(1, p)

unittest.main(argv=["foo"], exit = False, verbosity = 2)
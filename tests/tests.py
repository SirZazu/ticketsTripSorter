#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase

import sys

import os
sys.path.append(os.path.dirname(os.getcwd()))

from data import test_sort_data_1, test_sort_data_2, test_sort_data_3, test_sort_data_4, test_sort_data_5, \
    test_sort_data_6
from results import test_sort_result_1, test_sort_result_2, test_sort_result_3, test_sort_result_4, \
    test_sort_result_5, test_list_result
from main import TicketsTripSorter


class TestsTripSorter(TestCase):
    def setUp(self):
        self.ts = TicketsTripSorter()

    def test_simple_chain_travel(self):
        sorted_trip = self.ts._sort_list(test_sort_data_1)
        self.assertListEqual(test_sort_result_1, sorted_trip)

    def test_additional_europe_round(self):
        sorted_trip = self.ts._sort_list(test_sort_data_2)
        self.assertListEqual(test_sort_result_2, sorted_trip)

    def test_additional_route_after_start(self):
        sorted_trip = self.ts._sort_list(test_sort_data_3)
        self.assertListEqual(test_sort_result_3, sorted_trip)

    def test_additional_route_before_the_end(self):
        sorted_trip = self.ts._sort_list(test_sort_data_4)
        self.assertListEqual(test_sort_result_4, sorted_trip)

    def test_additional_route_from_first_city(self):
        sorted_trip = self.ts._sort_list(test_sort_data_5)
        self.assertListEqual(test_sort_result_5, sorted_trip)

    def test_error_no_start_or_end_city(self):
        sorted_trip = self.ts._sort_list(test_sort_data_6)
        self.assertEqual("Wrong list", sorted_trip)

    def test_convert_sorted_list_to_string(self):
        sorted_trip = self.ts.sort_trip_list(test_sort_data_1)
        self.assertListEqual(test_list_result, sorted_trip)


if __name__ == "__main__":
    unittest.main()

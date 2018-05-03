#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
__author__ = "Michał Uziak"
Algorithm for sorting travel cards and generate list of instructions for user.
Implementation of Euler circuit in graph (Hierholzer’s Algorithm)

"""

from dicts import INITIAL_WORDS_DICT


class TicketsTripSorter(object):
    def __init__(self):
        pass

    def _create_inctruction_list(self, trip_list):
        new_list = []
        for el in trip_list:

            initial_words = INITIAL_WORDS_DICT[el['transport_type']][:1].upper() + INITIAL_WORDS_DICT[
                                                                                       el['transport_type']][1:]

            transport_type_name = el['transport_type'] + " "
            transport_type_name += el['transport_name'] if 'transport_name' in el else ""

            if "transport_gate" in el:
                seat_string = "Gate " + el['transport_gate'] + ", seat " + el['seat']
            elif "seat" in el:
                seat_string = "Sit in sit " + el['seat']
            else:
                seat_string = " No seat assignment"
            end_word = "You have arrived at your final destination."

            info = el['info'] + "." if 'info' in el else ""
            helper_string = "{} {} from {} to {}. {}. {}".format(initial_words, transport_type_name, el['departure'],
                                                                 el['arrival'], seat_string, info)
            new_list.append(helper_string)
        new_list.append(end_word)

        return new_list

    def _create_initial_data(self, trips_list):
        # we need to count edges for every kind of city
        self.city_edges = {}
        for el in trips_list:
            if el['departure'] not in self.city_edges:
                self.city_edges[el['departure']] = [0, 0]
            if el['arrival'] not in self.city_edges:
                self.city_edges[el['arrival']] = [0, 0]
            self.city_edges[el['departure']][0] += 1
            self.city_edges[el['arrival']][1] += 1
        # find the start node and end node
        start_city = end_city = None
        for key, val in self.city_edges.items():
            if self.city_edges[key][0] == self.city_edges[key][1]:
                continue
            if self.city_edges[key][0] > self.city_edges[key][1]:
                start_city = key
                continue
            if self.city_edges[key][1] > self.city_edges[key][0]:
                end_city = key

        return start_city, end_city

    def _sort_list(self, trips_list):
        # create dict to have names of cities
        start_city, end_city = self._create_initial_data(trips_list)
        if not start_city or not end_city:
            return "Wrong list"

        current_path = []
        for idx, el in enumerate(trips_list):
            if el['departure'] == start_city:
                current_idx = idx
        # to calculate problem with Hierholzer’s Algorithm we need closed graph,
        # need to add the node from end to start
        trips_list.append({'departure': end_city, 'arrival': start_city, 'transport_type': None})
        self.city_edges[end_city][0] += 1
        current_path.append(trips_list[current_idx])
        current_city = trips_list[current_idx]["arrival"]
        next_city = ""
        final_result = []
        del trips_list[current_idx]
        while current_path:
            if self.city_edges[current_city][0] > 0:
                for idx, val in enumerate(trips_list):
                    if val['departure'] == current_city:
                        current_path.append(trips_list[idx])
                        next_city = val['arrival']
                        del trips_list[idx]
                        break
                self.city_edges[current_city][0] -= 1
                current_city = next_city
            else:
                helper_val = current_path.pop()
                final_result.append(helper_val)
                current_city = helper_val['departure']
        # we need to remove one extra element - now first element
        del final_result[0]

        return list(reversed(final_result))

    def sort_trip_list(self, list_to_sort):
        result_list = self._sort_list(list_to_sort.copy())
        if not isinstance(result_list, list):
            return result_list
        text_list = self._create_inctruction_list(result_list)
        return text_list

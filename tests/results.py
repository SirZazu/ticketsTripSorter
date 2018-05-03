#!/usr/bin/python3
# -*- coding: utf-8 -*-

test_sort_result_1 = [
    {'departure': 'Madrid', 'arrival': 'Barcelona', 'transport_type': 'train', 'transport_name': '78A', 'seat': '45B'},
    {'departure': 'Barcelona', 'arrival': 'Gerona Airport', 'transport_type': 'airport bus'},
    {'departure': 'Gerona Airport', 'arrival': 'Stockholm', 'transport_type': 'flight', 'transport_name': 'SK455',
     'transport_gate': '45', 'seat': '3A', 'info': 'Baggage drop at ticket counter 344'},
    {'departure': 'Stockholm', 'arrival': 'New York JFK', 'transport_type': 'flight', 'transport_name': 'SK22',
     'transport_gate': '22', 'seat': '7B', 'info': 'Baggage will we automatically transferred from your last leg'}
]

test_sort_result_2 = [
    {'departure': 'Madrid', 'arrival': 'Barcelona', 'transport_type': 'train', 'transport_name': '78A', 'seat': '45B'},
    {'departure': 'Barcelona', 'arrival': 'Gerona Airport', 'transport_type': 'airport bus'},
    {'departure': 'Gerona Airport', 'arrival': 'Warsaw', 'transport_type': 'flight', 'transport_name': 'SK455',
     'transport_gate': '45', 'seat': '3A', 'info': 'Baggage drop at ticket counter 344'},
    {'departure': 'Warsaw', 'arrival': 'Berlin', 'transport_type': 'flight', 'transport_name': 'SK455',
     'transport_gate': '45', 'seat': '3A', 'info': 'Baggage drop at ticket counter 344'},
    {'departure': 'Berlin', 'arrival': 'Gerona Airport', 'transport_type': 'flight', 'transport_name': 'SK455',
     'transport_gate': '45', 'seat': '3A', 'info': 'Baggage drop at ticket counter 344'},
    {'departure': 'Gerona Airport', 'arrival': 'Stockholm', 'transport_type': 'flight', 'transport_name': 'SK455',
     'transport_gate': '45', 'seat': '3A', 'info': 'Baggage drop at ticket counter 344'},
    {'departure': 'Stockholm', 'arrival': 'New York JFK', 'transport_type': 'flight', 'transport_name': 'SK22',
     'transport_gate': '22', 'seat': '7B', 'info': 'Baggage will we automatically transferred from your last leg'}]

test_sort_result_3 = [
    {'departure': 'Madrid', 'arrival': 'Barcelona', 'transport_type': 'train', 'transport_name': '78A', 'seat': '45B'},
    {'departure': 'Barcelona', 'arrival': 'Warsaw', 'transport_type': 'airport bus'},
    {'departure': 'Warsaw', 'arrival': 'Barcelona', 'transport_type': 'airport bus'},
    {'departure': 'Barcelona', 'arrival': 'Gerona Airport', 'transport_type': 'airport bus'},
    {'departure': 'Gerona Airport', 'arrival': 'Stockholm', 'transport_type': 'flight', 'transport_name': 'SK455',
     'transport_gate': '45', 'seat': '3A', 'info': 'Baggage drop at ticket counter 344'},
    {'departure': 'Stockholm', 'arrival': 'New York JFK', 'transport_type': 'flight', 'transport_name': 'SK22',
     'transport_gate': '22', 'seat': '7B', 'info': 'Baggage will we automatically transferred from your last leg'}]

test_sort_result_4 = [
    {'departure': 'Madrid', 'arrival': 'Barcelona', 'transport_type': 'train', 'transport_name': '78A', 'seat': '45B'},
    {'departure': 'Barcelona', 'arrival': 'Warsaw', 'transport_type': 'airport bus'},
    {'departure': 'Warsaw', 'arrival': 'Barcelona', 'transport_type': 'airport bus'},
    {'departure': 'Barcelona', 'arrival': 'Gerona Airport', 'transport_type': 'airport bus'},
    {'departure': 'Gerona Airport', 'arrival': 'Stockholm', 'transport_type': 'flight', 'transport_name': 'SK455',
     'transport_gate': '45', 'seat': '3A', 'info': 'Baggage drop at ticket counter 344'},
    {'departure': 'Stockholm', 'arrival': 'New York JFK', 'transport_type': 'flight', 'transport_name': 'SK22',
     'transport_gate': '22', 'seat': '7B', 'info': 'Baggage will we automatically transferred from your last leg'},
    {'departure': 'New York JFK', 'arrival': 'Paris', 'transport_type': 'flight', 'transport_name': 'SK22',
     'transport_gate': '22', 'seat': '7B', 'info': 'Baggage will we automatically transferred from your last leg'},
    {'departure': 'Paris', 'arrival': 'Moscow', 'transport_type': 'flight', 'transport_name': 'SK22',
     'transport_gate': '22', 'seat': '7B', 'info': 'Baggage will we automatically transferred from your last leg'},
    {'departure': 'Moscow', 'arrival': 'New York JFK', 'transport_type': 'flight', 'transport_name': 'SK22',
     'transport_gate': '22', 'seat': '7B', 'info': 'Baggage will we automatically transferred from your last leg'}]

test_sort_result_5 = [
    {'departure': 'Madrid', 'arrival': 'Warsaw', 'transport_type': 'train', 'transport_name': '78A', 'seat': '45B'},
    {'departure': 'Warsaw', 'arrival': 'Madrid', 'transport_type': 'train', 'transport_name': '78A', 'seat': '45B'},
    {'departure': 'Madrid', 'arrival': 'Barcelona', 'transport_type': 'train', 'transport_name': '78A', 'seat': '45B'},
    {'departure': 'Barcelona', 'arrival': 'Gerona Airport', 'transport_type': 'airport bus'},
    {'departure': 'Gerona Airport', 'arrival': 'Stockholm', 'transport_type': 'flight', 'transport_name': 'SK455',
     'transport_gate': '45', 'seat': '3A', 'info': 'Baggage drop at ticket counter 344'},
    {'departure': 'Stockholm', 'arrival': 'New York JFK', 'transport_type': 'flight', 'transport_name': 'SK22',
     'transport_gate': '22', 'seat': '7B', 'info': 'Baggage will we automatically transferred from your last leg'}]

test_list_result = ['Take train 78A from Madrid to Barcelona. Sit in sit 45B. ',
                    'Take the airport bus  from Barcelona to Gerona Airport.  No seat assignment. ',
                    'Take flight SK455 from Gerona Airport to Stockholm. Gate 45, seat 3A. Baggage drop at ticket '
                    'counter 344.',
                    'Take flight SK22 from Stockholm to New York JFK. Gate 22, seat 7B. Baggage will we automatically '
                    'transferred from your last leg.',
                    'You have arrived at your final destination.']

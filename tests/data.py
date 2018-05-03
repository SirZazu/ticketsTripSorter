#!/usr/bin/python3
# -*- coding: utf-8 -*-

test_sort_data_1 = [
    {
        "departure": "Barcelona",
        "arrival": "Gerona Airport",
        "transport_type": "airport bus"
    },
    {
        "departure": "Stockholm",
        "arrival": "New York JFK",
        "transport_type": "flight",
        "transport_name": "SK22",
        "transport_gate": "22",
        "seat": "7B",
        "info": "Baggage will we automatically transferred from your last leg"
    },
    {
        "departure": "Madrid",
        "arrival": "Barcelona",
        "transport_type": "train",
        "transport_name": "78A",
        "seat": "45B"
    },
    {
        "departure": "Gerona Airport",
        "arrival": "Stockholm",
        "transport_type": "flight",
        "transport_name": "SK455",
        "transport_gate": "45",
        "seat": "3A",
        "info": "Baggage drop at ticket counter 344"
    }
]

test_sort_data_2 = [
    {
        "departure": "Barcelona",
        "arrival": "Gerona Airport",
        "transport_type": "airport bus"
    },
    {
        "departure": "Stockholm",
        "arrival": "New York JFK",
        "transport_type": "flight",
        "transport_name": "SK22",
        "transport_gate": "22",
        "seat": "7B",
        "info": "Baggage will we automatically transferred from your last leg"
    },
    {
        "departure": "Madrid",
        "arrival": "Barcelona",
        "transport_type": "train",
        "transport_name": "78A",
        "seat": "45B"
    },
    {
        "departure": "Gerona Airport",
        "arrival": "Stockholm",
        "transport_type": "flight",
        "transport_name": "SK455",
        "transport_gate": "45",
        "seat": "3A",
        "info": "Baggage drop at ticket counter 344"
    },
    {
        "departure": "Gerona Airport",
        "arrival": "Warsaw",
        "transport_type": "flight",
        "transport_name": "SK455",
        "transport_gate": "45",
        "seat": "3A",
        "info": "Baggage drop at ticket counter 344"
    },
    {
        "departure": "Warsaw",
        "arrival": "Berlin",
        "transport_type": "flight",
        "transport_name": "SK455",
        "transport_gate": "45",
        "seat": "3A",
        "info": "Baggage drop at ticket counter 344"
    },
    {
        "departure": "Berlin",
        "arrival": "Gerona Airport",
        "transport_type": "flight",
        "transport_name": "SK455",
        "transport_gate": "45",
        "seat": "3A",
        "info": "Baggage drop at ticket counter 344"
    },
]

test_sort_data_3 = [
    {
        "departure": "Barcelona",
        "arrival": "Gerona Airport",
        "transport_type": "airport bus"
    },
    {
        "departure": "Barcelona",
        "arrival": "Warsaw",
        "transport_type": "airport bus"
    },
    {
        "departure": "Warsaw",
        "arrival": "Barcelona",
        "transport_type": "airport bus"
    },
    {
        "departure": "Stockholm",
        "arrival": "New York JFK",
        "transport_type": "flight",
        "transport_name": "SK22",
        "transport_gate": "22",
        "seat": "7B",
        "info": "Baggage will we automatically transferred from your last leg"
    },
    {
        "departure": "Madrid",
        "arrival": "Barcelona",
        "transport_type": "train",
        "transport_name": "78A",
        "seat": "45B"
    },
    {
        "departure": "Gerona Airport",
        "arrival": "Stockholm",
        "transport_type": "flight",
        "transport_name": "SK455",
        "transport_gate": "45",
        "seat": "3A",
        "info": "Baggage drop at ticket counter 344"
    }
]

test_sort_data_4 = [
    {
        "departure": "Barcelona",
        "arrival": "Gerona Airport",
        "transport_type": "airport bus"
    },
    {
        "departure": "Barcelona",
        "arrival": "Warsaw",
        "transport_type": "airport bus"
    },
    {
        "departure": "Warsaw",
        "arrival": "Barcelona",
        "transport_type": "airport bus"
    },
    {
        "departure": "Stockholm",
        "arrival": "New York JFK",
        "transport_type": "flight",
        "transport_name": "SK22",
        "transport_gate": "22",
        "seat": "7B",
        "info": "Baggage will we automatically transferred from your last leg"
    },
    {
        "departure": "New York JFK",
        "arrival": "Paris",
        "transport_type": "flight",
        "transport_name": "SK22",
        "transport_gate": "22",
        "seat": "7B",
        "info": "Baggage will we automatically transferred from your last leg"
    },
    {
        "departure": "Paris",
        "arrival": "Moscow",
        "transport_type": "flight",
        "transport_name": "SK22",
        "transport_gate": "22",
        "seat": "7B",
        "info": "Baggage will we automatically transferred from your last leg"
    },
    {
        "departure": "Moscow",
        "arrival": "New York JFK",
        "transport_type": "flight",
        "transport_name": "SK22",
        "transport_gate": "22",
        "seat": "7B",
        "info": "Baggage will we automatically transferred from your last leg"
    },
    {
        "departure": "Madrid",
        "arrival": "Barcelona",
        "transport_type": "train",
        "transport_name": "78A",
        "seat": "45B"
    },
    {
        "departure": "Gerona Airport",
        "arrival": "Stockholm",
        "transport_type": "flight",
        "transport_name": "SK455",
        "transport_gate": "45",
        "seat": "3A",
        "info": "Baggage drop at ticket counter 344"
    }
]

test_sort_data_5 = [
    {
        "departure": "Barcelona",
        "arrival": "Gerona Airport",
        "transport_type": "airport bus"
    },
    {
        "departure": "Stockholm",
        "arrival": "New York JFK",
        "transport_type": "flight",
        "transport_name": "SK22",
        "transport_gate": "22",
        "seat": "7B",
        "info": "Baggage will we automatically transferred from your last leg"
    },
    {
        "departure": "Madrid",
        "arrival": "Barcelona",
        "transport_type": "train",
        "transport_name": "78A",
        "seat": "45B"
    },
    {
        "departure": "Gerona Airport",
        "arrival": "Stockholm",
        "transport_type": "flight",
        "transport_name": "SK455",
        "transport_gate": "45",
        "seat": "3A",
        "info": "Baggage drop at ticket counter 344"
    },
    {
        "departure": "Madrid",
        "arrival": "Warsaw",
        "transport_type": "train",
        "transport_name": "78A",
        "seat": "45B"
    },
    {
        "departure": "Warsaw",
        "arrival": "Madrid",
        "transport_type": "train",
        "transport_name": "78A",
        "seat": "45B"
    },
]

test_sort_data_6 = [
    {
        "departure": "Madrid",
        "arrival": "Barcelona",
        "transport_type": "train",
        "transport_name": "78A",
        "seat": "45B"
    },
    {
        "departure": "Barcelona",
        "arrival": "Madrid",
        "transport_type": "train",
        "transport_name": "78A",
        "seat": "45B"
    },
]

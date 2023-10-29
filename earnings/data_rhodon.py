import util

RHODON_DATA = [
    {"date": "2023-09-20", "gains": 2.61, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-09-21", "gains": 2.64, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-09-23", "gains": 2.84, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-09-25", "gains": 2.32, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-09-27", "gains": 2.67, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-09-29", "gains": 2.79, "time_minutes": 83, "name": "Rhodon"},
    {"date": "2023-10-01", "gains": 1.62, "time_minutes": 56, "name": "Rhodon"},
    {"date": "2023-10-02", "gains": 2.49, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-04", "gains": 2.12, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-05", "gains": 1.99, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-07", "gains": 2.48, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-09", "gains": 2.84, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-11", "gains": 2.75, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-12", "gains": 2.71, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-14", "gains": 1.37, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-16", "gains": 2.84, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-18", "gains": 2.56, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-19", "gains": 2.42, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-21", "gains": 3.01, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-23", "gains": 2.80, "time_minutes": 30, "name": "Rhodon"},
]

RHODON_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in RHODON_DATA]

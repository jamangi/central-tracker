import util

RHODON_DATA = [
    {"date": "2023-10-21", "gains": 3.01, "time_minutes": 30, "name": "Rhodon"},
    {"date": "2023-10-23", "gains": 2.80, "time_minutes": 30, "name": "Rhodon"},
]

RHODON_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in RHODON_DATA]

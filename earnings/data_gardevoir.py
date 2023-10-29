import util

GARDEVOIR_DATA = [
    {"date": "2023-10-21", "gains": 3.01, "time_minutes": 30, "name": "Gardevoir"},
    {"date": "2023-10-23", "gains": 2.80, "time_minutes": 30, "name": "Gardevoir"},
]

GARDEVOIR_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in GARDEVOIR_DATA]

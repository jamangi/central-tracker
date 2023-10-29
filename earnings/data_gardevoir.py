import util

GARDEVOIR_DATA = [
    {"date": "2023-10-29", "gains": 3.01, "time_minutes": 60, "name": "Gardevoir"},
]

GARDEVOIR_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in GARDEVOIR_DATA]

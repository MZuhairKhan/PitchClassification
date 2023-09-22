import pybaseball
pybaseball.cache.enable()
data = statcast(start_dt="2022-05-07", end_dt="2022-11-05").columns
print(data.columns)
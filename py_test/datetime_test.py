#! usr/bin/env python
from datetime import datetime

st = "00:00:00"
et = "00:00:10"
st_time = datetime.strptime(st, '%H:%M:%S')
et_time = datetime.strptime(et, '%H:%M:%S')
type(st_time)
type(et_time)

print(st_time)
print(et_time)
print((et_time - st_time).seconds)

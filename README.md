# binsearch

Get results for exam scores

```
from binsearch import BinSearch

grade = BinSearch([(85,"A"), (75,"B"), (65,"C"), (55,"D"), (0,"E")], sort=True)
for point in [54,55,64,65,74,75,84,85]:
    print('{} - {}'.format(point, grade.find(point)))
```

```
from binsearch import BinSearch

grade = BinSearch({85:"A", 75:"B", 65:"C", 55:"D", 0:"E"})
for point in [54,55,64,65,74,75,84,85]:
    print('{} - {}'.format(point, grade.find(point)))
```

Convert date into Japan era (Gengou) format

```
from binsearch import BinSearch
from datetime import date

japanera = BinSearch([
    (date(1868, 9, 8), "明治"),
    (date(1912, 7,30), "大正"),
    (date(1926,12,25), "昭和"),
    (date(1989, 1, 8), "平成"),
    (date(2019, 7, 1), "令和"),
])
for d in [
    date(1912, 7,29),
    date(1912, 7,30),
    date(1926,12,24),
    date(1926,12,25),
    date(1989, 1, 7),
    date(1989, 1, 8),
    date(2019, 6,30),
    date(2019, 7, 1),
]:
    orig, era = japanera.find(d)
    print('{}{}年{}月{}日'.format(era, '元' if d.year == orig.year else d.year-orig.year+1, d.month, d.day))
```

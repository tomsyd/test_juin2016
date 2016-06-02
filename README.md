# test_juin2016

First exercice:
---------------

```
> python test1.py fileName
```

* bookings.csv: 10000011 lines
* searches.csv: 20390199 lines

Second exercice:
----------------

The airport names are displayed in the output:

```
> python test2.py bookings.csv
London Heathrow Airport 88809.0
Orlando International Airport 70930.0
Los Angeles International Airport 70530.0
Mc Carran International Airport 69630.0
John F Kennedy International Airport 66270.0
Paris - Charles-de-Gaulle 64490.0
Suvarnabhumi 59460.0
Miami International Airport 58150.0
San Francisco International Airport 58000.0
Dubai International Airport 55590.0
```

Third exercice:
---------------

We check the 3 Spain cities: MAD, AGP and BCN.

```
> geo.get('MAD','name')
Out[32]: 'Madrid / Barajas'

> geo.get('AGP','name')
Out[35]: 'M\xc3\xa1laga Airport'

> geo.get('BCN','name')
Out[36]: 'Barcelona\xe2\x80\x93El Prat Airport'
```

```
> python test3.py searchFile
```

For the moment, there are several problems in the script:

1. it does not convert Year-Month to datetime (so the plot is really ugly)
2. there are 2 warnings to fix

Bonus exercice 2: write a web service:
--------------------------------------

First step: generate a csv file containing all (sorted) data from the second exercice:

```
> python b2_data_from_test2.py bookings.csv
> python test1.py test2_result.csv
```

* test2_result.csv: 2275 lines
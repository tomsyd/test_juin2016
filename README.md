# test_juin2016

First exercise:
---------------

```
> python test1.py bookings.csv
> python test1.py searches.csv
```

* bookings.csv: 10000011 lines
* searches.csv: 20390199 lines

Second exercise:
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

Third exercise:
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
> python test3.py searches.csv
```

For the moment, there are several problems in the script:

1. it does not convert Year-Month to datetime (so the plot is really ugly)
2. there are 2 warnings to fix

Bonus exercise 2: write a web service:
--------------------------------------

First step: generate a csv file containing all (sorted) data from the second exercise:

```
> python b2_data_from_test2.py bookings.csv
> python test1.py test2_result.csv
```

* test2_result.csv: 2275 lines

Second step: to start the web service:

```
> python b2.py
```

Example: web link to retrieve the top 12 airports.

* http://localhost:8080/airports/12

Bonus exercise 1: match serach with bookings:
---------------------------------------------

First step: reduce the bookings file as small as possible. We will just keep thos columns useful for the search identification:

* pos_oid: to identify the point of sales office id
* dep_port: origin
* arr_port: destination
* cre_date: creation date should be the same or one day after the search date - to simplify, let's say the same day here
* brd_time: bording day of the flight

```
> python b1_data_from_bookings.py bookings.csv
```

The above command will generate a new file called bkg4b1.csv which will contain only the cited 5 columns.

The reason here is to get a file of small size for our use (940M instead of 4.1G).

So potentially we could hope to keep this file in memory for our next step.
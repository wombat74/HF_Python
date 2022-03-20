from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

# dests = set(flights.values())
# print(dests)

# West_End_Times = [k for k, v in flights.items() if v == 'WEST END']
# print(West_End_Times)

# for dest in set(flights.values()):
#     print(dest, '->', [k for k, v in flights.items() if v == dest])

when = {}
for dest in set(flights.values()):
    when[dest] = [k for k, v in flights.items() if v == dest]

pprint.pprint(when)
print()

when2 = {dest: [k for k, v in flights.items() if v == dest] for dest in set(flights.values())}
pprint.pprint(when2)

# flights2 = {}

# for k, v in flights.items():
#     flights2[convert2ampm(k)] = v.title()

# more_flights = {convert2ampm(k): v.title() 
#                 for k, v in flights.items() 
#                 if v == 'FREEPORT'}

# pprint.pprint(more_flights)
# print()

# flight_times = []
# for ft in flights.keys():
#     flight_times.append(convert2ampm(ft))

# print(flight_times)
# print()

# destinations = []
# for dest in flights.values():
#     destinations.append(dest.title())

# print(destinations)
# print()

# more_dests = [dest.title() for dest in flights.values()]
# print(more_dests)
# print()

# more_flights = [convert2ampm(ft) for ft in flights.keys()]
# print(more_flights)
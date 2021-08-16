import json
from dataclasses import dataclass
import requests


@dataclass
class Route:
    name: str
    departure_time: str


def get_routes_available_pretty(station):
    routes = get_routes_available_full(station)
    for i, r in enumerate(routes):
        print(f'{i}. {str(r).capitalize()}')


def get_routes_available_full(station):
    routes = []
    json_resp = requests.get(f'http://myttc.ca/{station[0]}.json').json()
    for r in json_resp['stops']:
        for s in r['routes']:
            routes.append(s["name"])
    return routes


def get_route_options_pretty(route_list):
    route_name = route_list[0]
    station_name = route_list[1]
    route_options = get_route_options_from_route_station(route_name, station_name)
    for i, ro in enumerate(route_options):
        print(f"Route {ro.name[0:3]},Option #{i} | Name: {ro.name.capitalize()} | Next Departure: {ro.departure_time.capitalize()}")


def get_route_options_from_route_station(route_name, station):
    route_name = route_name.replace("_", " ")
    print(route_name)
    print(station)
    departures_list = []
    json_resp = requests.get(f'http://myttc.ca/{station}.json').json()
    data = json.dumps(json_resp)
    for r in json_resp['stops']:
        for s in r['routes']:
            if s["name"] == route_name.title():
                for departures in s['stop_times']:
                    r = Route(departures['shape'], departures['departure_time'])
                    departures_list.append(r)
            return departures_list


def get_routes_near(street_a, street_b):
    json_resp = requests.get(f'http://myttc.ca/near/{street_a}_and_{street_b}.json').json()
    data = json.dumps(json_resp)
    print(data)


def get_json_response_station(station):
    pass


class TTCService:

    def __init__(self):
        pass


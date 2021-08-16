import ttc_service
import argparse


if __name__ == '__main__':
    # Examples
    # print(ttc_service.get_routes_station_full_json("finch_station"))
    # ttc_service.get_route_options_pretty(["510_spadina", "union_station"])
    ttc_service.get_route_options_pretty(["5erast", "finch_station"])

    # ttc_service.get_routes_near("steeles", "bathurst")
    parser = argparse.ArgumentParser(description="Command line tool to find bus and subway routes for the Toronto "
                                                 "Transit Commission")
    parser.add_argument('-s', '--station', metavar="<station>", type=str, nargs=1,
                        help="Get list of routes departing from supplied --station 's'")
    parser.add_argument('-r', '--route', metavar=("<route>", "<station>"), type=str, nargs=2,
                        help="The name of the route and the station: '52_steeles_west' 'finch_station'")
    args = parser.parse_args()

    if args.station:
        ttc_service.get_routes_available_pretty(args.station)

    if args.route:
        ttc_service.get_route_options_pretty(args.route)



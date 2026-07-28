capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

travel_log = {
    "France": ["Paris","Lille","Dijon" ],
    "Germany": ["Berlin","Hamburg","Stuttgart" ],
    "Japan": ["Tokyo","Kyoto","Osaka" ]
}

#print Lille
print(travel_log["France"][1]);

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][0])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 6,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
}

#print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
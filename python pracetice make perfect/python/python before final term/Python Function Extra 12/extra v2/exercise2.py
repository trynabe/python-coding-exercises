city_country = {
    "bangkok": "thailand",
    "tokyo": "japan",
    "osaka": "japan",
    "paris": "france",
    "lyon": "france",
    "ottawa": "canada"
}

country_continent = {
    "thailand": "asia",
    "japan": "asia",
    "france": "europe",
    "canada": "north_america"
}

def count_city(city_country, country_continent):
    result = {}

    for city, country in city_country.items():
        cont = country_continent[country]

        if cont not in result:
            result[cont] = 0
        result[cont] += 1

    return dict(sorted(result.items()))

print(count_city(city_country, country_continent))
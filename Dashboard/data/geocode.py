import requests

url_geo = "https://nominatim.openstreetmap.org/search"

def find_sede(sede):
    city = sede.split(',')
    c= city[1]
    query= {
        "q":c,
        "format":"json"

    }
    print(query)
    results = requests.get(url_geo, params = query).json()[0]
    print(results)
    return list(map(float,[results["lon"],results["lat"]]))
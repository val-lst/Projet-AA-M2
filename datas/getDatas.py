import urllib.request, json

with urllib.request.urlopen("https://overpass-api.de/api/interpreter?data=%2F*%5Bout%3Ajson%5D%3B%0Aarea%5Bname%20%3D%20%22France%22%5D%3B%0A%28way%28area%29%5B%22highway%22~%22%5E%28services%7Crest_area%29%24%22%5D%3B%3E%3B%29%3B%0Aout%3B*%2F%0A%0A%0A%5Bout%3Ajson%5D%3B%0Aarea%5Bname%20%3D%20%22Gironde%22%5D%3B%0A%28way%28area%29%5B%22highway%22~%22%5E%28motorway%7Ctrunk%7Cservices%7Crest_area%7Cmotorway_link%7Ctrunk_link%29%24%22%5D%3B%3E%3B%29%3B%0Aout%3B") as url:
    data = json.loads(url.read().decode())

    output_file = "datas/gironde.json"

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
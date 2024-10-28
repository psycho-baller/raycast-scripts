import json


def clean_geojson(data):
    cleaned_data = []
    for feature in data["features"]:
        properties = feature["properties"]
        geometry = feature["geometry"]
        cleaned_feature = {
            "id": properties["datasource"]["raw"]["osm_id"],
            "name": properties.get("name", properties.get("address_line1", None)),
            "lon": geometry["coordinates"][0],
            "lat": geometry["coordinates"][1],
            "categories": properties["categories"] if properties["categories"] else [],
        }
        if cleaned_feature["name"] is None:
            continue
        cleaned_data.append(cleaned_feature)
    return cleaned_data


data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "Calgary Technologies Inc",
                "country": "Canada",
                "country_code": "ca",
                "state": "Alberta",
                "city": "Calgary",
                "postcode": "T2L 2A4",
                "suburb": "Brentwood",
                "street": "31 Street NW",
                "lon": -114.13060901707867,
                "lat": 51.08427535,
                "state_code": "AB",
                "formatted": "Calgary Technologies Inc, 31 Street NW, Calgary, AB T2L 2A4, Canada",
                "address_line1": "Calgary Technologies Inc",
                "address_line2": "31 Street NW, Calgary, AB T2L 2A4, Canada",
                "categories": ["building"],
                "details": [],
                "datasource": {
                    "sourcename": "openstreetmap",
                    "attribution": "© OpenStreetMap contributors",
                    "license": "Open Database License",
                    "url": "https://www.openstreetmap.org/copyright",
                    "raw": {
                        "name": "Calgary Technologies Inc",
                        "osm_id": 23647427,
                        "building": "yes",
                        "osm_type": "w",
                    },
                },
                "place_id": "51983aece55b885cc0597369de88c98a4940f00102f901c3d468010000000092031843616c6761727920546563686e6f6c6f6769657320496e63",
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-114.13060901707865, 51.08427534923512],
            },
        },
        # ...
    ],
}

print(json.dumps(clean_geojson(data), indent=2))

from ..credentials import metro_apikey
from ..g_translate import translate
import requests


def metro_api(y, x, radius_m=1000):
    stations = get_nearests_stations(y, x, radius_m=radius_m)
    for s in stations:
        if 'odpt:railway' not in s:
            print(s)
            raise
    railways = [s['odpt:railway'] for s in stations]
    railways_status = get_train_status(railways)
    status_text_jp = [railways_status[s['odpt:railway']] for s in stations]
    status_text_en_dict = {jp: en for jp, en in zip(
        status_text_jp, translate(status_text_jp))}
    output_stations = []
    for s in stations:
        output_station = {}
        output_station['station'] = s['dc:title']
        output_station['station_en'] = s['owl:sameAs'].split('.')[-1]
        output_station['station_code'] = s['odpt:stationCode']
        output_station['railway_en'] = s['odpt:railway'].split('.')[-1]
        output_station['status'] = railways_status[s['odpt:railway']]
        output_station['status_en'] = status_text_en_dict[output_station['status']]
        output_stations.append(output_station)
    return output_stations
    # print(stations)


def get_nearests_stations(y, x, radius_m=1000):
    url = f"https://api.tokyometroapp.jp/api/v2/places?rdf:type=odpt:Station&lon={x}&lat={y}&radius={radius_m}&acl:consumerKey={metro_apikey}"
    stations = requests.get(url).json()
    # print(stations)
    # print(stations[0])
    stations = [
        {k: station.get(k, None) for k in
         ['dc:title', 'odpt:stationCode', 'owl:sameAs',
          'odpt:railway']
         }
        for station in stations]
    return stations


def get_train_status(railways):
    url = f"https://api.tokyometroapp.jp/api/v2/datapoints?rdf:type=odpt:TrainInformation&acl:consumerKey={metro_apikey}"
    json = requests.get(url).json()
    json = {x['odpt:railway']: x['odpt:trainInformationText']
            for x in json if x['odpt:railway'] in railways}
    return json


if __name__ == '__main__':
    import pprint
    # pprint.pprint(get_nearests_stations(35.6340074, 139.7135059, 2000))
    # pprint.pprint(get_train_status(['odpt.Railway:TokyoMetro.Namboku', ]))
    metro_api(35.6340074, 139.7135059, 2000)

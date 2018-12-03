from ..credentials import hotpper_apikey
from ..g_translate import translate
import requests

# TODO: working hour?
# TODO: cashe translate result


def hotpper_api(y, x):
    """
    wrap with func translate
    """
    shops = hotpper_api_raw(y, x)
    jp_keys = ['catch', 'genre', 'name', 'budget']
    all_texts = []
    for shop in shops:
        shop_texts = [shop.get(k, '') for k in jp_keys]
        all_texts.extend(shop_texts)
    all_texts_en = translate(all_texts)
    i = 0
    for shop in shops:
        for jp_key in jp_keys:
            shop[jp_key + '_en'] = all_texts_en[i]
            i += 1
    return shops


def hotpper_api_raw(y, x):
    """lat(=35) is y, lng(=135) is x"""
    url = f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={hotpper_apikey}&format=json&lat={y}&lng={x}"
    json = requests.get(url).json()
    raw_shops = json['results']['shop']
    """
    pprint.pprint(raw_shops[0]) #if you wanna see full json
    """
    shops = []
    for raw_shop in raw_shops:
        r = raw_shop
        shop = {k: v for k, v in raw_shop.items() if k in [
            'name', 'catch', 'lat', 'lng', 'logo_image', 'open', 'address']}
        shop['genre'] = shop.get('genre', '') + '　' + \
            raw_shop.get('genre', {}).get('name', '')
        shop['genre'] = shop.get('genre', '') + '　' + \
            raw_shop.get('genre', {}).get('name', '')
        shop['catch'] = shop.get('catch', '') + '　' + \
            raw_shop.get('genre', {}).get('catch', '')
        shop['url'] = raw_shop.get('urls', {}).get('pc', '')
        shop['photos'] = raw_shop.get('photo', {}).get('pc', '')
        shop['budget'] = raw_shop.get('budget', {}).get('average', '') + \
            '　' + raw_shop.get('budget', {}).get('name', '')
        shops.append(shop)
    return shops


if __name__ == '__main__':
    meguro_station_pos = (35.6340074, 139.7135059)
    import pprint
    pprint.pprint(hotpper_api(*meguro_station_pos))

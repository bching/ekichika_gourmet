from g_translate import translate
from metro import metro_api
from hotpper import hotpper_api

"""
目黒駅 is @35.6340074,139.7135059
args are named 'y' and 'x' ('y' comes first)
(https://www.google.com/maps/search/%E7%9B%AE%E9%BB%92%E9%A7%85/@35.6340074,139.7135059,17z/data=!3m1!4b1)
"""

if __name__ == '__main__':
    """args must be float"""
    import pprint
    pprint.pprint(metro_api(35.6340074, 139.7135059))
    pprint.pprint(hotpper_api(35.6340074, 139.7135059))

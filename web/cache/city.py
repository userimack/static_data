from django_redis import get_redis_connection
from web.cache import destination

def __pipeline():
    conn = get_redis_connection("default")
    return conn.pipeline()

def __process_city(item):
    print(item)
    return item.decode("utf-8").split("\t")[1:]

def __city_dict(item):
    city_data = item.decode("utf-8").split("\t")
    res = dict()
    res['code'] = city_data[0]
    res['name'] = city_data[1]
    res['country'] = city_data[3]
    res['dest_code'] = city_data[2]
    dest = destination.get(city_data[2])
    res['dest_name'] = dest[0]['name']
    return res

def search(city):
    city = city.lower() if city else ""
    conn = get_redis_connection("default")
    result = conn.zrangebylex("[m]city.name", "["+city, "["+city+"\xff")
    return [__process_city(item) for item in result]

def get(code):
    conn = get_redis_connection("default")
    result = conn.zrangebylex("[m]city", "[" + code + "\t", "[" + code + "\t\xff", 0, 1)
    return [__city_dict(item) for item in result]

def get_list(codes):
    codes = list(set(codes))
    pipe = __pipeline()
    for code in codes:
        pipe.zrangebylex("[m]city", "[" + code + "\t", "[" + code + "\t\xff", 0, 1)
    result = pipe.execute()
    print(result)
    final_result = []
    for city_data in result:
        city_result = [__city_dict(item) for item in city_data]  
        final_result.extend(city_result)
    return final_result

def get_supp_mapping(code):
    pass

def get_grn_mapping(code):
    pass
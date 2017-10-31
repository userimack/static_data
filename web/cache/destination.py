from django_redis import get_redis_connection


def __pipeline():
    conn = get_redis_connection("default")
    return conn.pipeline()

def __process_dest(item):
    return item.decode("utf-8").split("\t")[1:]

def __dest_dict(item):
    dest_data = item.decode("utf-8").split("\t")
    res = dict()
    res['code'] = dest_data[0]
    res['name'] = dest_data[1]
    res['country'] = dest_data[2]
    return res

def search(query):
    query = query.lower() if dest else ""
    conn = get_redis_connection("default")
    result = conn.zrangebylex("[m]destination.name", "["+query, "["+query+"\xff")
    return [__process_dest(item) for item in result]

def get(code):
    conn = get_redis_connection("default")
    result = conn.zrangebylex("[m]destination", "[" + code + "\t", "[" + code + "\t\xff", 0, 1)
    return [__dest_dict(item) for item in result]

def get_list(codes):
    pipe = pipeline()
    for code in codes:
        pipe.zrangebylex("[m]destination", "[" + code + "\t", "[" + code + "\t\xff", 0, 1)
    result = pipe.execute()
    return [__dest_dict(item) for item in result]

def get_supp_mapping(code):
    pass

def get_grn_mapping(code):
    pass
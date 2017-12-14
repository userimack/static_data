import re
from web.cache import city


def senitize(data):
    return re.sub('[^A-Za-z\.\,]+', ' ', data).strip()


def process_city_mappings(city_name):
    results = city.search(city_name)

    if results: return results
    results = city.search(city_name.replace(" ", ""))
    if results: return results

    d = city_name.split()

    if len(d) <= 1:
        return results

    for item in d:
        if len(item) > 3:
            fin_results = process_city_mappings(item)
            results.extend(fin_results)
    return results


def process_city(city_mapping):
    city_name_data = city_mapping.supp_city_name.split(",")
    city_name_data = [senitize(city_name) for city_name in city_name_data]
    results = []
    for city_name in city_name_data:
        results.extend(process_city_mappings(city_name))
    city_codes = [item[0] for item in results]
    # final_result = city.get_list(city_codes)
    return city.get_list(city_codes)
    # return sorted(final_result, key=lambda k: k['country'])

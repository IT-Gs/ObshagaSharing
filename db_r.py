_requests = {
    {
        'name': 'pan for pancakes',
        'condition': 'clean, non-stick',
        'time': '2 weeks',
        'benefits': '10 pancakes'
    },
    {
        'name': 'hair dryer',
        'condition': 'three speeds, cold and hot airflow',
        'time': 'until 25 november',
        'benefits': '2 sweets milka'
    },
    {
        'name': 'laptop',
        'condition': '--',
        'time': '2 weeks',
        'benefits': '10 pancakes',
    },
    {
        'name': 'nude shoes, heels ',
        'condition': 'new, 38size',
        'time': '27 nov',
        'benefits': '500 rub',
    },
    {
        'name': 'shoe dryer',
        'condition': 'clean',
        'time': '1 week',
        'benefits': 'lays and orange juice',
    },
    {
        'name': 'mirror',
        'condition': 'around 1 meters, clean',
        'time': '3 weeks',
        'benefits': '700rub',
    },
    {
        'name': 'Bakeware',
        'condition': 'cute',
        'time': '1 week',
        'benefits': '5 cakes',
    },
    {
        'name': 'charging on iphone',
        'condition': '--',
        'time': 'until 22 nov',
        'benefits': '100rub and chocolate',
    },
    {
        'name': 'outlet extension',
        'condition': '--',
        'time': 'until friday',
        'benefits': 'chocolate',
    },
    {
        'name': 'fash drive',
        'condition': 'free 1gb',
        'time': '1 weeks',
        'benefits': '200rub'
    }
}


_request_list = []

for name, request_data in _requests.items():
    _new_element = {'name': name}
    _new_element.update(request_data)
    _request_list.append(_new_element)


# Get request filtered by name
def get_requests_by_name(q):
    results = []
    # SEARCH

    for request in _request_list:
       if request['name'].lower() .find(q.lower()) >=0:
            results.append(request)

    return results


def get_request(itemname):
    return _requests.get(itemname)


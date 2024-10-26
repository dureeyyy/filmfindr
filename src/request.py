from _movie import Movie

def send_request(url : str, apikey : str, query: str):

    key = query.split(' : ', 1)
    value = query.split(' : ', 2)
    print(query)
    print(f'Key : {key[0]}, value : {value[1]}')

    params = {
        'apikey' : apikey,
        key[0] : value[1]
        }
    
    print(params)

    request = httpx.get(url, params=params)
    print(request.url)

    print(request.json())

    return request.json()

def handle_response(json_response : any):

    # json_parse = json.loads(json_response)
    print(f'JSON : {json_response}')

    movie = Movie ()

    movie.set_title(json_response['Title'])
    movie.set_year(json_response['Year'])
    movie.set_rated(json_response['Rated'])
    movie.set_genre(json_response['Genre'])
    movie.set_poster(json_response['Poster'])
    movie.set_plot(json_response['Plot'])
    movie.set_director(json_response['Director'])
    movie.set_actors(json_response['Actors'])
    movie.set_writers(json_response['Writer'])
    
    return movie
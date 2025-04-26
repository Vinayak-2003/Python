import requests, time

start = time.time()

url = "https://pokeapi.co/api/v2/pokemon/"
resp = requests.get(url)
print(resp.status_code)

end = time.time()



print("Total time: ", (end-start))
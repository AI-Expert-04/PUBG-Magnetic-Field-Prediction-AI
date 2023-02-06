import requests

url = "https://api.pubg.com/shards/steam/matches/b7e8d783-bb0c-4608-bd4f-b15d55f00d57"

header = {
  "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MzkzYTNiMC03ZWM0LTAxM2ItNGU0Ni0wYjMxMjcwM2U2NjYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjc0NjQwNTAzLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctbWFnbmV0aWMtIn0.tkl8OUjhe8ZUQ4rjEIE2PepLhccIU75wtgZozCnHfoM",
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)

player_dataitgirls_json = r.json()
print(player_dataitgirls_json)

from requests import get
from pprint import PrettyPrinter

printer = PrettyPrinter()
BASE_URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_btqZsSyTVT0qZYGkcCb6C80301XnO11Y1xzkYulZ"
API_KEY = "fca_live_btqZsSyTVT0qZYGkcCb6C80301XnO11Y1xzkYulZ"

r = get(BASE_URL)
data = r.json()
print(data)
# printer.pprint(data)

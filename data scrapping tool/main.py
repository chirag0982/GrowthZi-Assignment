from src.gmaps import Gmaps



queries = [
   "malls in pune"
]

Gmaps.places(queries,max=5)
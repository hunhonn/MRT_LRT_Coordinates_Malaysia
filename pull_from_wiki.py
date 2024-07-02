import pandas as pd
import googlemaps
key="ADD_API_KEY"
#function to geocode
def get_coordinates(address):
    try:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            return None, None
    except Exception as e:
        print(f"Error fetching coordinates {address}: {e}")
        return None, None

gmaps = googlemaps.Client(key=key)
url="https://en.wikipedia.org/wiki/List_of_rail_transit_stations_in_the_Klang_Valley_area"

list_of_tables=pd.read_html(url)

MRT=list_of_tables[7]

MRT_Kajang=MRT[1:30]

MRT_Kajang['geocode_name']='MRT Station ' + MRT_Kajang["Station Name"]
MRT_Kajang[['Latitude', 'Longitude']] = MRT_Kajang['geocode_name'].apply(
    lambda x: pd.Series(get_coordinates(x))
)

MRT_Kajang.to_csv("stationsMRTKajangLine.csv",index=False)
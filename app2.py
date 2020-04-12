import folium 
import pandas
import json
import io

data_json =  io.open('world.json','r',encoding='utf-8-sig').read()

df = pandas.read_csv('Volcanoes.txt')

map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=4,tiles='Mapbox bright')



def color(elev):
  if elev in range(0,1000):
    col='green'
  elif elev in range(1000,3000):
    col='orange'
  else:
    col='red'
  return col

fg=folium.FeatureGroup(name="Volcano Locations")

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
  fg.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium
  .Icon(icon_color=color(elev))))

map.add_child(fg)

map.add_child(folium.GeoJson(data=data_json,
 name="World Population",
 style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000\
   else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(folium.LayerControl())


map.save('test2.html')
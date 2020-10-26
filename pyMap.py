import folium

#In the terminal --- dir(folium), help(folium.Map)

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright") #map object with location of longitude/latitude, with zoom

#Adding a marker to show current location
fg = folium.FeatureGroup(name="My Map")
#
# fg.add_child(folium.Marker(location=[38.58, -99.09], popup="Hi I am here", icon=folium.Icon(color="red")))

#adding multiple marker
for coordinates in [[38.58, -99.09],[39.58, -97.09]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am here", icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("pyMap.html") #Saves the python map object into an html file
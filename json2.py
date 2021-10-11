import json

infile = open("eq_data_30_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

eq_data = json.load(infile)

##3^ converts contents of load file into a dicitonary

json.dump(eq_data, outfile, indent=4)

print(len(eq_data["features"]))

##Shows the number of earthquakes in this file, means its a list

list_of_eqs = eq_data["features"]

mags = []
lons = []
lats = []
hover_text = []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    title = eq["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)


print(mags[:5])
print(lons[:5])
print(lats[:5])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_text,
        "marker": {
            "size": [mag * 5 for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquake 1 Day")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="globalearthquake1day.html")

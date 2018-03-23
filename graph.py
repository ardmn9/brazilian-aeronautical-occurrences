import folium
import pandas

df = pandas.read_csv('oco.csv', delimiter='~')

series = df['ocorrencia_uf'].value_counts()
newdf = pandas.DataFrame({'UF': series.index, 'freq': series.values})
newdf = newdf[:-1]

br_states = r'brazil-states.geojson'

m = folium.Map([-15, -55], zoom_start=4)

m.choropleth(
    geo_data=br_states,
    data=newdf,
    columns=['UF', 'freq'],
    threshold_scale=[15, 100, 300, 400, 602, 1490],
    key_on='feature.properties.sigla',
    fill_color='YlOrRd',
    line_weight=0,
    legend_name='Aeronautical Occurrences',
)

m.save(outfile='map.html')

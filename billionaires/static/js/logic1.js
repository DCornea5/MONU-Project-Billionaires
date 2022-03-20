d3.csv('./output/billionaires2_geo_dc1.csv',
  function(err, rows){function unpack(rows, key) {return rows.map(function(row){ return row[key];
})};

var data = [{
  lon: unpack(rows, 'longitude'), lat: unpack(rows, 'latitude'), radius:10,
  z: unpack(rows, 'NetWorth'), type: "densitymapbox", coloraxis: 'coloraxis',
  hoverinfo: 'skip'}];

var layout = {
    mapbox: {center: {lon: 60, lat: 30}, style: "outdoors", zoom: 2},
    coloraxis: {colorscale: "Viridis"}, title: {text: "Billionaires Net Worth"},
    width: 600, height: 400, margin: {t: 30, b: 0}};

var config = {mapboxAccessToken: "API_KEY"};

Plotly.newPlot('myDiv', data, layout, config);
})



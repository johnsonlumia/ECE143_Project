import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    name = 'Computer Architecture',
    x = [6,7,8,9,10,11,12,13,14,15,16,17,18], 
    y = [16,16,16,16,16,16,16,15,15,15,15,14,14]
)

trace2 = go.Scatter(
    name = 'Data Structures',
    x= [6,7,8,9,10,11,12,13,14,15,16,17,18],
    y = [10,10,10,10,11,11,10,10,10,10,10,10,10]
)

trace3 = go.Scatter(
    name = 'machine learning',
    x= [6,7,8,9,10,11,12,13,14,15,16,17,18],
    y = [4,0,4,4,4,4,4,6,6,6,6,7,8]
)

trace4 = go.Scatter(
    name = 'storage systems',
    x = [6,7,8,9,10,11,12,13,14,15,16,17,18],
    y = [5,5,5,5,5,5,5,0,0,0,0,0,0]
)

trace5 = go.Scatter(
    name = 'information technology',
    x = [6,7,8,9,10,11,12,13,14,15,16,17,18],
    y = [5,5,5,4,4,0,0,0,0,0,0,0,0]
)

layout = go.Layout(
    title = 'UCSD CSE Top Skills'
)

py.plot([trace1,trace2,trace3,trace4,trace5], layout)
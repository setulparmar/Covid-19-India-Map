import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import folium

app=dash.Dash(__name__)
server=app.server
app.layout=html.Div([html.H1('Covid19-India(By setul parmar)'),html.Iframe(id='map',srcDoc=open('Covid19India.html','r').read(),width='100%',height='600')])

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
if __name__=='__main__':
    app.run_server(debug=True)
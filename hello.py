import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from dash.dependencies import Input, Output, State
from plotly import graph_objs as go
from plotly.graph_objs import *
from datetime import datetime as dt

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

server = app.server

mapbox_access_token = "pk.eyJ1IjoiZGdsaW5kbmVyMiIsImEiOiJja2NucnV0OHAwZHV0MzRsYjZqa3M2eXBsIn0.Q55tSfrIj9N4hOPb-hfIGw"
mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"


# Create Dictionary of Hospital Locations?



list_of_locations = {
"Alabama"       :   {   "lat":  32.31823    ,   "long": -86.902298  }
,
"Alaska"    :   {   "lat":  66.160507   ,   "long": -153.369141 }
,
"Arizona"   :   {   "lat":  34.048927   ,   "long": -111.093735 }
,
"Arkansas"  :   {   "lat":  34.799999   ,   "long": -92.199997  }
,
"California"    :   {   "lat":  36.778259   ,   "long": -119.417931 }
,
"Colorado"  :   {   "lat":  39.113014   ,   "long": -105.358887 }
,
"Connecticut"   :   {   "lat":  41.599998   ,   "long": -72.699997  }
,
"Delaware"  :   {   "lat":  39  ,           "long": -75.5   }
,
"Florida"   :   {   "lat":  27.994402   ,   "long": -81.760254  },
"Georgia"   :   {   "lat":  33.247875   ,   "long": -83.441162  }
,
"Hawaii"    :   {   "lat":  19.741755   ,   "long": -155.844437 }
,
"Idaho  "   :   {   "lat":  44.068203   ,   "long": -114.742043 }
,
"Illinois"  :   {   "lat":  40  ,           "long": -89 }
,
"Indiana"   :   {   "lat":  40.273502   ,   "long": -86.126976  },
"Iowa"          :   {   "lat":  42.032974   ,   "long": -93.581543  }
,
"Kansas"    :   {   "lat":  38.5    ,           "long": -98 }
,
"Kentucky"  :   {   "lat":  37.839333   ,   "long": -84.27002   }
,
"Louisiana" :   {   "lat":  30.39183    ,   "long": -92.329102  }
,
"Maine"         :   {   "lat":  45.367584   ,   "long": -68.972168  }
,
"Maryland"  :   {   "lat":  39.045753   ,   "long": -76.641273  }
,
"Massachusetts" :   {   "lat":  42.407211   ,   "long": -71.382439  }
,
"Michigan"  :   {   "lat":  44.182205   ,   "long": -84.506836  }
,
"Minnesota" :   {   "lat":  46.39241    ,   "long": -94.63623   }
,
"Mississippi"   :   {   "lat":  33  ,           "long": -90 }
,
"Missouri"  :   {   "lat":  38.573936   ,   "long": -92.60376   },
"Montana"   :   {   "lat":  46.96526    ,   "long": -109.533691 }
,
"Nebraska"  :   {   "lat":  41.5    ,           "long": -100    }
,
"Nevada"    :   {   "lat":  39.876019   ,   "long": -117.224121 },
"New Hampshire" :   {   "lat":  44  ,           "long": -71.5   }
,
"New Jersey"    :   {   "lat":  39.833851   ,   "long": -74.871826  }
,
"New Mexico"    :   {   "lat":  34.307144   ,   "long": -106.018066 }
,
"New York"  :   {   "lat":  43  ,           "long": -75 }
,
"North Carolina":   {   "lat":  35.782169   ,   "long": -80.793457  },
"North Dakota"  :   {   "lat":  47.650589   ,   "long": -100.437012 }
,
"Ohio"          :   {   "lat":  40.367474   ,   "long": -82.996216  }
,
"Oklahoma"  :   {   "lat":  36.084621   ,   "long": -96.921387  }
,
"Oregon"    :   {   "lat":  44  ,           "long": -120.5  }
,
"Pennsylvania"  :   {   "lat":  41.203323   ,   "long": -77.194527  },
"Rhode Island"  :   {   "lat":  41.700001   ,   "long": -71.5   }
,
"South Carolina":   {   "lat":  33.836082   ,   "long": -81.163727  },
"South Dakota"  :   {   "lat":  44.5    ,           "long": -100    }
,
"Tennessee" :   {   "lat":  35.860119   ,   "long": -86.660156  },
"Texas"         :   {   "lat":  31  ,           "long": -100    }
,
"Utah"          :   {   "lat":  39.41922    ,   "long": -111.950684 },
"Vermont"   :   {   "lat":  44  ,           "long": -72.699997  }
,
"Virginia"  :   {   "lat":  37.926868   ,   "long": -78.024902  }
,
"Washington"    :   {   "lat":  47.751076   ,   "long": -120.740135 }
,
"West Virginia" :   {   "lat":  39  ,           "long": -80.5   }
,
"Wisconsin" :   {   "lat":  44.5    ,           "long": -89.5   }
,
"Wyoming"   :   {   "lat":  43.07597    ,   "long": -107.290283 }
    }




# Layout of Dash App
app.layout = html.Div(
    children = [
        html.Div(
            className="row",
            children = [
                # Column for User Inputs
                html.Div(
                    className="four columns div-user-controls",
                    children = [
                        html.Img(
                            className="logo", src=app.get_asset_url("ibm_logo.png")
                            ),
                        html.H2("COVID-19 Dashboard"),
                        html.P(
                            """Select a time using the date picker to view the threat
                               level of each counties exposure to COVID-19."""
                            ),
                        html.Div(
                            className="div-for-dropdown",
                            children=[
                                dcc.DatePickerSingle(
                                    id="date-picker",
                                    min_date_allowed=dt(2020,5,1),
                                    max_date_allowed=dt(2020,7,15),
                                    initial_visible_month=dt(2020,7,1),
                                    date=dt(2020,7,5).date(),
                                    display_format="MMMM D, YYYY",
                                    style={'border': "0px solid black"},
                                    )
                                ],
                            ),

                        # Make side-by-side layout
                        html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className='div-for-dropdown',
                                    children = [
                                    # Dropdown for Selecting State on Map
                                    dcc.Dropdown(
                                        id='location-dropdown',
                                        options=[
                                            {"label": i, "value": i}
                                            for i in list_of_locations
                                            ],
                                        value="North Carolina",
                                        )
                                    ],
                            ),
                        ],
                    ),
                    html.P(id="total-cases"),
                    html.P(id="total-cases-selection"),
                    html.P(id='date-value')
                ],
            ),
                # Column for Graphs
        html.Div(
            className="eight columns div-for-charts bg-grey",
                    children=[
                        dcc.Graph(
                                    style={'height': '100%'},
                                    id="county-choropleth",
                                    figure=dict(
                                        layout=dict(
                                            mapbox=dict(
                                                layers=[],
                                                accesstoken=mapbox_access_token,
                                                style=mapbox_style,
                                                center=dict(
                                                    lat=38.72490, lon=-95.61446
                                                ),
                                                pitch=0,
                                                zoom=3.5,
                                            ),
                                            autosize=True,
                                        ),
                                    ),
                                )
                        ],
                    ),
                ],
            )
        ]
    )



@app.callback(
    Output("county-choropleth", "figure"),
    [Input("location-dropdown", "value")],
    [State("county-choropleth", "figure")],
)
def display_map(state, figure):
    #cm = dict(zip(BINS, DEFAULT_COLORSCALE))

    data = [
        dict(
            lat=list_of_locations[state]["lat"],
            lon=list_of_locations[state]["long"],
            text=state,
            type="scattermapbox",
            hoverinfo="text",
            marker=dict(size=5, color="white", opacity=0),
        )
    ]

    annotations = [
        dict(
            showarrow=False,
            align="right",
            text="<b>Age-adjusted death rate<br>per county per year</b>",
            font=dict(color="#2cfec1"),
            bgcolor="#1f2630",
            x=0.95,
            y=0.95,
        )
    ]

    #for i, bin in enumerate(reversed(BINS)):
    #    color = cm[bin]
    #    annotations.append(
    #        dict(
    #            arrowcolor=color,
    #            text=bin,
    #            x=0.95,
    #            y=0.85 - (i / 20),
    #            ax=-60,
    #            ay=0,
    #            arrowwidth=5,
    #            arrowhead=0,
    #            bgcolor="#1f2630",
    #            font=dict(color="#2cfec1"),
    #        )
    #    )

    if state in list_of_locations:
        lat = list_of_locations[state]["lat"]
        lon = list_of_locations[state]["long"]
        zoom = 6
    else:
        lat = 38
        lon = -95
        zoom = 3.5
    

    layout = dict(
        mapbox=dict(
            layers=[],
            accesstoken=mapbox_access_token,
            style=mapbox_style,
            center=dict(lat=lat, lon=lon),
            zoom=zoom,
        ),
        hovermode="closest",
        margin=dict(r=0, l=0, t=0, b=0),
        annotations=annotations,
    )

    base_url = "https://raw.githubusercontent.com/jackparmer/mapbox-counties/master/"
    #for bin in BINS:
    #    geo_layer = dict(
    #        sourcetype="geojson",
    #        source=base_url + str(year) + "/" + bin + ".geojson",
    #        type="fill",
    #        color=cm[bin],
    #        opacity=DEFAULT_OPACITY,
            # CHANGE THIS
    #        fill=dict(outlinecolor="#afafaf"),
    #    )
    #    layout["mapbox"]["layers"].append(geo_layer)

    fig = dict(data=data, layout=layout)
    return fig
   

if __name__ == "__main__":
    app.run_server(debug=True)
        
 


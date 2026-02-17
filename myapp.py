from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder(return_type='pandas', datetimes=True)
countries = df['country'].drop_duplicates()

app = Dash(__name__)
server = app.server
# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": symbol, "value": symbol} for symbol in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(symbol):
    new_df = df[df["country"] == symbol]
    fig = px.line(new_df, x="year", y='gdpPercap', title=f"GDP in {symbol} ")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 
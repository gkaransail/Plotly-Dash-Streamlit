import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import requests

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout for Dash app
app.layout = dbc.Container([
    html.H1("Customer Sales Data"),
    dcc.Input(id="filter-value", type="text", placeholder="Enter value", debounce=True),
    html.Button(id="submit-btn", n_clicks=0, children="Submit"),
    html.Div(id="output-data"),
])

# Callback to fetch data from FastAPI and display it
@app.callback(
    Output("output-data", "children"),
    Input("submit-btn", "n_clicks"),
    Input("filter-value", "value"),
)
def update_data(n_clicks, filter_value):
    if n_clicks > 0 and filter_value:
        try:
            # Fetch data from FastAPI
            url = f"http://127.0.0.1:8000/data/{filter_value}"  # Correct the FastAPI URL
            response = requests.get(url)

            if response.status_code == 200:
                # Display the data as formatted JSON
                data = response.json()
                return html.Pre(str(data))  # Display the response in a formatted way
            else:
                return html.Div("No data found or error occurred.")
        except Exception as e:
            return html.Div(f"Error: {str(e)}")
    
    return "Enter a Primary UPC and click submit."

if __name__ == "__main__":
    app.run_server(port=4065)




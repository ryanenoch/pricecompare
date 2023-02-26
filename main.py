from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State
from price import price

stores=['Giant Tiger','Food Basics','Metro','Some Random Grocery Store']
app = Dash(__name__)
server = app.server

app.layout = html.Div([
  html.H1(children='Price Compare'),
  html.Div(children=[
            dcc.Input(id="prtinput", type="text", placeholder='Enter Product name'),
            dcc.Dropdown(id="storinput", options=stores,placeholder='Filter by store'),
            #html.Button('Enter', id='enter', n_clicks=0)
        ],
                 style={
                     'display': 'flex',
                     'justify-content': 'center'
                 }),
          html.Br(),
  dash_table.DataTable(
            id='table',
            columns=[
                {
                    'name': 'Date',
                    'id': 'date',
                    'deletable': False,
                    'renamable': False
                },
                {
                    'name': 'Store',
                    'id':'store',  
                    'type': 'text',
                    'deletable': False,
                    'renamable': False
                },
                {
                    'name': 'Product',
                    'id': 'product',
                    'deletable': False,
                    'renamable': False
                },
                {
                    'name': 'Availability',
                    'id': 'availability',
                    'deletable': False,
                    'renamable': False
                },
                {
                    'name': 'Regular Price (CAD)',
                    'id': 'reg_price',
                    'deletable': False,
                    'renamable': False
                },
                {
                    'name': 'Rewards Price (CAD)',
                    'id': 'rew_price',
                    'deletable': False,
                    'renamable': False
                }
            ],
            data=[],  #starts with empty data
            editable=False,
            row_deletable=False,
            style_cell={
                'fontSize': 15,
                'font-family': 'sans-serif',
                'whiteSpace': 'normal',#wordwrap for cells
                'textAlign': 'center'  #to center align the text in the cell 
            },
            style_table={
                'padding-left': '0%',
                'padding-right': '0%',
                'marginLeft': 'auto',
                'marginRight': 'auto',
                'width': '99%'
            },
            style_header={
                'padding-left': '20 px',
                'padding-right': '20 px',
                'backgroundColor': 'lightblue',  #table header BG color
                'fontWeight': 'bold',
                'color': 'black',
                'whiteSpace': 'normal'  #wordwrap for headers
            }),
],style={'font-family': 'sans-serif'})

@app.callback(
  Output('table','data'),
  State('table','data'),
  Input("prtinput", "value"),
  Input("storinput", "value")
)
def prod(rows,prtname,storname):
  resultdf=price(prtname,storname)
  print(resultdf)
  print()
  

  records=resultdf.to_dict('records')
  print(records)
  print()

  return records
  
if __name__ == '__main__':
    app.run_server(debug=True, port=os.getenv("PORT", default=5000))
#app.run_server(host='0.0.0.0', port=8081, debug=True)

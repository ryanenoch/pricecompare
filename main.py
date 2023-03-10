from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State
from price import price

app = Dash(__name__)

server = app.server

app.layout = html.Div([
  html.H1(children='Price Compare'),
  html.Div(children=[
            dcc.Input(id="prtinput", type="text", placeholder='Enter Product name'),
            #html.Button('Enter', id='enter', n_clicks=0)
        ],
                 style={
                     'display': 'grid',
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
                    'name': 'Price (CAD)',
                    'id': 'price',
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
                'backgroundColor': 'mintcream',
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
                'backgroundColor': 'lightgreen',  #table header BG color
                'fontWeight': 'bold',
                'color': 'black',
                'whiteSpace': 'normal'  #wordwrap for headers
            }),
  html.Br(),
  html.Footer([
    html.P('Made in Sault Ste. Marie????????'),
    html.P('?? 2023 Ryan Enoch')
  ])
],style={'font-family': 'sans-serif'})

@app.callback(
  Output('table','data'),
  State('table','data'),
  Input("prtinput", "value")
)
def prod(rows,prtname):
  resultdf=price(prtname)
  print(resultdf)
  print()
  

  records=resultdf.to_dict('records')
  print(records)
  print()

  return records
  
if __name__ == '__main__':
    app.run_server(debug=True, port=os.getenv("PORT", default=5000))
#app.run_server(host='0.0.0.0', port=8081, debug=True)

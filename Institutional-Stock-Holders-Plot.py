import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

cont = 'Y'

while cont == 'Y':

    #Prompt user
    print('Input a ticker (ex. AMZN)')
    ticker = input()

    try:
        #Collect ticker data
        ticker_data = yf.Ticker(ticker)

        inst_holders_df = ticker_data.institutional_holders

        #Create figure
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=inst_holders_df['Holder'],
            y=inst_holders_df['Shares'],
            name='Shares per Holder',
            marker_color='indianred'
        ))

        fig.update_layout(barmode='group', xaxis_tickangle=-45)

        fig.show()

    except (Exception):
        print("Ticker not found..")
        continue

    print('Continue? (Y/N)')
    cont = input()



import yfinance as yf
import datetime as dt
from Stock import Stock as st
from ETF import ETF as etf
from MutualFund import MutualFund as mf
import requests
import os
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    yf.pdr_override()
    today = dt.datetime.now()
    d = today.strftime("%Y-%m-%d")
    POST_URL = ""

    with open(os.path.join(sys.path[0], "watchlistDataURL.txt")) as file:
        for line in file:
            POST_URL = line

    headers = {"Content-Type": "application/json"}

    stocks = ['AAPL', 'AMD', 'AMZN', 'AXP', 'BAC', 'BHP', 'CAT', 'CCI', 'CMC', 'CSCO', 'CVS', 'DIS', 'DUK', 'FDX', 'GOOGL',
              'INTC', 'JNJ', 'KO', 'MSFT', 'NFG', 'O', 'TGT', 'TSLA', 'UPS', 'WM', 'ARKF', 'ARKK', 'ARKQ', 'ARKW', 'DGEIX',
              'FREL', 'GLD', 'SCHD', 'SPHD']
    for s in stocks:
        sData = []
        current = yf.Ticker(s).info

        #Get Investment type
        qType = current["quoteType"]

        #If equity collect this set of information
        if qType == 'EQUITY':
            currentPrice = current['currentPrice']
            previous = current['previousClose']
            high = current['fiftyTwoWeekHigh']
            low = current['fiftyTwoWeekLow']

            oneDay = 'No Change'
            if currentPrice - previous > 0:
                oneDay = 'Up'
            elif currentPrice - previous < 0:
                oneDay = 'Down'

            percentHigh = (currentPrice / high) * 100
            formatHigh = "{:.2f}".format(percentHigh)
            percentLow = (currentPrice / low) * 100
            formatLow = "{:.2f}".format(percentLow)

            # Preset Values in case of no dividend
            divStatus = False
            d3 = ""
            exDivDate = current['exDividendDate']
            divRate = current['trailingAnnualDividendRate']
            divYield = current['trailingAnnualDividendYield']
            percentYield = None
            formatYield = None

            if divYield is not None:
                divStatus = True
                percentYield = divYield * 100
                formatYield = "{:.2f}".format(percentYield)
                floatYield = float(formatYield)

            if exDivDate is not None:
                timestamp = float(exDivDate)
                d2 = dt.datetime.fromtimestamp(timestamp)
                d3 = d2.strftime("%Y-%m-%d")

            trailingeps = current['trailingEps']
            forwardeps = current['forwardEps']
            epsGrowth = (((forwardeps - trailingeps) / trailingeps) * 100)
            formatEG = "{:.2f}".format(epsGrowth)

            try:
                trailingPE = current['trailingPE']
            except:
                trailingPE = None

            try:
                forwardPE = current['forwardPE']
            except:
                forwardPE = None

            if trailingPE is not None:
                peDecrease = (((forwardPE - trailingPE) / trailingPE) * 100)
                formatPED = "{:.2f}".format(peDecrease)
            else:
                peDecrease = None

            stock = st(current['symbol'], d, qType, current['longName'], current['sector'], current['industry'], currentPrice, previous, oneDay,
                       high, low, formatHigh, formatLow, divStatus, d3, divRate, floatYield, current['debtToEquity'],
                       trailingeps, forwardeps, formatEG, trailingPE, forwardPE, formatPED)

            r = requests.request("POST", POST_URL, headers=headers, data=stock.to_json())
            print(r.text)

        #If ETF collect this information
        elif qType == 'ETF':
            current = yf.Ticker(s).info

            currentPrice = current['regularMarketPrice']
            previous = current['previousClose']
            high = current['fiftyTwoWeekHigh']
            low = current['fiftyTwoWeekLow']

            oneDay = 'No Change'
            if currentPrice - previous > 0:
                oneDay = 'Up'
            elif currentPrice - previous < 0:
                oneDay = 'Down'

            percentHigh = (currentPrice / high) * 100
            formatHigh = "{:.2f}".format(percentHigh)
            sData.append(formatHigh + '%')
            percentLow = (currentPrice / low) * 100
            formatLow = "{:.2f}".format(percentLow)

            yieldStatus = False
            fundYield = current['yield']
            estYearlyRate = None
            percentYield = None
            formatYield = None
            if fundYield is not None:
                divStatus = True
                estYearlyRate = currentPrice * fundYield
                percentYield = fundYield * 100
                formatYield = "{:.2f}".format(percentYield)

            sData.append(yieldStatus)
            sData.append(estYearlyRate)
            sData.append(formatYield)

            fund = etf(current['symbol'], d, qType, current['longName'], currentPrice, previous, oneDay, high, low,
                       formatHigh, formatLow, divStatus, estYearlyRate, formatYield)

            r = requests.request("POST", POST_URL, headers=headers, data=fund.to_json())
            print(r.text)

        elif qType == 'MUTUALFUND':
            current = yf.Ticker(s).info

            currentPrice = current['regularMarketPrice']
            previous = current['regularMarketPreviousClose']

            oneDay = 'No Change'
            if currentPrice - previous > 0:
                oneDay = 'Up'
            elif currentPrice - previous < 0:
                oneDay = 'Down'

            m = mf(current['symbol'], d, qType, current['longName'], currentPrice, previous, oneDay)
            r = requests.request("POST", POST_URL, headers=headers, data=m.to_json())
            print(r.text)

    print('Upload Complete')
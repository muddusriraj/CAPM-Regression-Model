import pandas as pd
msftLoc = "MSFTRawData.csv"
tBillLoc = "tBillRawData.csv"
snpLoc = "SnPRawData.csv"


#calculates daily return rate using daily highs and formats dataset to
#be ['Date', 'Return']
def dfReturnRate(df):
    currVals = pd.to_numeric(df['High'].iloc[1:].values) 
    backVals = pd.to_numeric(df['High'].iloc[0:-1].values)
    returnRate = (currVals - backVals) / backVals
    df.drop(index=0, inplace=True)
    df.reset_index(drop=True, inplace=True)

    df['Return'] = returnRate
    df.drop(columns=['Close/Last', 'Volume', 'Open', 'High', 'Low'], inplace=True)
    


msftDf = pd.read_csv(msftLoc)
msftDf['High'] = msftDf['High'].apply(lambda ele: ele[1:])
tBillDf = pd.read_csv(tBillLoc)
snpDf = pd.read_csv(snpLoc)

dfReturnRate(msftDf)
dfReturnRate(snpDf)
tBillDf['Return'] = tBillDf['TB3MS']/91
tBillDf.drop(columns=['TB3MS'], inplace=True)
#reformatting tBill dates as they are seperated by dashes instead of slashes 
#like the other datasets and are in a different order
tBillDf['observation_date'] = tBillDf['observation_date'].apply(lambda date : f'{date[5:7]}/{date[8:10]}/{date[0:4]}')
tBillDf.rename(columns={'observation_date': 'Date'}, inplace=True)

#have consistent dates for the tBill data, msft data, and SPY data
msftDf.drop(list(range(0, 10)), inplace=True)
msftDf.reset_index(drop=True, inplace=True)
snpDf.drop(list(range(0, 10)), inplace=True)
snpDf.reset_index(drop=True, inplace=True)
tBillDf.drop(list(range(0, 972)), inplace=True)
tBillDf.reset_index(drop=True, inplace=True)

#tBill data needs to be matched up to individual dates for each month for 
#MSFT and SPY (MSFT and SPY already have matching dates in their dataset so
#using MSFT dates will suffice)

tBillReturnRates = []
tBillind = 1

for index, row in msftDf.iterrows():
    
    currMSFTDate = row['Date']
    currTBillDate = tBillDf.iloc[-tBillind]['Date']

    if currTBillDate[0:2] == currMSFTDate[0:2] and currTBillDate[6:10] == currMSFTDate[6:10]:
        tBillReturnRates.append(tBillDf.iloc[-tBillind]['Return'])
    else:
        tBillind = tBillind+1
        tBillReturnRates.append(tBillDf.iloc[-tBillind]['Return'])

totalDf = pd.DataFrame(columns=['Date', 'Return MSFT', 'Return S&P', 'Return T-Bill'])

totalDf['Date'] = msftDf['Date']
totalDf['Return MSFT'] = msftDf['Return']
totalDf['Return S&P'] = snpDf['Return']
totalDf['Return T-Bill'] = tBillReturnRates

totalDf.to_csv('totalReturnRates.csv', encoding='utf-8', index=False)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fullData = pd.read_csv("covid19vaccinesbycounty.csv")
countries = ["Nevada", "Los Angeles"]
for x in countries:
    fullDataNevada = fullData.loc[fullData['county']==x]
    dates = [data for data, df in fullDataNevada.groupby('administered_date')]
    results = fullDataNevada.groupby('administered_date').mean()
    plt.plot(dates, results['cumulative_pfizer_doses'])
    plt.plot(dates, results['cumulative_moderna_doses'])
    plt.legend(["Phizer full","Moderna full"])
    plt.xticks(np.arange(0, len(dates)+1,20),rotation =45,size=6)
    plt.show()

import os
import pandas as pd
import numpy as np

# riga 62 partono quelli con le unità
# riga 602 partono quelli con le decine


def main():
    filename = "Regressione/HomeWork_Regression_2024_v1.xlsx"
    spreedsheet = "Cloud"
    df = pd.read_excel(filename, sheet_name = spreedsheet)

    if 'currentTime' in df.columns:
        for i in range(1, 60):
            df['currentTime'].iloc[i] = str(df['currentTime'].iloc[i]).replace('.', ',')
            
        colonne1 = df['currentTime'].iloc[60:600].apply(lambda x: '{:.0f}'.format(x))
        colonne2 = df['currentTime'].iloc[600:].apply(lambda x: '{:.0f}'.format(x))
        #df['currentTime'] = df['currentTime'].astype(str).str.replace('.', '', regex=False)
        for i in range(60, 600):
            #df['currentTime'].iloc[i] = str(df['currentTime'].iloc[i])[:1] + ',' + str(df['currentTime'].iloc[i])[1:]
            number = colonne1.iloc[i-60]
            df['currentTime'].iloc[i] = number[:1] + ',' + number[1:]
        for i in range(600, len(df)):
            #df['currentTime'].iloc[i] = str(df['currentTime'].iloc[i])[:2] + ',' + str(df['currentTime'].iloc[i])[2:]
            number = colonne2.iloc[i-600]
            df['currentTime'].iloc[i] = number[:2] + ',' + number[2:]

    #df = df.applymap(lambda x: f"{x}".replace('.', ',') if isinstance(x, (int, float)) else x)
    
    df.to_excel("Cloud.xlsx", index=False)



if __name__ == "__main__":

    main()
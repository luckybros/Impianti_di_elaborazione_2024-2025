import numpy as np
import pandas as pd
from scipy.stats.mstats import theilslopes
import matplotlib.pyplot as plt

import locale

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

def main():
    file_name = "Regressione/HomeWork_Regression_2024_v1.xlsx"
    
    output_csv = "Regressione/regression_results_"
    
    tables = ["os1", "os2", "os3", "VMres1", "VMres3"]

    # Dizionario per salvare i risultati
    results = {
        "Metric": ["Pendenza", "Intercetta", "Intervallo superiore", "Intervallo inferiore"]
    }

    for table in tables: 
        print(table)
        output_csv_local = output_csv
        results_local = results

        df = pd.read_excel(file_name, sheet_name=table)

        x_column = df.columns[0]  # Prima colonna
        y_column = df.columns[1:]

        x_float = df[x_column].astype(str).apply(locale.atof)
    
        x = np.array(x_float)
    
        for column in y_column:
            y_numeric = pd.to_numeric(df[column], errors='coerce')
            y = np.array(y_numeric)
        
            slope, intercept, low, up = theilslopes(y, x, 0.95)

            slope = round(slope, 3)
            intercept = round(intercept, 3)
            low = round(low, 3)
            up = round(up, 3)
        
            results_local[column] = [slope, intercept, up, low]
    
        print(results_local)

        results_df = pd.DataFrame(results_local)
        results_df.to_csv(output_csv + table + ".csv", index=False, decimal=',', sep=';')
        #print(f"Risultati salvati in {output_csv + table + ".csv"})


if __name__ == "__main__":

    main()
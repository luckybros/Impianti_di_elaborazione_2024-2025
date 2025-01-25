import numpy as np
import pandas as pd
from scipy.stats.mstats import theilslopes
import matplotlib.pyplot as plt

import locale

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

def main():
    file_name = "Regressione/Cloud.xlsx"
    output_csv = "Regressione/regression_results_cloud.csv"
    
    x_column = "currentTime"
    y_column = ["core0Usage...", "core1Usage...", "core2Usage...", "core3Usage...", "usedMemory", "total_IO_read", "total_IO_write"]
    
    df = pd.read_excel(file_name)
    
    x_float = df[x_column].astype(str).apply(locale.atof)
    
    #print(x_float)
    
    x = np.array(x_float)

    # Dizionario per salvare i risultati
    results = {
        "Metric": ["Pendenza", "Intercetta", "Intervallo superiore", "Intervallo inferiore"]
    }
    
    for column in y_column:
        y = np.array(df[column])
        
        slope, intercept, low, up = theilslopes(y, x, 0.95)
        
        results[column] = [slope, intercept, up, low]
    
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_csv, index=False, decimal=',', sep=';')
    print(f"Risultati salvati in {output_csv}")


if __name__ == "__main__":

    main()
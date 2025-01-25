import numpy as np
import pandas as pd
from scipy.stats.mstats import theilslopes
import locale

# Imposta il locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

def main():
    file_name = "Regressione/HomeWork_Regression_2024_v1.xlsx"
    output_csv = "Regressione/risultati-"
    tables = ["os1", "os2", "os3", "VMres1", "VMres3"]

    for table in tables: 
        print(f"Processing sheet: {table}")
        
        # Legge il foglio Excel
        df = pd.read_excel(file_name, sheet_name=table)

        # Prima colonna come asse X
        x_column = df.columns[0]
        x_float = df[x_column].astype(str).apply(locale.atof)  # Converte in float
        x = np.array(x_float)

        # Colonne Y
        y_columns = df.columns[1:]
        
        # Lista per raccogliere i risultati
        results = []

        # Calcola Theil-Sen per ogni colonna Y
        for column in y_columns:
            y_numeric = pd.to_numeric(df[column], errors='coerce')  # Converte in numerico
            y = np.array(y_numeric)
        
            slope, intercept, low, up = theilslopes(y, x, 0.95)

            results.append({
                "Colonna": column,
                "Pendenza": round(slope, 3),
                "Intercetta": round(intercept, 3),
                "Intervallo Superiore": round(up, 3),
                "Intervallo Inferiore": round(low, 3)
            })
        
        # Salva i risultati in un DataFrame
        results_df = pd.DataFrame(results)
        
        # Salva in CSV
        output_file = f"{output_csv}{table}.csv"
        results_df.to_csv(output_file, index=False, decimal=',', sep=';')
        print(f"Risultati salvati in: {output_file}")

if __name__ == "__main__":
    main()
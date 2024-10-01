# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:43:02 2024

@author: sheri
"""
import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import os
from datetime import datetime
import argparse

def main(input_file, output_name):
    # Data from Excel
    try:
        data = pd.read_excel(input_file)
    except Exception as e:
        print(f"Error loading data: {e}")
        exit()

    t_values = data['t'].values
    R_values = data['R'].values
    print("t values:", t_values)
    print("R values:", R_values)

    R_values[R_values == 1] = 0.99999
    valid_indices = R_values < 1

    # Define all g(R) functions
    g_functions = {
        'P1': lambda R: R**(1/2),
        'P2': lambda R: R**(1/3),
        'P3': lambda R: R**(1/4),
        'A2': lambda R: (-np.log(1 - R))**(1/2),
        'A3': lambda R: (-np.log(1 - R))**(1/3),
        'A4': lambda R: (-np.log(1 - R))**(1/4),
        'R2': lambda R: 1 - (1 - R)**(1/2),
        'R3': lambda R: 1 - (1 - R)**(1/3),
        'D1': lambda R: R**2,
        'D2': lambda R: ((1 - R) * np.log(1 - R)) + R,
        'D3': lambda R: (1 - (1 - R)**(1/3))**2,
        'D4': lambda R: 1 - (2/3) * R - (1 - R)**(2/3),
        'F0': lambda R: R,
        'F1': lambda R: -np.log(1 - R),
        'F2': lambda R: (1 / (1 - R)) - 1,
        'F3': lambda R: (1/2) * (((1 - R)**-2) - 1)
    }

    # g(R) calculations  and fitting the data
    results = {}
    for name, func in g_functions.items():
        g_values = func(R_values)
        slope, intercept, r_value, p_value, std_err = linregress(t_values, g_values)
        results[name] = {
            'g_values': g_values,
            'slope': slope,
            'intercept': intercept,
            'r_squared': r_value**2,
            'fitted_values': slope * t_values + intercept
        }
        print(f"\nFitting for {name}:")
        print(f"Slope (k): {slope}")
        print(f"Intercept: {intercept}")
        print(f"R-squared: {r_value**2}")

    # Creating DataFrames
    results_df = pd.DataFrame({
        't_values': t_values,
        'R_values': R_values,
        **{f'g_{name}': res['g_values'] for name, res in results.items()},
        **{f'Fitted_g_{name}': res['fitted_values'] for name, res in results.items()}
    })

    summary_df = pd.DataFrame([
        {'Parameter': f'{param}_{name}', 'Value': value}
        for name, res in results.items()
        for param, value in [('Slope', res['slope']), ('Intercept', res['intercept']), ('R_squared', res['r_squared'])]
    ])

    # Displaying DataFrames
    print(results_df)
    print(summary_df)

    # Outputing to Excel
    output_file_path = f'{output_name}_fitted_results.xlsx'
    with pd.ExcelWriter(output_file_path) as writer:
        results_df.to_excel(writer, sheet_name='Fitted Data', index=False)
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
    print(f"Results have been saved to {output_file_path}")

    # Plotting function
    def plot_data(t_values, g_values, slope, intercept, r_squared, title, filename):
        plt.figure(figsize=(10, 6))
        plt.scatter(t_values, g_values, label='Original Data', color='blue')
        fitted_values = slope * t_values + intercept
        plt.plot(t_values, fitted_values, color='red', label='Fitted Line')
        plt.text(0.1, 0.9, f'Slope: {slope:.2f}\nIntercept: {intercept:.2f}\nR²: {r_squared:.2f}',
                 transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
        plt.title(title)
        plt.xlabel('(t)')
        plt.ylabel('(g(R))')
        plt.legend()
        plt.grid()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename_with_timestamp = f"{os.path.splitext(filename)[0]}_{timestamp}.png"
        plt.savefig(filename_with_timestamp)
        plt.close()

    # Creating the plots
    for name, res in results.items():
        plot_data(t_values, res['g_values'], res['slope'], res['intercept'], res['r_squared'],
                  f'Plot of (g_{name}) vs (t)', f'{output_name}_g_{name}_vs_t.png')
    print("All plots have been saved as PNG files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="calculating kinetics from Excel file and generate plots.")
    parser.add_argument("input_file", help="Path to the input Excel file")
    parser.add_argument("output_name", help="Base name for output files (without extension)")
    args = parser.parse_args()

    main(args.input_file, args.output_name)
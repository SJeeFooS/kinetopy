# Kinetopy

**Kinetopy** is a Python tool designed to calculate solid-state kinetics from experimental data and generate corresponding plots. This tool provides an approach for analyzing and visualizing kinetic data using various kinetic models.

**The kinetic models are based on the paper "Solid-State Kinetic Models: Basics and Mathematical Fundamentals" by Ammar Khawam and Douglas R. Flanagan**

## Reaction Models and Expressions

Kinetopy calculates the kinetics for various solid-state reaction models, based on the integral forms. The table below lists the models included in both differential and integral forms.

### TABLE 1: Solid-State Rate and Integral Expressions for Different Reaction Models


| **Model**                         | **Differential Form (f(R))**                        | **Integral Form (g(R))**                             |
|-----------------------------------|-----------------------------------------------------|------------------------------------------------------|
| **Nucleation Models**             |                                                     |                                                      |
| Power Law (P2)                    | $2R^{1/2}$                                          | $R^{1/2}$                                            |
| Power Law (P3)                    | $3R^{2/3}$                                          | $R^{1/3}$                                            |
| Power Law (P4)                    | $4R^{3/4}$                                          | $R^{1/4}$                                            |
| Avrami-Erofeyev (A2)              | $2(1 - R)[-\ln(1 - R)]^{1/2}$                       | $[-\ln(1 - R)]^{1/2}$                                |
| Avrami-Erofeyev (A3)              | $3(1 - R)[-\ln(1 - R)]^{2/3}$                       | $[-\ln(1 - R)]^{1/3}$                                |
| Avrami-Erofeyev (A4)              | $4(1 - R)[-\ln(1 - R)]^{3/4}$                       | $[-\ln(1 - R)]^{1/4}$                                |
| **Geometrical Contraction Models**|                                                     |                                                      |
| Contracting Area (R2)             | $2(1 - R)^{1/2}$                                    | $1 - (1 - R)^{1/2}$                                  |
| Contracting Volume (R3)           | $3(1 - R)^{2/3}$                                    | $1 - (1 - R)^{1/3}$                                  |
| **Diffusion Models**              |                                                     |                                                      |
| 1-D Diffusion (D1)                | $\frac{1}{2R}$                                      | $R^2$                                                |
| 2-D Diffusion (D2)                | $-\frac{1}{\ln(1 - R)}$                             | $(1 - R)\ln(1 - R) + R$                              |
| 3-D Diffusion-Jander (D3)         | $\frac{3(1 - R)^{2/3}}{2(1 - (1 - R)^{1/3})}$     | $(1 - (1 - R)^{1/3})^2$                              |
| Ginstling-Brounshtein (D4)        | $\frac{3}{2((1 - R)^{-1/3} - 1)}$                  | $1 - \frac{2}{3}R - (1 - R)^{2/3}$                  |
| **Reaction-Order Models**         |                                                     |                                                      |
| Zero-Order (F0/R1)                | $1$                                                 | $R$                                                  |
| First-Order (F1)                  | $1 - R$                                            | $-\ln(1 - R)$                                        |
| Second-Order (F2)                 | $(1 - R)^2$                                        | $\frac{1}{1 - R} - 1$                                |
| Third-Order (F3)                  | $(1 - R)^3$                                        | $\frac{1}{2}[(1 - R)^{-2} - 1]$                      |


---

These models are incorporated into Kinetopy to provide a wide range of options for fitting experimental data and visualizing solid-state kinetics.


---

## Key Features
- **Automated kinetic model fitting:** Supports several kinetic models like P1, P2, A2, and others.
- **Data visualization:** Automatically generates plots for each kinetic model (g(R) vs time.
- **Excel integration:** Input data is read from an Excel file (headers t and R in first row, then data), and results are saved back to Excel.

---

## Requirements
Before running Kinetopy, make sure you have the following Python packages installed:
- `pandas`
- `numpy`
- `scipy`
- `matplotlib`
- `openpyxl`

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt

python setup.py install

```


## Installation

You can install Kinetopy by cloning the repository and running the `setup.py`:

```bash
git clone https://github.com/yourusername/kinetopy.git
cd kinetopy
python setup.py install
```
## Usage
write this in terminal

```bash
kinetopy.py input_file_example.xlsx output_file_example
```

replace input_file_example.xlsx by the name of your file (must be existed in the same folder)

##Input File Format
Your input Excel file should contain two columns:

t: Time values.
R: Reaction progress values (fraction reacted).

the first row, first column must be written as t.
the first row, second column must be written as R.

An example input file might look like this:


| **t** | **R** |
|-------|-------|
| 0     | 0.1   |
| 5     | 0.3   |
| 10    | 0.5   |
| 15    | 0.7   |
| 20    | 0.9   |


# Author

Sherif Ashraf Ahmed Hefney

# Email: 

Sherif1.se@gmail.com

# kinetopy

a Python tool designed to calculate solid-state kinetics from experimental data and generate corresponding plots.
>>>>>>> bc636f6ef009639c3be262bcec8cb2de9ea2f0a1

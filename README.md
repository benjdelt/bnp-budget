[Français](./README.fr.md)

# BNP Paribas Fortis Budget

A Python script that takes a CSV file with banking transactions exported from BNP Paribas Fortis PC Banking app and
produces graphs representing monthly and quarterly income, expenses and balances. It also prints that data to the 
STDOUT.

## Getting Started

- Make sure Python (>=3.10.0) and Pip (>=21.2.3) are installed.
- Clone the repo and `cd` into it.
- Create a virtual environment using venv and activate it following 
[these instructions](https://docs.python.org/3/library/venv.html).
- Install the dependencies
```
pip install -r requirements.txt
```
- Run the script
```
python script.py
```
The generated graphs open automatically and are saved as gitignored png files.

### Dependencies

- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)



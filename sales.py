import statistics
import csv

monthly_sales = {}

with open('ventas.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['Month']
        sales = int(row['Sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print("Monthly sales data:", sales)

# Hallar la media
mean_sales = statistics.mean(sales)
print("Mean sales:", mean_sales)
# Hallar la mediana
median_sales = statistics.median(sales)
print("Median sales:", median_sales)
# Hallar la moda
mode_sales = statistics.mode(sales)
print("Mode sales:", mode_sales)
# Hallar la desviación estándar
std_dev_sales = statistics.stdev(sales)
print("Standard Deviation of sales:", std_dev_sales)
# Hallar la varianza
variance_sales = statistics.variance(sales)
print("Variance of sales:", variance_sales)
# Hallar el rango
range_sales = max(sales) - min(sales)
print("Range of sales:", range_sales)

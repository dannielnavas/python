import reports
sales_report = reports.generate_sales_report("January", [1500, 2300, 1800])
expenses_report = reports.generate_expenses_report("January", [800, 600, 400])
print(sales_report)
print(expenses_report)

import pandas as pd

# Provided data
# Load the CSV file into a DataFrame
file_path = 'VentasOriginal.csv'

# Use try-except block to catch any potential exceptions
try:
    df1 = pd.read_csv(file_path)
    print('(1)','\n',df1.head())  # Optionally, print the first few rows to verify the data has been loaded correctly
except Exception as e:
    print("An error occurred:", e)
print('\n')

# Ejercicio 6: Filtrar las filas con ventas mayores a 10000
# Load the CSV file into a DataFrame
file_path = 'C:/Users/Usuario/Desktop/VentasOriginal.csv'
df = pd.read_csv(file_path)

print('(2)','\n','Filtrado ventas por vendedor')
sales_david = df[df['Vendedor'] == 'David']
print('Ventas per Vendedor')
print(sales_david)
print('\n')

print('(3)','\n','Promedio de ventas per Producto')
Sales_Producto = df.groupby('Producto')['Ventas'].mean()
print(Sales_Producto)
print('\n')

print('(4)','\n','ventas por orden decendiente')
DataFrame = df.sort_values(by = 'Ventas', ascending = False)
print(DataFrame)
print('\n')

#Ventas mayores a 10000
print ('(5)','\n','Filtrar las filas con ventas mayores a 10000')
df_filtrado = df[df['Ventas']>10000]
print('\n')
print(df_filtrado)
print('\n')

#Ejercicio 8: Eliminar la columna "Vendedor"
file_path = 'C:/Users/Usuario/Desktop/VentasOriginal.csv'
df = pd.read_csv(file_path)
print('(6)','\n','Eliminar la columna "Vendedor"')
print('\n')
df_sin_vendedor = df.drop(columns=['Vendedor'])
print(df_sin_vendedor)
print('\n')

# Ejercicio 9: Calcular el total de ventas por región
print('(7)','\n','Calcular el total de ventas por región')
print('\n')
df_ventas_region = df.groupby('Region')['Ventas'].sum()
print(df_ventas_region)
print('\n')

# Ventas per producto
print('(8)','Calcular el total de las ventas por producto')
df_ventas_por_producto = df.groupby('Producto')['Ventas'].sum()
print(df_ventas_por_producto)

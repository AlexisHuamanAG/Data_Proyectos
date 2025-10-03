import pandas as pd

url = "https://unete.censos2025.com.pe/public/home/detalle/2/121"
tablas = pd.read_html(url)  # devuelve una lista de DataFrames

print(len(tablas))  
df = tablas[0]  
df.to_csv(r"C:\Users\Usuario\Desktop\Proyectos\CENSISTAS\vacantes.csv",index=False)

print(df.head())


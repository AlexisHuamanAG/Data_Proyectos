import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

import requests
import pandas as pd
from datetime import datetime


fuentes = {
    "Kambista": "https://api.kambista.com/v1/exchange/calculates?originCurrency=USD&destinationCurrency=PEN&amount=100&active=S",
    
}

datos = []

for nombre, url in fuentes.items():
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            compra = data["tc"]["bid"]
            venta = data["tc"]["ask"]
            
            datos.append({
                "Fuente": nombre,
                "Compra": compra,
                "Venta": venta,
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        else:
            print(f"Error en {nombre}: {r.status_code}")
    except Exception as e:
        print(f"Fallo en {nombre}: {e}")


df = pd.DataFrame(datos)

df.to_csv("tipos_de_cambio.csv", index=False, encoding="utf-8-sig")

print(df)
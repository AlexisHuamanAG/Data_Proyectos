import requests
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

# API Kambista
def get_kambista(amount=1500):
    url = f"https://api.kambista.com/v1/exchange/calculates?originCurrency=USD&destinationCurrency=PEN&amount={amount}&active=S"
    response = requests.get(url).json()
    
    return {
        "Casa": "Kambista",
        "Compra": float(response["tc"]["bid"]),
        "Venta": float(response["tc"]["ask"])
    }



def get_rextie():
    url = "https://app.rextie.com/api/v1/fxrates/rate/?origin=template-original&commit=false&utm_source=cuanto-esta-el-dolar&utm_medium=cced_listado&utm_campaign=landing_nuevo&utm_term=listado&utm_content="
    
    response = requests.post(url, json={})
    data = response.json()
    
    return {
        "Casa": "Rextie",
        "Compra": float(data["fx_rate_buy"]),
        "Venta": float(data["fx_rate_sell"])
    }

def main():
    datos = []
    datos.append(get_kambista())   
    datos.append(get_rextie())    

    df = pd.DataFrame(datos)
    print(df)
    # Guardar a CSV para Power BI
    df.to_csv("casas_cambio.csv", index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    main()
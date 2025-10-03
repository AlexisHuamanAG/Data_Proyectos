import requests
import pandas as pd
import numpy as np  
import os
from datetime import datetime
import traceback


def get_kambista(amount=1500):
    try:
        url = f"https://api.kambista.com/v1/exchange/calculates?originCurrency=USD&destinationCurrency=PEN&amount={amount}&active=S"
        response = requests.get(url, timeout=5).json()
        return {
            "Casa": "Kambista",
            "Compra": float(response["tc"]["bid"]),
            "Venta": float(response["tc"]["ask"])
        }
    except Exception as e:
        print("Error Kambista:", e)
        return {"Casa": "Kambista", "Compra": np.nan, "Venta": np.nan}

def get_rextie():
    try:
        url = "https://app.rextie.com/api/v1/fxrates/rate/?origin=template-original&commit=false&utm_source=cuanto-esta-el-dolar&utm_medium=cced_listado&utm_campaign=landing_nuevo&utm_term=listado&utm_content="
        response = requests.post(url, json={}, timeout=5).json()
        return {
            "Casa": "Rextie",
            "Compra": float(response["fx_rate_buy"]),
            "Venta": float(response["fx_rate_sell"])
        }
    except Exception as e:
        print("Error Rextie:", e)
        return {"Casa": "Rextie", "Compra": np.nan, "Venta": np.nan}

def get_cambio_seguro():
    try:
        url = "https://api.cambioseguro.com/api/v1.1/config/rates"
        response = requests.get(url, timeout=5).json()
        return {
            "Casa": "Cambio Seguro",
            "Compra": float(response["data"]["purchase_price"]),
            "Venta": float(response["data"]["sale_price"])
        }
    except Exception as e:
        print("Error Cambio Seguro:", e)
        return {"Casa": "Cambio Seguro", "Compra": np.nan, "Venta": np.nan}

def get_cambiafx():
    try:
        url = "https://apiluna.cambiafx.pe/api/BackendPizarra/getTcCustomerNoAuth?idParCurrency=1"
        response = requests.get(url, timeout=5).json()
        data = response[0]
        return {"Casa": "Cambia FX", "Compra": float(data["tcBuy"]), "Venta": float(data["tcSale"])}
    except Exception as e:
        print("Error Cambia FX:", e)
        return {"Casa": "Cambia FX", "Compra": np.nan, "Venta": np.nan}

def get_western_union():
    try:
        url = "https://apiluna.cambiafx.pe/api/BackendPizarra/getTcCustomerNoAuth?idParCurrency=1"
        response = requests.get(url, timeout=5).json()
        data = response[0]
        return {"Casa": "Cambia FX", "Compra": float(data["tcBuy"]), "Venta": float(data["tcSale"])}
    except Exception as e:
        print("Error Cambia FX:", e)
        return {"Casa": "Cambia FX", "Compra": np.nan, "Venta": np.nan}

def get_cambiodigital():
    urls = {
        "Compra": "https://cambiodigitalperu.com/ajax/dolar-compra.php",
        "Venta": "https://cambiodigitalperu.com/ajax/dolar-venta.php"
    }
    
    resultado = {"Casa": "Cambio Digital"}

    try:
        for key, url in urls.items():
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            resultado[key] = float(response.text.strip())
        return resultado

    except Exception as e:
        print("Error Cambio Digital:", e)
        return {"Casa": "Cambio Digital", "Compra": None, "Venta": None}

def main():
    datos = []
    for func in [get_kambista, get_rextie, get_cambio_seguro, get_cambiafx, get_cambiodigital]:
        resultado = func()       
        resultado["Fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        datos.append(resultado)

    df = pd.DataFrame(datos)
    print(df)

    archivo = r"C:\Users\Usuario\Desktop\Proyectos\TIPO DE CAMBIO\casas_cambio.csv"
    if os.path.exists(archivo):
       
        df.to_csv(archivo, mode='a', index=False, header=False, encoding="utf-8-sig")
    else:
      
        df.to_csv(archivo, index=False, encoding="utf-8-sig")

try:
    main()
except Exception as e:
    with open(r"C:\Users\Usuario\Desktop\Proyectos\TIPO DE CAMBIO\error_log.txt", "a") as f:
        f.write(str(e) + "\n")
        f.write(traceback.format_exc() + "\n")

# if __name__ == "__main__":
#     while True:
#         main()
#         print("Esperando 10 segundos...\n")
#         time.sleep(10)


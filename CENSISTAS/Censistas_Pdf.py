import camelot
import pandas as pd


archivo_pdf = r"C:\Users\Usuario\Desktop\Proyectos\Censistas_Aprobados.pdf"

paginas_totales = 1052  
bloque_paginas = 10    
flavor = 'lattice'     

dfs = []


for inicio in range(1, paginas_totales + 1, bloque_paginas):
    fin = min(inicio + bloque_paginas - 1, paginas_totales)
    rango_paginas = f"{inicio}-{fin}"
    
    print(f"Procesando páginas {rango_paginas}...")
    tablas = camelot.read_pdf(archivo_pdf, pages=rango_paginas, flavor=flavor)
    
    if tablas:
        dfs.extend([t.df for t in tablas])
        print(f"  → Se extrajeron {len(tablas)} tablas en este bloque")
    else:
        print("  → No se detectaron tablas en este bloque")


if dfs:
    df_total = pd.concat(dfs, ignore_index=True)
    
    df_total = df_total.drop_duplicates().reset_index(drop=True)
    
    # Guardar en CSV
    df_total.to_csv(r"C:\Users\Usuario\Desktop\Proyectos\tabla_censistas.csv", index=False)
    print(f"\n✅ CSV final guardado con {len(df_total)} filas y {len(df_total.columns)} columnas")
else:
    print("❌ No se extrajeron tablas de todo el PDF")


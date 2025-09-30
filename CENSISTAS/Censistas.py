import pandas as pd

df=pd.read_csv(r"C:\Users\Usuario\Desktop\Proyectos\CENSISTAS\tabla_censistas.csv")
df=df.drop(columns="NRO_CONV")

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].map(lambda x: x.strip().upper() if isinstance(x, str) else x)

relevante=df[["DESC_SEDE","DESC_SUB_SEDE","POSTULANTE"]]
relevante.to_csv("censistas_postulantes.csv", index=False)
# print(nuevo)

print(df.duplicated().sum())
print(df.info())
print(df.isna().sum())

# print(nuevo.value_counts("DESC_SEDE"))
# print(nuevo.value_counts("DESC_SUB_SEDE"))
grupo_lima=df.groupby("DESC_SUB_SEDE")["POSTULANTE"].count().sort_values(ascending=False, inplace=False).head(10)
# print(grupo_lima)


df1=pd.read_csv(r"C:\Users\Usuario\Desktop\Proyectos\vacantes.csv",header=0)
# print(df1.columns.tolist())
# print(df1.duplicated().sum())
# print(df1.info())
# print(df1.isna().sum())
df1["SUBSEDE DEPARTAMENTAL"] = df1["SUBSEDE DEPARTAMENTAL"].str.split(":").str[0].str.strip()
vacantes_final=df1[["SEDE DEPARTAMENTAL","SUBSEDE DEPARTAMENTAL","PERSONAL A CONTRATAR","PERSONAL A CAPACITAR"]]
vacantes_final.to_csv("vacantes_final.csv",index=False)
print(vacantes_final)

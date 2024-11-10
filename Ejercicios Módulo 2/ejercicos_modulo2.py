import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt


# INTENTO EJERCICIO 3

# df = pd.read_csv("/Users/danny.gomez/Documents/Git/Ejercicios Módulo 2/big_bang_theory_dataset.csv")

# sheldon_speaker = df[df['Speaker'] == 'Sheldon']

# penny_location = sheldon_speaker[sheldon_speaker['Text'] == "Penny."]['Location']

# penny_contains_text = sheldon_speaker[sheldon_speaker['Text'].str.contains("Penny", case=False, na=False)]['Location']

# plt.figure(figsize=(14, 5))

# plt.hist(penny_location, bins=10, alpha=0.5, label="Exactamente 'Penny'")

# plt.hist(penny_contains_text, bins=10, alpha=0.5, label="Frase con 'Penny'")
# plt.title("Localizaciones donde Sheldon menciona a Penny")
# plt.xlabel("Localización")
# plt.ylabel("Frecuencia")
# plt.legend()
# plt.show()

#EJERCICIO 3
df = pd.read_csv("/Users/danny.gomez/Documents/Git/Ejercicios Módulo 2/big_bang_theory_dataset.csv")

df[df['Text'] == "Penny."]
bool_mask = (df["Text"] == "Penny.") & (df["Speaker"] == "Sheldon")

df_penny = df [bool_mask]
y = df_penny.groupby ("Location").count()['Text']
x = df_penny ["Location"].unique()
plt.title("Localizaciones donde Sheldon menciona 'Penny.'")
plt.bar (x, y)
plt.xticks (rotation=45)
plt.show()


#EJERCICIO 4

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/danny.gomez/Documents/Git/Ejercicios Módulo 2/big_bang_theory_dataset.csv")

df = df.dropna(subset=['Speaker', 'Location'])

df_unique_locations = df.drop_duplicates(subset=['Location'])

plt.figure(figsize=(12, 6)) #SE APRECUA MEJOR EN EL COLAB 
plt.scatter(df_unique_locations['Speaker'], df_unique_locations['Location'], alpha=0.5)
plt.title("Escena por Personaje")
plt.xlabel("Personaje")
plt.ylabel("Localización")
plt.xticks(rotation=45)
plt.show()

#EJERCICIO #5
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("/Users/danny.gomez/Documents/Git/Ejercicios Módulo 2/big_bang_theory_dataset.csv")

#Columna si la frase contiene Penny
df['cant_menciones_penny'] = df['Text'].str.contains("Penny", case=False, na=False).astype(int)

#Se Agrupa por temporada y personaje, y contar el número de menciones de Penny
grupoPersTemp = df.groupby(['Season', 'Speaker']).agg({'cant_menciones_penny': 'sum'}).reset_index()

#Se crean los indices 
grupoPersTemp['personaje_temporada'] = grupoPersTemp['Speaker'] + " Temp " + grupoPersTemp['Season'].astype(str)
grupoPersTemp['group_index'] = grupoPersTemp.groupby(['Season', 'Speaker']).ngroup()


X = grupoPersTemp[['cant_menciones_penny']].values
y = grupoPersTemp['Speaker'].factorize()[0]

#Modelo de regresión logística
log_reg = LogisticRegression()
log_reg.fit(X, y)


print("Etiquetas de personaje y temporada:\n", grupoPersTemp[['personaje_temporada', 'cant_menciones_penny']])
print("ADICIONAL: ")
print("Coeficientes de regresión logística:", log_reg.coef_)
print("Intercepción:", log_reg.intercept_)
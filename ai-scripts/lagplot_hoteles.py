import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import lag_plot
from sklearn.linear_model import LinearRegression


# Cargar el CSV
df = pd.read_csv("ocupacion_hotelera.csv", sep=",")  # Ajusta el separador si es necesario

# Lista de hoteles únicos
hoteles = df["hotel_nombre"].unique()

# Diccionario para almacenar predicciones
predicciones = {}


# Crear lag plots y generar dummies temporales para cada hotel
for hotel in hoteles:
    df_hotel = df[df["hotel_nombre"] == hotel].sort_values("fecha").reset_index(drop=True)
    
    # Copia del dataframe
    df_hotel_with_features = df_hotel.copy()
    
    # Crear variable de tiempo
    # df_hotel_with_features["Time"] = np.arange(len(df_hotel.index))
    
    # Training data
    # X = df_hotel_with_features.loc[:, ['Time']]  # features
    # y = df_hotel_with_features.loc[:, 'precio_promedio_noche']  # target
    
    df_hotel_with_features['Lag_1'] = df['precio_promedio_noche'].shift(1)
    
    X = df_hotel_with_features.loc[:, ['Lag_1']]
    X.dropna(inplace=True)  # drop missing values in the feature set
    y = df_hotel_with_features.loc[:, 'precio_promedio_noche']  # create the target
    y, X = y.align(X, join='inner')  # drop corresponding values in target

    model = LinearRegression()
    model.fit(X, y)
    
    y_pred = pd.Series(model.predict(X), index=X.index)
    
    # Guardar predicciones
    predicciones[hotel] = y_pred
    
df_predicciones = pd.DataFrame(predicciones)
df_predicciones.to_csv("predicciones_hoteles.csv")

    
    
    
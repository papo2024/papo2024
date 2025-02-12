# -*- coding: utf-8 -*-
"""Laboratorio_AD-B_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17VGYY1ImDY9xLeUQiQHlyxvYNn61qU4f
"""

import pandas as pd

# Cargar el dataset
df = pd.read_csv('CSV Laboratorio 3 AD-B.csv')

# 1. Verificar valores nulos
print("Valores nulos por columna:")
print(df.isnull().sum())

# 2. Contar filas duplicadas
print("\nCantidad de filas duplicadas:")
print(df.duplicated().sum())

# 3. Análisis de la columna 'City'
if 'City' in df.columns:
  print("\nConteo de valores en la columna 'City':")
  # Incluye NaN si los hay
  print(df['City'].value_counts(dropna=False))
else:
  print("\nLa columna 'City' no está presente en el dataset.")

import pandas as pd

# Cargar el dataset
df = pd.read_csv('CSV Laboratorio 3 AD-B.csv')

# 1. Manejo de valores nulos
print(df.isnull().sum())

# Reemplazar valores nulos en la columna 'Category' con 'Unknown'
df['Category'] = df['Category'].fillna('Unknown')
# Reemplazar valores nulos en la columna 'City' con 'Unknown City'

df['City'] = df['City'].fillna('Unknown City')

# Reemplazar valores nulos en la columna 'Value' con la mediana de la columna
if 'Value' in df.columns:
  df['Value'] = df['Value'].fillna(df['Value'].median())

# 2. Eliminar duplicados
df = df.drop_duplicates()

# 3. Normalización de formatos

# Convertir texto de la columna 'City' a minúsculas
if 'City' in df.columns:
   df['City'] = df['City'].str.lower()

# Estandarizar fechas al formato AAAA/MM/DD
if 'Date' in df.columns:
  df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y/%m/%d')

# Revisar cambios realizados
print("Primeras filas del dataset después de la limpieza y normalización:")
print(df.head(5))

# Exportar el dataset limpio (opcional)
df.to_csv('Laboratorio_AD-B3.csv', index=False)
print("Dataset limpio guardado como 'Laboratorio_AD-B3.csv'.")
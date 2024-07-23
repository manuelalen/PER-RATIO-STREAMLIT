import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt

# Configuración de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Reemplaza 'your-google-sheet-id' con el ID de tu Google Sheets
sheet = client.open_by_key("1kfWmcm3XaPjpJmiF0EAFTnjUA49WVZjX7MNY4RRQo6k").sheet1

# Cargar los datos
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Calcular el P/E ratio promedio por industria
average_pe = df.groupby('Industry')['P/E Ratio'].mean().reset_index()

# Calcular el P/E ratio promedio general
overall_average_pe = df['P/E Ratio'].mean()

# Streamlit app
st.title('P/E Ratio by Industry')

# Sidebar para la selección de industria
selected_industry = st.sidebar.selectbox('Select Industry', average_pe['Industry'].unique())

# Filtrar los datos según la industria seleccionada
filtered_data = average_pe[average_pe['Industry'] == selected_industry]

# Graficar los datos
fig, ax = plt.subplots()
ax.bar(average_pe['Industry'], average_pe['P/E Ratio'], color='skyblue')
ax.axhline(overall_average_pe, color='red', linestyle='--', label=f'Overall Average P/E Ratio: {overall_average_pe:.2f}')
ax.set_xlabel('Industry')
ax.set_ylabel('Average P/E Ratio')
ax.set_title('Average P/E Ratio by Industry')
ax.legend()

# Mostrar la gráfica
st.pyplot(fig)

# Mostrar los datos filtrados
st.write(f'Average P/E Ratio for {selected_industry}: {filtered_data["P/E Ratio"].values[0]:.2f}')

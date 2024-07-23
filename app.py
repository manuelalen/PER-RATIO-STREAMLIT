import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo Excel
df = pd.read_excel('PERs.xlsx')

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

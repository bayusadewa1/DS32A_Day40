import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px

def tampilkan():
    st.title("Proyek Data Science")
    
    st.write("""
    ### Visualisasi Data Interaktif
    Berikut beberapa contoh visualisasi data interaktif yang saya buat menggunakan Plotly.
    """)
    
    # Example 1: Random Data Line Chart
    st.markdown("#### Contoh Line Chart")
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    fig = px.line(data, title="Contoh Line Chart Interaktif")
    st.plotly_chart(fig)
    
    # Example 2: Filtered Data
    st.markdown("#### Filter Data Interaktif")
    range_slider = st.slider("Pilih range nilai:", 0, 100, (25, 75))
    filtered_data = data[(data['A']*100 >= range_slider[0]) & (data['A']*100 <= range_slider[1])]
    st.write(f"Data terfilter (range {range_slider}):")
    st.dataframe(filtered_data)
    
    # Example 3: Interactive Scatter Plot
    st.markdown("#### Contoh Scatter Plot")
    scatter_data = pd.DataFrame({
        'X': np.random.randn(100),
        'Y': np.random.randn(100),
        'Category': np.random.choice(['A', 'B', 'C'], 100)
    })
    fig2 = px.scatter(scatter_data, x='X', y='Y', color='Category', 
                     title="Scatter Plot dengan Kategori")
    st.plotly_chart(fig2)
    
    st.markdown("""
    ### Proyek Lainnya
    - **Analisis Sentimen Media Sosial**: Membangun model klasifikasi teks untuk analisis sentimen
    - **Sistem Rekomendasi Produk**: Mengembangkan sistem rekomendasi berbasis collaborative filtering
    - **Prediksi Harga Saham**: Membuat model time series forecasting untuk prediksi harga saham
    """)
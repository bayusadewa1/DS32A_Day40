import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def prediksi():
    st.title("✈️ Flight Customer Segmentation")
    st.markdown("""
    **Segment your airline customers based on their flight behavior and characteristics**

    This interactive tool uses K-Means clustering to group customers with similar flight patterns.
    Use the sidebar to adjust clustering parameters and explore different customer segments.
    """)
    
    # Sidebar for user inputs
    st.sidebar.header("Clustering Parameters")
    n_clusters = st.sidebar.slider("Number of Clusters", 2, 10, 4)
    selected_features = st.sidebar.multiselect(
        "Select Features for Clustering",
        options=['FLIGHT_COUNT', 'BP_SUM', 'SEG_KM_SUM', 'Points_Sum', 'avg_discount', 'AGE'],
        default=['FLIGHT_COUNT', 'BP_SUM', 'SEG_KM_SUM', 'Points_Sum']
    )

    # Load data
    @st.cache_data
    def load_data():
        df = pd.read_csv('flight.csv')
        
        # Data preprocessing similar to the notebook
        df_clean = df.copy()
        
        # Handle missing values
        missing_col = ['SUM_YR_1', 'AGE', 'SUM_YR_2', 'WORK_COUNTRY', 'GENDER']
        for col in missing_col:
            df_clean.dropna(subset=[col], inplace=True)
        
        df_clean['WORK_CITY'].fillna(df_clean['WORK_CITY'].mode()[0], inplace=True)
        df_clean['WORK_PROVINCE'].fillna(df_clean['WORK_PROVINCE'].mode()[0], inplace=True)
        
        # Convert data types
        df_clean['AGE'] = df_clean['AGE'].astype(int)
        
        return df_clean

    df = load_data()

    # Show raw data option
    if st.checkbox("Show Raw Data"):
        st.subheader("Raw Data")
        st.write(df)

    # Clustering section
    st.header("Customer Segmentation Analysis")

    # Check if features are selected
    if not selected_features:
        st.warning("Please select at least one feature for clustering")
        st.stop()

    # Prepare data for clustering
    X = df[selected_features]

    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X_scaled)

    # Add cluster labels to dataframe
    df['Cluster'] = clusters

    # Display cluster sizes
    st.subheader("Cluster Distribution")
    cluster_counts = df['Cluster'].value_counts().sort_index()
    st.bar_chart(cluster_counts)

    # Cluster characteristics
    st.subheader("Cluster Characteristics")
    cluster_means = df.groupby('Cluster')[selected_features].mean()
    st.dataframe(cluster_means.style.background_gradient(cmap='Blues'))

    # Visualization
    st.subheader("Cluster Visualization")

    # Select features for visualization
    viz_features = st.multiselect(
        "Select Features for Visualization",
        options=selected_features,
        default=selected_features[:2] if len(selected_features) >= 2 else selected_features
    )

    if len(viz_features) >= 2:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(
            data=df,
            x=viz_features[0],
            y=viz_features[1],
            hue='Cluster',
            palette='viridis',
            ax=ax
        )
        ax.set_title(f"Cluster Visualization: {viz_features[0]} vs {viz_features[1]}")
        st.pyplot(fig)
    else:
        st.warning("Please select at least 2 features for visualization")

    # Display customers in each cluster
    st.subheader("Explore Customers by Cluster")
    selected_cluster = st.selectbox("Select Cluster to View", sorted(df['Cluster'].unique()))
    st.dataframe(df[df['Cluster'] == selected_cluster].head(20))

    # Cluster interpretation
    st.subheader("Cluster Interpretation")
    st.write("""
    Based on the cluster characteristics above, you can interpret each cluster as follows:
    - **High-Value Customers**: High flight counts, long distances, and many points
    - **Medium-Value Customers**: Moderate flight activity
    - **Low-Value Customers**: Infrequent flyers with low points
    - **Discount Seekers**: Customers who frequently use discounts (if 'avg_discount' is selected)

    Adjust the number of clusters and selected features in the sidebar to refine your segmentation.
    """)

    # Download clustered data
    st.subheader("Download Clustered Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='clustered_customers.csv',
        mime='text/csv',
    )

    # Footer
    st.markdown("---")
    st.markdown("""
    **Note**: This application uses K-Means clustering to segment flight customers based on their behavior.
    Adjust the parameters in the sidebar to explore different clustering configurations.
    """)
import streamlit as st

def tampilkan_kontak():
    st.title("Kontak")
    st.write("""
    Saya selalu terbuka untuk diskusi tentang proyek data science, kolaborasi, atau kesempatan kerja. 
    Jangan ragu untuk menghubungi saya melalui salah satu saluran berikut:
    """)
    
    # Contact cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### LinkedIn
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/bayusadewaazyumardi/)
        
        Terhubung dengan saya di LinkedIn untuk jaringan profesional dan pembaruan karir.
        """)
        
    with col2:
        st.markdown("""
        ### GitHub
        [![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/bayusadewa1)
        
        Lihat proyek open source dan repositori kode saya di GitHub.
        """)
    
    # Additional contact info
    st.markdown("""
    ### Informasi Kontak Lainnya
    
    📧 **Email**: bayu.sdwa.43@gmail.com  
    📱 **Telepon**: +62 819-9369-5432  
    🌐 **Website**: coming soon
    
    ### Formulir Kontak
    Kirim pesan langsung kepada saya:
    """)
    
    with st.form("contact_form"):
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Alamat Email")
        message = st.text_area("Pesan Anda")
        submitted = st.form_submit_button("Kirim Pesan")
        
        if submitted:
            st.success(f"Terima kasih {name}! Pesan Anda telah terkirim. Saya akan segera menghubungi Anda kembali.")
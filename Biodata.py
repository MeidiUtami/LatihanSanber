import streamlit as st

#set_page_config
st.set_page_config(
    page_title="Portofolio Web App",
    layout="wide"
)

#with st.container():
col_1, col_2, col_3, col_4 = st.columns([1,1,2,1])
with col_1:
    img_path = st.secrets.path_configuration['path_image']
    berkas_foto = "OIP2.gif"
    st.image(image=f"{img_path}{berkas_foto}")

with col_3:
    st.subheader("MEIDI UTAMI, S.ST")
    title = '<p style="font-family:Courier; color:Black; font-Size: 20px; font-wight: bold">-CHEMICAL ENGINEERING-</p>'
    st.markdown(title, unsafe_allow_html=True)
    teks = '''
    Pangkajene, 20 May 1996
    Tamalate, Moncongloe Bulu, Maros
    meidiutamihamzah@gmail.com
    linkedin.com/in/meidi-utami
    '''
    st.markdown(f'<p style="font-family:Courier; color:Black; font-Size: 20px; font-wight: bold">{teks}</p>', unsafe_allow_html=True)
        
st.divider()

with st.container():
    st.subheader("QUALITY CONTROL | DATA SCIENCE AND MACHINE LEARNING ENTHUSIAST")
    perkenalan = '''
    Bachelor Degree of Chemical Engineering at Politeknik Negeri Ujung Pandang who has experience as Laboratory Quality Control staff. 
    Experienced in managing college student and volunteer organizations with adaptive, loyalty and responsibility abilities in managing each activities project. 
    Have work interests related to analysis, Quality Control, administration and research and development (R&D). 
    Also have completed several online courses on Data Science, SQL, and Python, and passionate about applying data-driven solutions to real-world problems.
    '''
    st.markdown(f'<p style="font-family:Courier; color:Black; font-Size: 20px; font-wight: bold">{perkenalan}</p>', unsafe_allow_html=True)

st.divider()

with st.container():
    st.subheader("EDUCATION")
    with st.container():
        pendidikan = '''
        Bachelor Degree of Engineering (S.ST.) in Chemical Engineering, Chemical Industry Technology
        Politeknik Negeri Ujung Pandang, GPA: 3.78 (Cum Laude)
        '''
        col_1, col_2= st.columns([30,5])
        col_1.markdown(f'<p style="font-family:Courier; color:Black; font-Size: 20px; font-wight: bold">{pendidikan}</p>', unsafe_allow_html=True)
        col_2.text("08/2014-11/2018")

st.divider()

with st.container():
    st.subheader("WORK EXPERIENCES")
    #pengalaman 1
    with st.container():
        col_1, col_2, col_3= st.columns([4,26,5])
        col_1.caption("Chemical Analyst")
        col_2.text("PT. Gunbuster Nickel Industry, Morowali – Indonesia")
        col_3.text("09/2022-12/2023")
        
        with st.container():        
            col_1, col_2, col_3= st.columns([4,26,5])
            col_2.text('''
                    - Prepare ore samples using a hydraulic pellet press and fused bead tool.
                    - Analyze ore samples using Bruker S8 Tiger WDXRF instrument.
                    - Generate daily, weekly, monthly analysis and QAQC reports of ore samples.
                    ''')
    
    #pengalaman 2
    with st.container():
        col_1, col_2, col_3= st.columns([4,26,5])
        col_1.caption("Wet Lab Analyst")
        col_2.text("PT. Perkasa Agung Sejati, Makassar – Indonesia")
        col_3.text("01/2019-05/2023")
        
        with st.container():        
            col_1, col_2, col_3= st.columns([4,26,5])
            col_2.text('''
                    - Carry out sample preparation, analyze raw materials and final products for poultry feed 
                      using proximate analysis methods (protein, fat, moisture content, fiber), minerals and FFA.
                    - Analyze raw materials and final products for poultry feed using DS 2500 Near Infrared (NIR)
                      device.
                    - Generate daily, weekly and monthly analysis reports of raw materials and final poultry feed 
                      products.
                    - Carry Out analysis of local/seasonal raw materials (corn and bran) ; 
                      (screen test analysis, moisture content analysis and aflatoxin analysis).
                    ''')

    #pengalaman 3       
    with st.container():
        col_1, col_2, col_3= st.columns([4,26,5])
        col_1.caption("Internship")
        col_2.text("PT. Makassar Tene, Makassar – Indonesia")
        col_3.text("02/2018-03/2018")
        
        with st.container():        
            col_1, col_2, col_3= st.columns([4,26,5])
            col_2.text('''
                    - Prepare and analyze samples for moisture content, color, ash, polarization 
                      and reducing sugar in raw sugar and product sugar.
                    - Determine the MA/CV of refined sugar and the effective CaO content of lime milk.
                    ''')

st.divider()
    
with st.container():
    st.subheader("LICENSES & CERTIFICATIONS")
    #sertifikat 1
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Belajar Analisis Data dengan Phyton, Dicoding Indonesia")
        col_2.text("12/2023-12/2026")
    
    #sertifikat 2
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Belajar Dasar Structured Query Language (SQL), Dicoding Indonesia")
        col_2.text("12/2023-12/2026")

    #sertifikat 3
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Belajar Dasar Visualisasi Data, Dicoding Indonesia")
        col_2.text("12/2023-12/2026")

    #sertifikat 4
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Belajar Machine Learning untuk Pemula, Dicoding Indonesia")
        col_2.text("12/2023-12/2026")

    #sertifikat 5
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Memulai Pemrograman dengan Phyton, Dicoding Indonesia")
        col_2.text("12/2023-12/2026")

    #sertifikat 6
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Belajar Data Science, Dicoding Indonesia")
        col_2.text("11/2023-11/2026")

    #sertifikat 7
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Tes Potensi Akademik, UUO-PT BAPPENAS (Score: 517,18)")
        col_2.text("06/2022-06/2024")

    #sertifikat 8
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("TOEFL ITP, Central International Education (Score: 527)")
        col_2.text("03/2022-03/2024")   

st.divider()

with st.container():
    st.subheader("TRAINING & DEVELOPMENT")
    #training 1
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Full Stack Data Science Sanber Campus X ITB (Batch 1), Santai Berkualitas Syberindo")
        col_2.text("10/2023-Present")
    
    #training 2
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Pelatihan WDXRF S8 – Tiger, Dynatech")
        col_2.text("30 – 31 July 2023")

    #training 3
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Pelatihan Awareness Training Integrated Management System (IMS) – QHSE Batch 9, Makin Ahli")
        col_2.text("19 February 2023")

st.divider()

with st.container():
    st.subheader("ORGANIZATIONAL EXPERIENCES")
    #training 1
    with st.container():
        col_1, col_2 = st.columns([30,5])
        col_1.text("Staff UKH Ristek, Himpunan Mahasiswa Teknik Kimia PNUP")
        col_2.text("08/2015-08/2017")

st.divider()



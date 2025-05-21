import streamlit as st
import pandas as pd
from catboost import CatBoostClassifier
import matplotlib.pyplot as plt

import seaborn as sns
# Load model
@st.cache_resource
def load_model():
    model = CatBoostClassifier()
    model.load_model("catboost_cirrhosis_model.cbm")
    return model

model = load_model()

# Sidebar
st.sidebar.title(" Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["📊 Prediksi Sirosis", "ℹ️ Tentang" ,"penanganan sirosis","dataset📊"])

# Halaman prediksi
if page == "📊 Prediksi Sirosis":
    st.title("Prediksi Tahap Sirosis Liver")
    st.write("Masukkan data pasien untuk memprediksi stage sirosis (1 - 4) ")

    # Input pengguna
    age = st.number_input("Umur", min_value=1, max_value=120, value=50)
    ascites = st.selectbox("Ascites", ["Y", "N"])
    hepatomegaly = st.selectbox("Hepatomegaly", ["Y", "N"])
    edema = st.selectbox("Edema", ["N", "S", "Y"])
    bilirubin = st.number_input("Bilirubin", min_value=0.0, value=1.0)
    cholesterol = st.number_input("Cholesterol", min_value=0.0, value=200.0)
    albumin = st.number_input("Albumin", min_value=0.0, value=3.5)
    copper = st.number_input("Copper", min_value=0.0, value=50.0)
    alk_phos = st.number_input("Alkaline Phosphatase", min_value=0.0, value=100.0)
    sgot = st.number_input("SGOT", min_value=0.0, value=100.0)
    platelets = st.number_input("Platelets", min_value=0.0, value=250.0)
    prothrombin = st.number_input("Prothrombin", min_value=0.0, value=10.0)

    # Prediksi
    if st.button("🔍 Prediksi"):
        input_df = pd.DataFrame([{
            "Age": age,
            "Ascites": ascites,
            "Hepatomegaly": hepatomegaly,
            "Edema": edema,
            "Bilirubin": bilirubin,
            "Cholesterol": cholesterol,
            "Albumin": albumin,
            "Copper": copper,
            "Alk_Phos": alk_phos,
            "SGOT": sgot,
            "Platelets": platelets,
            "Prothrombin": prothrombin,
        }])

        prediction = model.predict(input_df)[0]
        st.success(f"🔬 Prediksi Tahap Sirosis: **Stage {int(prediction)}**")

# Halaman tentang
elif page == "ℹ️ Tentang":
    st.title("Bahaya Sirosis Hati: Dari Tahap 1 hingga Tahap 4")
    st.markdown("""
    Aplikasi ini memprediksi **tahap sirosis hati** berdasarkan data medis pasien menggunakan model **CatBoost Classifier**.
    Memahami tahapan sirosis hati sangat penting untuk penanganan dan prognosis yang lebih baik. Sirosis adalah kondisi progresif di mana hati mengalami kerusakan permanen.
    """)

    st.markdown("---")
    st.image("sirosis-hati.jpg")
    st.subheader("Tahap 1: Kompensasi")
   
    # Ganti 'path/to/image_stage1.jpg' dengan path sebenarnya ke gambar Anda
    
    st.markdown("""
    Pada tahap ini, **hati masih dapat berfungsi dengan baik** meskipun sudah ada jaringan parut. Seringkali, tidak ada gejala yang terlihat atau gejala yang sangat ringan.
    Hati masih mampu mengimbangi kerusakannya. Deteksi dini pada tahap ini memberikan kesempatan terbaik untuk memperlambat atau menghentikan progresivitas penyakit.
    """)

    st.markdown("---")

    st.subheader("Tahap 2: Kompensasi dengan Komplikasi (Ringan)")
    # Ganti 'path/to/image_stage2.jpg' dengan path sebenarnya ke gambar Anda

    st.markdown("""
    Sirosis pada tahap ini mulai menunjukkan komplikasi ringan, seperti **kelelahan yang lebih sering** atau **perubahan kecil dalam fungsi hati**.
    Meskipun hati masih mampu "berkompensasi", beban kerjanya semakin berat dan mulai muncul tanda-tanda kerusakan yang lebih jelas, meskipun belum parah.
    """)

    st.markdown("---")

    st.subheader("Tahap 3: Dekompensasi (Parah)")
    # Ganti 'path/to/image_stage3.jpg' dengan path sebenarnya ke gambar Anda

    st.markdown("""
    Ini adalah tahap di mana **hati sudah tidak mampu berfungsi secara optimal**. Gejala-gejala menjadi lebih jelas dan parah, termasuk:
    * **Asites** (penumpukan cairan di perut)
    * **Ensefalopati hepatik** (masalah fungsi otak karena penumpukan racun)
    * **Perdarahan varises** (pembuluh darah di kerongkongan atau perut yang membesar dan mudah berdarah)
    * **Jaundice** (kulit dan mata menguning)

    Pada tahap ini, pasien seringkali membutuhkan penanganan medis yang intensif untuk mengelola komplikasi.
    """)

    st.markdown("---")

    st.subheader("Tahap 4: Dekompensasi Tingkat Lanjut/Gagal Hati Terminal")
    # Ganti 'path/to/image_stage4.jpg' dengan path sebenarnya ke gambar Anda
 
    st.markdown("""
    Ini adalah **tahap akhir sirosis hati**, di mana hati telah mengalami kerusakan yang sangat parah dan tidak dapat berfungsi lagi.
    Komplikasi yang terjadi sangat serius dan mengancam jiwa. Pada tahap ini, **transplantasi hati** seringkali menjadi satu-satunya pilihan untuk kelangsungan hidup.

    ---

    **Fitur input yang digunakan untuk prediksi:**
    Umur, Ascites, Hepatomegaly, Edema, Bilirubin, Cholesterol, Albumin, Copper, Alk_Phos, SGOT, Platelets, Prothrombin.

    Dikembangkan oleh: **Kelompok 7**
    """)

elif page == "penanganan sirosis":
    st.title("Penanganan sirosis: Dari Tahap 1 hingga Tahap 4")
     
    st.markdown("""
    Penanganan sirosis hati sangat bergantung pada tahap keparahan penyakit dan penyebab yang mendasarinya. Tujuan utama pengobatan adalah untuk **memperlambat atau menghentikan progresivitas kerusakan hati**, **mengelola gejala**, dan **mencegah komplikasi**. Semakin dini sirosis terdeteksi dan diobati, semakin baik prognosisnya.
    """)

    st.markdown("---")

    st.subheader("Tahap 1: Sirosis Kompensasi")
    st.markdown("""
    Pada tahap ini, hati masih mampu menjalankan fungsinya dengan baik, dan gejalanya mungkin tidak ada atau sangat ringan. Penanganan berfokus pada:

    * **Mengatasi Penyebab Utama:** Ini adalah langkah terpenting. Misalnya, jika disebabkan oleh:
        * **Alkohol:** Penghentian total konsumsi alkohol.
        * **Hepatitis B atau C:** Pengobatan antivirus untuk menekan virus.
        * **Penyakit Hati Berlemak Non-Alkohol (NAFLD):** Penurunan berat badan, diet sehat, olahraga, dan kontrol gula darah/kolesterol.
        * **Penyakit Autoimun:** Obat imunosupresan.
    * **Perubahan Gaya Hidup:**
        * **Diet Sehat:** Batasi garam (untuk mencegah retensi cairan), hindari makanan olahan dan tinggi lemak.
        * **Menjaga Berat Badan Ideal:** Sangat penting, terutama untuk NAFLD.
        * **Olahraga Teratur:** Membantu kesehatan hati secara keseluruhan.
        * **Vaksinasi:** Vaksin hepatitis A dan B, flu, dan pneumonia untuk mencegah infeksi yang dapat memperburuk kondisi hati.
    * **Pemantauan Rutin:** Pemeriksaan darah dan pencitraan hati secara teratur untuk memantau kondisi dan mendeteksi komplikasi awal.
    """)

    st.markdown("---")

    st.subheader("Tahap 2: Sirosis Kompensasi dengan Komplikasi Ringan")
    st.markdown("""
    Selain penanganan seperti pada Tahap 1, pada tahap ini mungkin sudah mulai muncul komplikasi ringan yang memerlukan perhatian khusus:

    * **Pemberian Obat-obatan:** Untuk mengatasi gejala awal atau mencegah komplikasi agar tidak bertambah parah.
    * **Skrining untuk Komplikasi:** Dokter mungkin mulai melakukan skrining lebih sering untuk mencari tanda-tanda awal asites, varises esofagus, atau ensefalopati.
    * **Manajemen Gizi yang Lebih Ketat:** Konsultan gizi mungkin diperlukan untuk memastikan asupan nutrisi yang tepat dan mencegah malnutrisi.
    """)

    st.markdown("---")

    st.subheader("Tahap 3: Sirosis Dekompensasi (Parah)")
    st.markdown("""
    Pada tahap ini, hati sudah kesulitan berfungsi, dan komplikasi serius mulai muncul. Penanganan berfokus pada pengelolaan komplikasi ini:

    * **Asites (Penumpukan Cairan di Perut):**
        * **Pembatasan Garam Ketat:** Dalam diet.
        * **Diuretik:** Obat untuk membantu tubuh mengeluarkan kelebihan cairan melalui urine.
        * **Parasentesis:** Prosedur medis untuk mengeluarkan cairan dari perut jika diuretik tidak cukup.
    * **Ensefalopati Hepatik (Masalah Otak):**
        * **Laktulosa:** Obat untuk mengurangi penyerapan amonia (racun) di usus.
        * **Antibiotik:** Untuk mengubah flora usus dan mengurangi produksi racun.
    * **Perdarahan Varises Esofagus:**
        * **Obat Beta-blocker:** Untuk menurunkan tekanan di vena portal dan mengurangi risiko perdarahan.
        * **Ligasi Pita Endoskopik (EVL) atau Skleroterapi:** Prosedur untuk mengikat atau menyuntik varises yang berdarah.
        * **TIPS (Transjugular Intrahepatic Portosystemic Shunt):** Prosedur untuk membuat saluran baru di hati untuk mengurangi tekanan vena portal pada kasus yang parah.
    * **Infeksi:** Antibiotik untuk mengobati infeksi yang sering terjadi pada pasien sirosis.
    * **Pemantauan Fungsi Ginjal:** Sirosis lanjut dapat memengaruhi ginjal, sehingga pemantauan ketat diperlukan.
    """)

    st.markdown("---")

    st.subheader("Tahap 4: Sirosis Dekompensasi Tingkat Lanjut / Gagal Hati Terminal")
    st.markdown("""
    Ini adalah tahap akhir di mana hati telah rusak parah dan fungsinya sangat terganggu. Penanganan pada tahap ini bersifat paliatif dan mempersiapkan untuk pilihan terakhir:

    * **Manajemen Komplikasi yang Intensif:** Sama seperti Tahap 3, tetapi dengan penekanan yang lebih besar dan seringkali rawat inap.
    * **Transplantasi Hati:** Ini seringkali merupakan satu-satunya pilihan kuratif pada tahap ini. Pasien dievaluasi dan masuk dalam daftar tunggu transplantasi. Proses ini melibatkan pencarian hati donor yang cocok.
    * **Perawatan Paliatif:** Jika transplantasi bukan pilihan atau tidak memungkinkan, perawatan berfokus pada kenyamanan pasien dan manajemen gejala untuk meningkatkan kualitas hidup.

    ---

    **Penting:** Penanganan sirosis memerlukan pendekatan multidisiplin yang melibatkan dokter spesialis hati (hepatolog), ahli gizi, perawat, dan kadang-kadang ahli bedah. Kepatuhan pasien terhadap rencana pengobatan dan gaya hidup sangat krusial untuk keberhasilan penanganan.
    """)
elif page == "dataset📊":
    st.title("chart dataset")
    df = pd.read_csv("data_cleaned_12000.csv")
    # User input form
    

    # Identifikasi kolom numerik dan kategorikal
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_object_cols = df.select_dtypes(include=['object']).columns.tolist()

    # Kolom yang ingin divisualisasikan sebagai kategori (meskipun nilai bisa 0/1)
    categorical_display_cols = ['Ascites', 'Hepatomegaly', 'Edema', 'Stage']

    # Hapus kolom yang akan diplot sebagai kategori dari daftar kolom numerik
    numerical_cols = [col for col in numerical_cols if col not in categorical_display_cols]


    st.subheader("Visualisasi Fitur Numerik")
    for col in numerical_cols:
        st.markdown(f"#### Distribusi {col}")

        fig, ax = plt.subplots() # Buat satu plot per fitur
        sns.histplot(df[col].dropna(), kde=True, ax=ax)
        ax.set_title(f'Histogram {col}')
        ax.set_xlabel(col)
        ax.set_ylabel('Frekuensi')
        st.pyplot(fig)
        plt.close(fig) # Tutup figure untuk membebaskan memori
        st.markdown("---")

    st.subheader("Visualisasi Fitur Kategorikal")
    for col in categorical_display_cols:
        st.markdown(f"#### Distribusi {col}")
        fig, ax = plt.subplots()

        # Logic untuk melabeli kolom biner (0/1) menjadi 'No'/'Yes' di chart
        if col in ['Ascites', 'Hepatomegaly', 'Edema']:
            if df[col].dtype == 'object': # Jika masih string (misal 'Y'/'N' di CSV)
                display_series = df[col]
            else: # Jika sudah 0/1
                display_series = df[col].map({0: 'No', 1: 'Yes'})
        elif col == 'Stage':
            display_series = df[col].astype(str) # Pastikan 'Stage' diperlakukan sebagai string untuk bar chart
        else:
            display_series = df[col] # Untuk kolom kategorikal lain yang mungkin ada

        sns.countplot(x=display_series, ax=ax, palette='viridis')
        ax.set_title(f'Bar Chart {col}')
        ax.set_xlabel(col)
        ax.set_ylabel('Count')
        st.pyplot(fig)
        plt.close(fig) # Tutup figure untuk membebaskan memori
        st.markdown("---")

    st.markdown("""
    <br>
    Visualisasi ini membantu memahami karakteristik dan sebaran data yang digunakan untuk prediksi sirosis hati.
    """, unsafe_allow_html=True)
  
        
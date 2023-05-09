import streamlit as st

# Menambahkan CSS untuk mengubah warna judul menjadi hijau
st.markdown("""
    <style>
    .title {
        font-family: Helvetica;
        font-size: 5rem;
        color: #167042;
        text-align: center;
        padding-top: 50px;
    }
    </style> 
""", unsafe_allow_html=True)

# Menampilkan judul dengan kelas CSS "title"
st.markdown('<h1 class="title">Consa Meter</h1>', unsafe_allow_html=True)

st.subheader('Home')



st.caption('Konsentrasi terukur mengacu pada konsentrasi aktual atau nyata dari suatu zat dalam suatu sampel atau larutan. Ini adalah nilai konsentrasi yang diperoleh melalui proses pengukuran langsung atau metode analitis tertentu. Dalam pengukuran konsentrasi terukur, berbagai teknik dan instrumen dapat digunakan, tergantung pada jenis zat yang diukur dan metode analitis yang dipilih. Beberapa metode umum yang digunakan untuk mengukur konsentrasi terukur meliputi:')

st.caption('1. Titrasi: Metode titrasi digunakan untuk mengukur konsentrasi terukur dengan menambahkan larutan penyangga atau larutan reaktan yang diketahui ke dalam sampel dan mengamati perubahan warna atau perubahan sifat fisik lainnya. Dalam titrasi, konsentrasi terukur diperoleh berdasarkan volume larutan penyangga atau reaktan yang diperlukan untuk mencapai titik ekivalen.')
st.caption('2. Spektrofotometri: Metode spektrofotometri digunakan untuk mengukur konsentrasi terukur dengan mengukur absorbansi atau transmisi cahaya oleh sampel pada panjang gelombang tertentu. Ini melibatkan penggunaan spektrofotometer yang menghasilkan spektrum cahaya yang melewati sampel, dan konsentrasi terukur dihitung berdasarkan hukum Beer-Lambert.')
st.caption('3. Kromatografi: Metode kromatografi termasuk kromatografi gas (GC) dan kromatografi cair kinerja tinggi (HPLC) digunakan untuk memisahkan dan mengukur konsentrasi terukur zat tertentu dalam sampel kompleks. Konsentrasi terukur dihitung berdasarkan pemisahan dan deteksi kuantitatif zat target yang dihasilkan oleh sistem kromatografi.')
st.caption('4. Metode elektrokimia: Metode elektrokimia seperti elektrolisis, voltametri, dan amperometri digunakan untuk mengukur konsentrasi terukur zat berdasarkan respons listrik yang terjadi selama reaksi elektrokimia. Konsentrasi terukur dihitung berdasarkan arus atau potensial yang dihasilkan selama reaksi.')
st.caption('5. Metode gravimetri: Metode gravimetri melibatkan pengukuran berat sampel sebelum dan setelah reaksi atau pemisahan. Dalam metode ini, konsentrasi terukur dihitung berdasarkan perbedaan berat sampel sebelum dan setelah analisis.')

st.caption('Perhitungan konsentrasi terukur dapat melibatkan konversi unit, penggunaan persamaan matematika, dan faktor kalibrasi yang sesuai dengan metode pengukuran yang digunakan.')


st.subheader('Halo!')
st.subheader('Namaku Consa :sunglasses:')
st.subheader('Aku akan membantu kamu menghitung konsentrasi terukur')



st.header(':blue[_Konsentrasi Terukur_]')

st.caption('Masukkan Data Yang Kalian Punya')

y = st.number_input('Absorbansi', step=0.00001, format="%.5f")
b = st.number_input('Intersep', step=0.00001, format="%.5f")
a = st.number_input('Slope', step=0.00001, format="%.5f")

def hitung():
    x = (y - b) / a
    st.write(f"Konsentrasi = {x} (mg/L)")

if st.button("Calculate Konsentrasi Terukur"):
    hitung()


st.header(':blue[_Kadar Terukur_]')

y = st.number_input('Konsentrasi Terukur', step=0.00001, format="%.5f")
b = st.number_input('Faktor Pengali (Masukkan 1 jika tidak terdapat Faktor Pengali)', step=0.00001, format="%.5f")
a = st.number_input('Volume Sampel', step=0.00001, format="%.5f")
l = st.number_input('Bobot Sampel', step=0.00001, format="%.5f")


def hitung_kadar_terukur():
    m = (y * b * a) / l
    st.write(f"Kadar Terukur = {m} (mg/Kg)")

if st.button("Calculate Kadar Terukur"):
    hitung_kadar_terukur()

    

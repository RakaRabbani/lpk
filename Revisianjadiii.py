import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar
selected = option_menu(
    menu_title=None,
    options=["Artikel", "Calculator", "Masukan Dan Saran"],
    icons=["book-half", "pencil-square", "send-plus"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white"},
        "icon": {"color": "black", "font-family": "Times New Roman", "font-size": "25px"},
        "nav-link": {
            "font-size": "15px",
            "text-align": "mid",
            "margin": "0px",
            "--hover-color": "#69F0AE"
        },
        "nav-link-selected": {"background-color": "#69F0AE"}
    }
)



#isian
if selected == "Artikel":
    st.title("TEKNIK PENGAMBILAN SAMPEL :blue[AIR PERMUKAAN]")
    
    st.subheader("Pengertian Air Permukaan - Perhitungan Debit Air - Fungsi Pengukuran Debit Air")
    st.write("Air permukaan merupakan air yang terkumpul di atas tanah atau di mata air, sungai danau, lahan basah atau laut. Air permukaan berhubungan dengan air bawah tanah atau air atmosfer. Air permukaan dapat dibedakan menjadi dua jenis yaitu: Perairan Darat dan Perairan Laut.")
    st.write("Perairan Darat adalah air permukaan yang berada di atas daratan, misalnya seperti rawa-rawa, danau, sungai, dan lain sebagainya.")
    st.write("Perairan Laut adalah air permukaan yang berada di lautan luas.")

    st.subheader("Menghitung Debit Air Permukaan")
    st.write("Debit adalah jumlah aliran air (volume) yang mengalir melalui suatu penampang dalam waktu tertentu, umumnya dinyatakan dalam satuan volume/waktu yaitu (m³/detik). Yaitu dengan rumus berikut.")
    st.write("Debit= Volume (m³)/detik")

    st.subheader("Fungsi Pengukuran Debit Air")
    st.write("Pengukuran debit air penting dalam penelitian atau monitoring kualitas air permukaan karena dapat memberikan informasi tentang jumlah air yang sedang mengalir pada titik sampling. Debit air yang tinggi dapat menunjukkan aliran air yang kuat, yang dapat mempengaruhi penyebaran atau distribusi polutan. Di sisi lain, debit air yang rendah dapat mengindikasikan aliran yang lambat atau bahkan stagnan, yang mungkin menyebabkan penumpukan atau akumulasi polutan.")
    st.write("Selain itu, pengukuran debit air juga penting dalam menghitung beban polutan. Beban polutan adalah jumlah total polutan yang diangkut oleh aliran air dalam periode waktu tertentu. Dengan mengetahui debit air, kita dapat mengalikan konsentrasi polutan dalam air dengan debit tersebut untuk mengestimasi jumlah polutan yang masuk atau keluar dari suatu wilayah.")
    st.write("Dalam praktiknya, debit air dapat diukur menggunakan berbagai metode, seperti pengukuran langsung menggunakan perangkat pengukur debit, pengukuran dengan menggunakan perangkat pengukur kecepatan aliran air, atau dengan menggunakan model matematika yang memperhitungkan berbagai parameter hidrologi yang relevan.")


elif selected == "Masukan Dan Saran":
    st.header(":envelope: Hubungi kami")
    st.write("Punya saran atau permasalahan dalam mengakses web kami? Kami akan senang mendengar dari Anda. Kirimi kami pesan dan kami akan merespons sebaik mungkin.")

    contact_form = """
    <form action="https://formsubmit.co/fadlytai@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nama kamu (optional)" required>
        <input type="email" name="email" placeholder="email kamu" required>
        <textarea name="message" placeholder="Ketikkan kritik atau saranmu" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

elif selected == "Calculator":
        st.write("# Perhitungan Debit Air Sungai")
        st.write("Masukkan volume sungai yang sudah dikonversi ke meter dan masukkan waktu dalam satuan detik.")

        panjang = st.number_input("Masukkan panjang sungai (m): ", min_value=0.0, step=0.1)
        lebar = st.number_input("Masukkan lebar sungai (m): ", min_value=0.0, step=0.1)
        kedalaman = st.number_input("Masukkan kedalaman sungai (m): ", min_value=0.0, step=0.1)
        volume = panjang * lebar * kedalaman
        waktu = st.number_input("Masukkan waktu (detik): ", min_value=0.0, step=0.1)

        if st.button("Hitung"):
            debit = volume / waktu
            st.success(f"Hasil perhitungan Volume adalah {volume:.2f} m³")
            st.success(f"Hasil perhitungan Debit adalah {debit:.2f} m³/detik")
            

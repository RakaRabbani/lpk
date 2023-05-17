import streamlit as st

st.title(":green[Consa Meter]")
st.write(" ")
st.write("Selamat Datang!")
st.write(" ")
st.write("Rona Akan Membantu Kamu")
st.write(" ")
st.write(" ")
    
tab1, tab2, tab3 , tab4= st.tabs(["Rumus", "Konsentrasi Larutan Induk","Konsentrasi Deret Standar","Perhitungan Konsentrasi Terukur"])

with tab1:
    st.header("_:blue[Rumus]_")
    st.write(" ")
    st.write(" ")
    st.header("Rumus C Standar Induk")
    st.latex(r'''
                    C Standar Induk\left(\frac{mg}{L}\right)=
                    \left(\frac{Ar Fe * Bobot Garam Besi (mg)}{Mr Garam Besi * Volume Std (L)}\right)
                    ''')
    st.write(" ")
    st.header("Rumus C Deret Standar")
    st.latex(r'''
                    C Deret Standar\left(\frac{mg}{L}\right)=
                    \left(\frac{C Standar Induk\left(\frac{mg}{L}\right)}{Volume Labu Takar Deret Standar (L)}\right) * Volume Standar Induk (L)
                    ''')

with tab2:
        # Input perhitungan 1 - Konsentrasi Lar Induk
            st.header(":blue[Perhitungan C Standar Induk]")
            Ar = st.number_input('Ar sampel', step=0.0001, format="%.2f")
            Bg = st.number_input('Bobot sampel(mg)', step=0.0001, format="%.4f")
            Mr = st.number_input('Mr sampel', step=0.0001, format="%.2f")
            Vs = st.number_input('Volume Standar(L)', step=0.0001, format="%.2f")

            hitung_c_standar_induk = st.button('Hitung C Standar Induk')
            hasil_konsentrasi = None

            if hitung_c_standar_induk:
                def hitung_C_Standar_Induk(Ar, Bg, Mr, Vs):
                    konsentrasi = (Ar * Bg) / (Mr * Vs)
                    return konsentrasi

                if Ar == 0 or Bg == 0 or Mr == 0 or Vs == 0:
                    st.warning("Mohon masukkan nilai yang lebih dari 0 untuk melakukan perhitungan.")
                else:
                    hasil_konsentrasi = hitung_C_Standar_Induk(Ar, Bg, Mr, Vs)
                    st.write(f"C Standar Induk = {hasil_konsentrasi:.4f} (mg/L)")

with tab3:
        # Input perhitungan 2 - Konsentrasi Deret Std
            st.header(":blue[Perhitungan C Deret Standar]")
            Vtd = st.number_input('Volume Labu Takar Deret Standar(L)', step=0.0001, format="%.2f")
            Vlt = st.number_input('Volume Labu Takar Standar Induk(L)', step=0.0001, format="%.2f")
            Kons = st.number_input('C Standar Induk(mg/L)', step=0.0001, format="%.2f")

            hitung_c_Deret_Std = st.button('Hitung C Deret Standar')
            hasil_kadar = None

            if hitung_c_Deret_Std:
                def hitung_C_Deret_Std(Kons, Vtd, Vlt):
                    deret = (Kons / Vtd) * Vlt
                    return deret

                if Vtd == 0 or Vlt == 0:
                    st.warning("Mohon masukkan nilai yang lebih dari 0 untuk melakukan perhitungan.")
                else:
                    hasil_kadar = hitung_C_Deret_Std(Kons, Vtd, Vlt)
                    st.write(f"C Deret Standar = {hasil_kadar:.4f} (mg/L)")

with tab4:
        
        def hitung_konsentrasi(absorbansi, intersep, slope):
                konsentrasi = (absorbansi - intersep) / slope
                return konsentrasi

        def hitung_kadar_terukur(konsentrasi, faktor_pengali, volume_sampel, bobot_sampel):
                kadar_terukur = (konsentrasi * faktor_pengali * volume_sampel) / bobot_sampel
                return kadar_terukur
        
        def hitung_kadar_sampel(kadar_terukur, bobot_tablet):
                kadar_sampel = (kadar_terukur * bobot_tablet)
                return kadar_sampel

        def main():
                st.header(' ')
                st.header(' ')
                st.header(' ')

        # Input perhitungan 1 - Konsentrasi
        st.header(':blue[Perhitungan Konsentrasi]')
        absorbansi = st.number_input('Respon Alat', step=0.00001, format="%.5f")
        intersep = st.number_input('Intersep', step=0.00001, format="%.5f")
        slope = st.number_input('Slope', step=0.00001, format="%.5f")

        # Input perhitungan 2 - Kadar Terukur
        st.header(':blue[Perhitungan Kadar Terukur]')
        faktor_pengali = st.number_input('Faktor Pengali (Masukkan 1 jika tidak terdapat Faktor Pengali)', step=0.00001, format="%.5f")
        volume_sampel = st.number_input('Volume Sampel (L)', step=0.00001, format="%.5f")
        bobot_sampel = st.number_input('Bobot Sampel (Kg)', step=0.00001, format="%.5f")

        # Input perhitungan 3 - Kadar Sampel 
        st.header(':blue[Perhitungan Kadar Terukur]')
        bobot_tablet = st.number_input('Bobot Tablet (Kg)', step=0.00001, format="%.7f")

        # Tombol untuk menghitung
        if st.button("Calculate"):
            if absorbansi and intersep and slope and faktor_pengali and volume_sampel and bobot_sampel:
                    konsentrasi = hitung_konsentrasi(absorbansi, intersep, slope)
                    st.write(f"Konsentrasi = {konsentrasi:,.2f} (mg/L)", step=0.01, format="%.3f")

                    kadar_terukur = hitung_kadar_terukur(konsentrasi, faktor_pengali, volume_sampel, bobot_sampel)
                    st.write(f"Kadar Terukur = {kadar_terukur:,.2f} (mg/Kg)", step=0.01, format="%.3f")

                    kadar_sampel = hitung_kadar_sampel(kadar_terukur, bobot_tablet)
                    st.write(f"Kadar Sampel = {kadar_sampel:,.2f} (mg/tablet)", step=0.01, format="%.3f")
            else:
                    st.warning("Harap isi semua kolom input sebelum melakukan perhitungan.")

        if __name__ == '__main__':
                    main()
 






















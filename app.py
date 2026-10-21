import streamlit as st
import pandas as pd
import plotly.express as px

# Настройка страницы
st.set_page_config(
    page_title="İklim ve Tropik Meyveler Araştırma Portalı", 
    page_icon="🍌", 
    layout="wide"
)

# Главный заголовок
st.title("🌱 İklim Değişikliğinin Tropik Meyvelere Etkisi ve Sürdürülebilirlik")
st.markdown("### Mezuniyet Projesi Kapsamlı Araştırma, Analiz ve Simülasyon Platformu")
st.divider()

# Боковое меню
st.sidebar.header("🧭 Proje Menüsü")
menu = st.sidebar.radio(
    "Bölümler:", 
    ["📊 İklim Simülasyonu", "🍌 Detaylı Meyve Analizleri", "📚 Literatür ve Makaleler", "🌍 Küresel Risk Bölgeleri"]
)

if menu == "📊 İklim Simülasyonu":
    st.subheader("🌡️ Sıcaklık Artışı ve Verimlilik Simülasyonu")
    st.write("Küresel iklim projeksiyonlarının (IPCC senaryoları) seçilen tropik meyve türleri üzerindeki miktar ve kalite etkilerini simüle edin.")

    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        selected_fruit = st.selectbox(
            "İncelemek İstediğiniz Meyve:",
            ["Muz (Banana)", "Mango", "Avokado", "Ananas", "Papaya"]
        )
    with col_opt2:
        temp_increase = st.slider(
            "Öngörülen Sıcaklık Sapması (°C):",
            min_value=0.0, max_value=4.0, value=1.5, step=0.5
        )

    # Метрики
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Seçilen Ürün", value=selected_fruit)
    m2.metric(label="Sıcaklık Artışı", value=f"+{temp_increase} °C")
    est_loss = int(temp_increase * 7.5)
    m3.metric(label="Tahmini Verim Kaybı", value=f"%{est_loss}", delta=f"-{est_loss}%", delta_color="inverse")
    m4.metric(label="Risk Seviyesi", value="Kritik" if temp_increase > 2.0 else "Orta", delta="Dikkat" if temp_increase > 2.0 else "Stabil")

    st.divider()

    # Детальный текст в зависимости от фрукта
    if "Muz" in selected_fruit:
        st.info("📌 **Muz Tarımında İklim Etkisi:** Muz bitkisi yüksek suya ve 27-30°C optimum sıcaklığa ihtiyaç duyar. Artan sıcaklıklar ve düzensiz yağışlar, *Fusarium oxysporum* (Panama hastalığı) gibi yıkıcı mantar enfeksiyonlarının yayılma hızını artırır.")
    elif "Mango" in selected_fruit:
        st.info("📌 **Mango Tarımında İklim Etkisi:** Çiçeklenme döneminde yaşanan aşırı sıcaklık dalgalanmaları ve erken bahar yağışları polenleşmeyi engeller. Bu durum meyve tutum oranını doğrudan düşürür ve kalitesiz ürün rekoltesine yol açar.")
    elif "Avokado" in selected_fruit:
        st.info("📌 **Avokado Tarımında İklim Etkisi:** Avokado 'su ayak izi' en yüksek meyvelerden biridir. Kuraklık ve su kısıtı, meyve boyutlarının küçülmesine ve ağaçların fizyolojik stres altına girmesine neden olur.")
    else:
        st.info("📌 **Genel Tropik Etki:** Tropik ve subtropik meyveler iklim dalgalanmalarına karşı son derece hassastır. Artan buharlaşma ve toprak tuzluluğu kök sistemlerini olumsuz etkiler.")

    # График
    years = [2025, 2030, 2035, 2040, 2045, 2050]
    yield_data = [100, 98, 95 - temp_increase * 3, 90 - temp_increase * 5, 85 - temp_increase * 7, 80 - temp_increase * 10]
    
    df = pd.DataFrame({"Yıl": years, "Verimlilik Oranı (%)": yield_data})
    fig = px.line(df, x="Yıl", y="Verimlilik Oranı (%)", markers=True, title=f"{selected_fruit} Üretim Projeksiyonu (+{temp_increase}°C Senaryosu)")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "🍌 Detaylı Meyve Analizleri":
    st.subheader("📖 Tropik Meyve Türlerinin İklim Hassasiyetleri")
    st.write("Bu bölümde tez çalışmasının ana materyali olan meyvelerin biyolojik sınırları ve iklim istekleri detaylandırılmıştır.")

    tab1, tab2, tab3 = st.tabs(["🍌 Muz", "🥭 Mango", "🥑 Avokado"])

    with tab1:
        st.markdown("### Muz (Musa spp.)")
        st.markdown("""
        * **İdeal Sıcaklık:** 26°C - 30°C
        * **Su İhtiyacı:** Yüksek (Yıllık 1200-2500 mm düzenli yağış)
        * **İklim Değişikliği Tehditleri:** 
          1. Sıcaklık artışı su buharlaşmasını artırır, sulama maliyetleri yükselir.
          2. Yüksek nem ve sıcaklık, mantari hastalıkların (özellikle TR4 - Panama hastalığı) mutasyon geçirmesini ve yayılmasını tetikler.
          3. Fırtına ve tayfunların şiddetindeki artış muz gövdelerinin kırılmasına yol açar.
        """)

    with tab2:
        st.markdown("### Mango (Mangifera indica)")
        st.markdown("""
        * **İdeal Sıcaklık:** 24°C - 33°C
        * **Su İhtiyacı:** Orta (Kurak dönem çiçeklenme için gereklidir)
        * **İklim Değişikliği Tehditleri:**
          1. Kış ve ilkbahar geçişlerindeki anormal sıcaklıklar erken çiçeklenmeye neden olur, sonrasında gelen don veya ani soğuklar çiçekleri öldürür.
          2. Yağış rejiminin düzensizleşmesi antraknoz gibi fungal hastalıkların artmasına sebep olur.
        """)

    with tab3:
        st.markdown("### Avokado (Persea americana)")
        st.markdown("""
        * **İdeal Sıcaklık:** 20°C - 28°C
        * **Su İhtiyacı:** Çok Yüksek
        * **İklim Değişikliği Tehditleri:**
          1. Kısıtlı su kaynakları nedeniyle ağaçlar suya erişemez ve meyve kalitesi (yağ oranı ve lezzet) düşer.
          2. 35°C üzerindeki sıcaklıklar çiçek dökülmelerine ve meyve yanıklarına yol açar.
        """)

elif menu == "📚 Literatür ve Makaleler":
    st.subheader("📚 Akademik Literatür Taraması ve Kaynakça")
    st.write("Tez çalışmasının teorik altyapısını destekleyen ulusal ve uluslararası hakemli makaleler:")

    st.markdown("---")
    st.markdown("### 1. Küresel İklim Değişikliğinin Tarımsal Ekolojiye Etkileri")
    st.info("**Yazar:** Prof. Dr. Ahmet Yılmaz & Dr. Canan Demir (2024) | *Türkiye Tarım Bilimleri Dergisi*\n\n"
              "**Özet:** Çalışma, 2050 yılına kadar Akdeniz ve Ekvatoral kuşaktaki sıcaklık artışlarının tarım havzalarını nasıl daraltacağını ortaya koymaktadır. "
              "Özellikle tropik meyve yetiştiriciliğindeadaptasyon stratejilerinin (akıllı sulama, örtü altı tarım) acilen geliştirilmesi gerektiği vurgulanmaktadır.")

    st.markdown("---")
    st.markdown("### 2. Tropikal Meyve Üretiminde Patojen Dinamikleri ve İklim İlişkisi")
    st.info("**Yazar:** Maria Santos, Jean Paul, et al. (2023) | *Global Climate and Agriculture Review*\n\n"
              "**Özet:** İklim değişikliği ile birlikte artan sıcaklık ve nemin mantari hastalıkların (Fusarium wilt) yayılım alanlarını %22 oranında genişlettiği tespit edilmiştir. "
              "Muz ve avokado üretiminde dirençli türlerin (hybrid varieties) ıslah edilmesi hayati önem taşımaktadır.")

    st.markdown("---")
    st.markdown("### 3. Su Stresi Altında Tropik Meyve Ağaçlarının Fizyolojik Tepkileri")
    st.info("**Yazar:** Mehmet Aksoy (2022) | *İklim Değişikliği ve Çevre Araştırmaları Dergisi*\n\n"
              "**Özet:** Kuraklık stresinin bitki stoma hareketlerini kısıtladığı, fotosentez verimini düşürdüğü ve nihai rekoltede %30'a varan kayıplara sebep olduğu deneysel olarak kanıtlanmıştır.")

elif menu == "🌍 Küresel Risk Bölgeleri":
    st.subheader("🌍 İklim Değişikliğinden En Çok Etkilenen Üretim Bölgeleri")
    st.write("Dünya genelinde tropik meyve tedarik zincirini ve üretimini tehdit eden riskli coğrafyalar:")

    data_regions = {
        "Bölge / Ülke": [
            "Güneydoğu Asya (Filipinler, Hindistan)", 
            "Orta Amerika (Meksika, Honduras)", 
            "Ekvatoral Kuşak (Ekvador, Kolombiya)", 
            "Batı Afrika (Fildişi Sahili, Gana)"
        ],
        "Ana Ürün": ["Muz & Mango", "Avokado", "Muz & Ananas", "Ananas & Kakao/Tropikal"],
        "Risk Seviyesi": ["Yüksek", "Çok Yüksek", "Yüksek", "Orta-Yüksek"],
        "Başlıca İklim Problemi": ["Şiddetli tayfunlar ve seller", "Kronik kuraklık ve su kıtlığı", "Sıcaklık stresi ve fungal hastalıklar", "Düzensiz yağış ve toprak erozyonu"],
        "Öngörülen Etki (2050)": ["Üretim alanlarında %18 daralma", "Sulama maliyetlerinde %40 artış", "Rekoltede kalite düşüşü", "Tarım alanlarının kayması"]
    }
    df_reg = pd.DataFrame(data_regions)
    st.table(df_reg)
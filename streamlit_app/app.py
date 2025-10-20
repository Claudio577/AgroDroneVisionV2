import streamlit as st
import geemap.foliumap as geemap
from gee_utils import inicializar_gee, calcular_ndvi

# ========================================================
# Configuração inicial
# ========================================================
st.set_page_config(page_title="AgroDrone Vision", layout="wide", page_icon="🌾")
st.title("🌾 AgroDrone Vision — Análise NDVI com Sentinel-2")
st.markdown("Visualize a saúde da vegetação usando imagens de satélite Sentinel-2.")

# ========================================================
# Inicializa o Earth Engine
# ========================================================
inicializar_gee("edufin-ai-cloud")

# ========================================================
# Parâmetros de entrada
# ========================================================
col1, col2 = st.columns(2)
with col1:
    lat = st.number_input("Latitude", value=-23.55, format="%.6f")
with col2:
    lon = st.number_input("Longitude", value=-46.63, format="%.6f")

if st.button("🛰️ Gerar NDVI"):
    st.success("Processando imagem... aguarde alguns segundos.")

    ndvi, vis, point = calcular_ndvi(lat, lon)

    Map = geemap.Map(center=[lat, lon], zoom=10)
    Map.add_basemap("SATELLITE")
    Map.addLayer(ndvi, vis, "NDVI")
    Map.addLayer(point, {"color": "blue"}, "Localização")

    Map.to_streamlit(height=600)
else:
    st.info("Insira a latitude e longitude e clique em **Gerar NDVI**.")

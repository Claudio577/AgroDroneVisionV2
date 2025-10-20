import ee

def inicializar_gee(project_name="edufin-ai-cloud"):
    """Inicializa o Earth Engine"""
    try:
        ee.Initialize(project=project_name)
        print("✅ GEE conectado com sucesso!")
    except Exception:
        ee.Authenticate()
        ee.Initialize(project=project_name)
        print("🔐 Autenticação feita com sucesso!")

def calcular_ndvi(lat, lon, zoom=10):
    """Calcula o NDVI da área centralizada nas coordenadas fornecidas"""
    point = ee.Geometry.Point([lon, lat])
    img = ee.ImageCollection('COPERNICUS/S2_SR') \
        .filterBounds(point) \
        .filterDate('2024-01-01', '2024-12-31') \
        .sort('CLOUDY_PIXEL_PERCENTAGE') \
        .first()

    ndvi = img.normalizedDifference(['B8', 'B4']).rename('NDVI')
    vis = {'min': 0, 'max': 1, 'palette': ['red', 'yellow', 'green']}
    return ndvi, vis, point

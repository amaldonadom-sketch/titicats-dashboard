import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------------------------------------------
# Configuración de la página
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Titicats - Dashboard de Mercado",
    page_icon="🐱",
    layout="wide"
)

# Paleta de colores basada en los tokens originales
C_RUST = "#9A3E26"
C_COFFEE = "#6F4426"
C_COFFEE_LIGHT = "#C9A876"
C_ECO = "#57713F"
C_AMBER = "#A8752B"

# -------------------------------------------------------------------
# Base de Datos
# -------------------------------------------------------------------
data = [
    {"id": 1, "marca": "Bento Pet", "formato": "4 kg", "peso": 4, "precio": 37, "precioKg": 9.25,
     "tipo": "Bentonita económica", "biodeg": False, "origen": "Bolivia", "eco": 15},
    {"id": 2, "marca": "Bento Pet", "formato": "20 kg", "peso": 20, "precio": 157, "precioKg": 7.85,
     "tipo": "Bentonita económica", "biodeg": False, "origen": "Bolivia", "eco": 15},
    {"id": 3, "marca": "Karen", "formato": "4 kg", "peso": 4, "precio": 43, "precioKg": 10.75,
     "tipo": "Bentonita económica", "biodeg": False, "origen": "Bolivia", "eco": 16},
    {"id": 4, "marca": "PawerKatz", "formato": "4 kg", "peso": 4, "precio": 34.5, "precioKg": 8.58,
     "tipo": "Bentonita económica", "biodeg": False, "origen": "Bolivia", "eco": 15},
    {"id": 5, "marca": "Super Cat", "formato": "4 kg", "peso": 4, "precio": 34, "precioKg": 8.50,
     "tipo": "Bentonita económica", "biodeg": False, "origen": "No especificado", "eco": 14},
    {"id": 6, "marca": "Tom Cat", "formato": "4 kg", "peso": 4, "precio": 35, "precioKg": 8.75,
     "tipo": "Bentonita económica", "biodeg": False, "origen": "No especificado", "eco": 14},
    {"id": 7, "marca": "Alta Gama", "formato": "2 kg", "peso": 2, "precio": 56, "precioKg": 28.00,
     "tipo": "Bentonita premium", "biodeg": False, "origen": "Bolivia", "eco": 22},
    {"id": 8, "marca": "Cute Cat", "formato": "5 kg", "peso": 5, "precio": 112, "precioKg": 22.40,
     "tipo": "Bentonita premium", "biodeg": False, "origen": "Importado", "eco": 24},
    {"id": 9, "marca": "Tidy Cats", "formato": "3.6 kg", "peso": 3.6, "precio": 128, "precioKg": 35.56,
     "tipo": "Bentonita premium", "biodeg": False, "origen": "Importado", "eco": 26},
    {"id": 10, "marca": "Canada Litter", "formato": "12 kg", "peso": 12, "precio": 324, "precioKg": 27.00,
     "tipo": "Bentonita premium", "biodeg": False, "origen": "Importado", "eco": 25},
    {"id": 11, "marca": "Canada Litter", "formato": "18 kg Multicat", "peso": 18, "precio": 390, "precioKg": 21.67,
     "tipo": "Bentonita premium", "biodeg": False, "origen": "Importado", "eco": 25},
    {"id": 12, "marca": "Noba Science", "formato": "12 kg", "peso": 12, "precio": 362, "precioKg": 30.17,
     "tipo": "Bentonita premium", "biodeg": False, "origen": "Importado", "eco": 27},
    {"id": 13, "marca": "Noba Advanced", "formato": "15 kg", "peso": 15, "precio": 300, "precioKg": 20.00,
     "tipo": "Bentonita premium", "biodeg": False, "origen": "Importado", "eco": 27},
    {"id": 14, "marca": "Finotrato Bio-Litter", "formato": "2 kg", "peso": 2, "precio": 107, "precioKg": 53.50,
     "tipo": "Vegetal biodegradable", "biodeg": True, "origen": "Importado", "eco": 80},
    {"id": 15, "marca": "Viva Verde", "formato": "4 kg", "peso": 4, "precio": 130, "precioKg": 32.50,
     "tipo": "Vegetal biodegradable", "biodeg": True, "origen": "Importado", "eco": 78},
    {"id": 16, "marca": "Hello Kitty Rosa", "formato": "2 kg", "peso": 2, "precio": 67, "precioKg": 33.50,
     "tipo": "Vegetal biodegradable", "biodeg": True, "origen": "Importado", "eco": 72},
    {"id": 17, "marca": "Sanicat", "formato": "12 kg", "peso": 12, "precio": 132, "precioKg": 11.00,
     "tipo": "Vegetal biodegradable", "biodeg": True, "origen": "Importado", "eco": 75},
    {"id": 18, "marca": "Titicats", "formato": "2 kg", "peso": 2, "precio": 30, "precioKg": 15.00,
     "tipo": "Pellets de residuo de café", "biodeg": True, "origen": "Bolivia", "eco": 92},
    {"id": 19, "marca": "Titicats", "formato": "4 kg", "peso": 4, "precio": 50, "precioKg": 12.50,
     "tipo": "Pellets de residuo de café", "biodeg": True, "origen": "Bolivia", "eco": 92},
    {"id": 20, "marca": "Titicats", "formato": "10 kg", "peso": 10, "precio": 100, "precioKg": 10.00,
     "tipo": "Pellets de residuo de café", "biodeg": True, "origen": "Bolivia", "eco": 93},
]

df = pd.DataFrame(data)
df_comp = df[df["marca"] != "Titicats"]
df_titicats = df[df["marca"] == "Titicats"]

# -------------------------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------------------------
st.sidebar.title("☕ Titicats")
st.sidebar.caption("Estudio de mercado: arena sanitaria en pellets de residuo de café")

tab = st.sidebar.radio(
    "Navegación",
    [
        "Resumen ejecutivo",
        "Estructura del mercado",
        "Mapa competitivo",
        "Análisis de precios",
        "Arenas biodegradables",
        "Presentaciones Titicats"
    ]
)

# -------------------------------------------------------------------
# Pestañas del Dashboard
# -------------------------------------------------------------------

if tab == "Resumen ejecutivo":
    st.header("📊 Resumen ejecutivo")
    st.write("Panorama general del mercado de arena sanitaria en La Paz y posicionamiento de Titicats.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Marcas analizadas", df_comp["marca"].nunique())
    col2.metric("Precio mínimo", f"Bs {df_comp['precioKg'].min():.2f} /kg")
    col3.metric("Precio máximo", f"Bs {df_comp['precioKg'].max():.2f} /kg")
    col4.metric("Precio promedio", f"Bs {df_comp['precioKg'].mean():.2f} /kg")

    st.info(
        "**Posición de Titicats:** Rango de Bs 10 a 15 / kg. Se ubica en el segmento medio/económico compitiendo en costo contra las bentonitas tradicionales, pero ofreciendo una alternativa 100% biodegradable.")

elif tab == "Estructura del mercado":
    st.header("🧱 Estructura del mercado")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Marcas por tipo de arena")
        tipo_counts = df_comp.groupby("tipo")["marca"].nunique().reset_index()
        fig_marcas = px.bar(tipo_counts, x="marca", y="tipo", orientation="h",
                            labels={"marca": "N° Marcas", "tipo": "Tipo"}, color_discrete_sequence=[C_COFFEE])
        st.plotly_chart(fig_marcas, use_container_width=True)

    with col2:
        st.subheader("Precio promedio por tipo (Bs/kg)")
        tipo_avg = df_comp.groupby("tipo")["precioKg"].mean().reset_index()
        fig_prom = px.bar(tipo_avg, x="precioKg", y="tipo", orientation="h",
                          labels={"precioKg": "Bs/kg", "tipo": "Tipo"}, color_discrete_sequence=[C_AMBER])
        st.plotly_chart(fig_prom, use_container_width=True)

elif tab == "Mapa competitivo":
    st.header("🎯 Mapa competitivo")
    st.write("Comparación de Precio por Kg frente a la Diferenciación Ecológica.")

    fig_scatter = px.scatter(
        df, x="precioKg", y="eco", color="tipo", symbol="marca",
        text="marca", size="peso", hover_data=["formato", "precio"],
        labels={"precioKg": "Precio (Bs / kg)", "eco": "Índice Ecológico (0-100)"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

elif tab == "Análisis de precios":
    st.header("📈 Análisis de precios (Todas las referencias)")

    df_sorted = df.sort_values(by="precioKg", ascending=True).copy()
    df_sorted["Color"] = df_sorted["marca"].apply(lambda x: C_RUST if x == "Titicats" else C_COFFEE_LIGHT)

    fig_precios = px.bar(
        df_sorted, x="precioKg", y="marca", orientation="h",
        color="Color", color_discrete_map="identity",
        hover_data=["formato", "precio"],
        labels={"precioKg": "Precio por kg (Bs)", "marca": "Producto"}
    )
    st.plotly_chart(fig_precios, use_container_width=True)

elif tab == "Arenas biodegradables":
    st.header("🌱 Arenas biodegradables")
    st.write("Comparativa exclusiva de la categoría ecológica.")

    df_bio = df[df["biodeg"] == True].sort_values(by="precioKg", ascending=True)
    fig_bio = px.bar(
        df_bio, x="marca", y="precioKg", color="marca",
        text="precioKg", labels={"precioKg": "Bs / kg", "marca": "Marca"}
    )
    st.plotly_chart(fig_bio, use_container_width=True)

elif tab == "Presentaciones Titicats":
    st.header("📦 Presentaciones comerciales de Titicats")

    col1, col2, col3 = st.columns(3)
    col1.metric("Format 2 kg", "Bs 30", "Bs 15.00 / kg (Prueba)")
    col2.metric("Formato 4 kg", "Bs 50", "Bs 12.50 / kg (Estándar)")
    col3.metric("Formato 10 kg", "Bs 100", "Bs 10.00 / kg (Ahorro)")

    st.subheader("Curva de descuento por volumen")
    fig_line = px.line(
        df_titicats, x="formato", y="precioKg", markers=True,
        labels={"formato": "Formato", "precioKg": "Precio por kg (Bs)"},
        color_discrete_sequence=[C_RUST]
    )
    st.plotly_chart(fig_line, use_container_width=True)

import streamlit as st
from pathlib import Path
from utils.carga_ejercicios import cargar_ejercicios

st.set_page_config(
    page_title="Aprende Funciones",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.main {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

.titulo {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 0.5rem;
}

.subtitulo {
    text-align: center;
    font-size: 1.05rem;
    color: #475569;
    margin-bottom: 2rem;
}

.tarjeta {
    background: white;
    padding: 1.5rem;
    border-radius: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    margin-bottom: 1rem;
}

.feedback-ok {
    background: #dcfce7;
    color: #166534;
    padding: 1rem;
    border-radius: 12px;
    margin-top: 1rem;
    font-weight: 600;
}

.feedback-error {
    background: #fee2e2;
    color: #991b1b;
    padding: 1rem;
    border-radius: 12px;
    margin-top: 1rem;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "indice_ejercicio" not in st.session_state:
    st.session_state.indice_ejercicio = 0

ejercicios = cargar_ejercicios()
ejercicio = ejercicios[st.session_state.indice_ejercicio]

if st.session_state.pantalla == "inicio":
    st.markdown('<div class="titulo">📘 Aprende Funciones</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitulo">Practica matemáticas paso a paso con ayuda inteligente.</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Empezar", use_container_width=True):
            st.session_state.pantalla = "ejercicio"
            st.rerun()

elif st.session_state.pantalla == "ejercicio":
    st.progress(0.2)
    st.caption(f"Sección: {ejercicio['Seccion']} · Nivel: {ejercicio['Nivel']}")

    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader(f"Ejercicio {ejercicio['id']}")
    st.write(ejercicio["Enunciado"])

    ruta_imagen = Path("imagenes") / ejercicio["Imagen"]
    if ruta_imagen.exists():
        st.image(str(ruta_imagen), use_container_width=True)

    respuesta = st.text_input("Escribe tu respuesta")
    comprobar = st.button("Comprobar respuesta", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if comprobar:
        solucion_texto = ", ".join(ejercicio["Solucion"]) if isinstance(ejercicio["Solucion"], list) else ejercicio["Solucion"]

        if respuesta.strip().lower() == solucion_texto.strip().lower():
            st.markdown('<div class="feedback-ok">✅ Correcto. Muy bien hecho.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="feedback-error">❌ No es correcto. Inténtalo de nuevo o revisa la idea de función.</div>', unsafe_allow_html=True)
            with st.expander("Posibles tipos de error"):
                for error in ejercicio["Error_tipo"]:
                    st.write(f"- {error}")
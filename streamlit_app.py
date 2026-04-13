import streamlit as st

st.set_page_config(
    page_title="Aprende Funciones",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #eef4ff 0%, #dbeafe 45%, #e0f2fe 100%);
}

.main {
    padding-top: 0rem;
}

.hero-card {
    width: 100%;
    max-width: 950px;
    margin: 2rem auto 1rem auto;
    background: rgba(255,255,255,0.82);
    backdrop-filter: blur(10px);
    border-radius: 28px;
    padding: 3rem 2rem 2.2rem 2rem;
    box-shadow: 0 18px 50px rgba(15, 23, 42, 0.12);
    text-align: center;
    border: 1px solid rgba(255,255,255,0.55);
}

.badge {
    display: inline-block;
    background: #1d4ed8;
    color: white;
    padding: 0.45rem 1rem;
    border-radius: 999px;
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 1.2rem;
    letter-spacing: 0.3px;
}

.hero-title {
    font-size: 3.2rem;
    font-weight: 800;
    line-height: 1.1;
    color: #0f172a;
    margin-bottom: 0.8rem;
}

.hero-title span {
    color: #2563eb;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #334155;
    max-width: 760px;
    margin: 0 auto 1.4rem auto;
    line-height: 1.7;
}

.hero-mini {
    font-size: 1rem;
    color: #475569;
    margin-bottom: 1.2rem;
}

.pill {
    text-align: center;
    background: #eff6ff;
    color: #1e3a8a;
    padding: 0.8rem 0.9rem;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.95rem;
    border: 1px solid #bfdbfe;
    margin: 0.3rem 0;
}

.bottom-note {
    margin-top: 1.2rem;
    color: #64748b;
    font-size: 0.95rem;
    text-align: center;
}

.stButton > button {
    background: linear-gradient(90deg, #2563eb 0%, #4f46e5 100%);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.95rem 1.2rem;
    font-size: 1.05rem;
    font-weight: 700;
    box-shadow: 0 8px 22px rgba(37, 99, 235, 0.25);
}

.stButton > button:hover {
    filter: brightness(1.05);
}

@media (max-width: 900px) {
    .hero-title {
        font-size: 2.3rem;
    }

    .hero-subtitle {
        font-size: 1.05rem;
    }

    .hero-card {
        padding: 2rem 1.2rem;
    }
}
</style>
""", unsafe_allow_html=True)

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if st.session_state.pantalla == "inicio":
    st.markdown("""
<div class="hero-card">
    <div class="badge">📚 Matemáticas · 2º de ESO</div>
    <div class="hero-title">
        Aprende <span>Funciones</span><br>
        de forma visual e inteligente
    </div>
    <div class="hero-subtitle">
        Practica el concepto de función, interpreta gráficas y resuelve ejercicios
        paso a paso con ayuda adaptada a tus respuestas.
    </div>
    <div class="hero-mini">
        Una aplicación pensada para aprender a tu ritmo, mejorar con cada intento
        y ganar seguridad en matemáticas.
    </div>
</div>
""", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="pill">📈 Gráficas</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="pill">🧠 Feedback inmediato</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="pill">🎯 Ejercicios adaptativos</div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="pill">🏆 Progreso por niveles</div>', unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns([1.2, 1, 1.2])
    with col2:
        if st.button("Comenzar", use_container_width=True):
            st.session_state.pantalla = "ejercicio"
            st.rerun()

    st.markdown(
        "<div class='bottom-note'>Preparado para alumnado de 2º de ESO</div>",
        unsafe_allow_html=True
    )

elif st.session_state.pantalla == "ejercicio":
    st.title("📘 Ejercicios")
    st.write("Aquí irá el contenido de tus ejercicios.")
    if st.button("Volver a la portada"):
        st.session_state.pantalla = "inicio"
        st.rerun()
import streamlit as st
from pathlib import Path
from utils.carga_ejercicios import cargar_ejercicios, filtrar_ejercicios
import pandas as pd
import matplotlib.pyplot as plt

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

.exercise-card {
    width: 100%;
    max-width: 1000px;
    margin: 1.5rem auto 1rem auto;
    background: rgba(255,255,255,0.9);
    border-radius: 24px;
    padding: 2rem;
    box-shadow: 0 18px 50px rgba(15, 23, 42, 0.10);
    border: 1px solid rgba(255,255,255,0.6);
}

.exercise-title {
    font-size: 2rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 0.4rem;
    text-align: center;
}

.exercise-meta {
    text-align: center;
    color: #475569;
    font-size: 1rem;
    margin-bottom: 1.5rem;
}

.exercise-box {
    background: #f8fafc;
    border: 1px solid #dbeafe;
    border-radius: 18px;
    padding: 1.4rem;
    margin-top: 1rem;
}

.exercise-label {
    color: #1e3a8a;
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.exercise-text {
    color: #0f172a;
    font-size: 1.1rem;
    line-height: 1.7;
    white-space: pre-line;
}

.info-chip {
    display: inline-block;
    background: #eff6ff;
    color: #1e3a8a;
    padding: 0.4rem 0.8rem;
    border-radius: 999px;
    font-size: 0.9rem;
    font-weight: 600;
    margin: 0.2rem;
    border: 1px solid #bfdbfe;
}

.top-actions {
    width: 100%;
    max-width: 1000px;
    margin: 0 auto;
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

    .exercise-title {
        font-size: 1.6rem;
    }

    .exercise-card {
        padding: 1.2rem;
    }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Estado inicial
# -----------------------------
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "nivel_actual" not in st.session_state:
    st.session_state.nivel_actual = "1"

if "dificultad_actual" not in st.session_state:
    st.session_state.dificultad_actual = "1"

if "indice_ejercicio" not in st.session_state:
    st.session_state.indice_ejercicio = 0

# -----------------------------
# Carga y filtrado de ejercicios
# -----------------------------
todos_los_ejercicios = cargar_ejercicios()

ejercicios_actuales = filtrar_ejercicios(
    todos_los_ejercicios,
    nivel=st.session_state.nivel_actual,
    dificultad=st.session_state.dificultad_actual
)

# Seguridad por si el índice se sale
if ejercicios_actuales and st.session_state.indice_ejercicio >= len(ejercicios_actuales):
    st.session_state.indice_ejercicio = 0

# -----------------------------
# Pantalla de inicio
# -----------------------------
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
            st.session_state.nivel_actual = "1"
            st.session_state.dificultad_actual = "1"
            st.session_state.indice_ejercicio = 0
            st.rerun()

    st.markdown(
        "<div class='bottom-note'>Preparado para alumnado de 2º de ESO</div>",
        unsafe_allow_html=True
    )

# -----------------------------
# Pantalla de ejercicios
# -----------------------------
elif st.session_state.pantalla == "ejercicio":
    st.markdown('<div class="top-actions">', unsafe_allow_html=True)

    col_top_1, col_top_2, col_top_3 = st.columns([1, 2, 1])
    with col_top_1:
        if st.button("⬅ Volver a la portada", use_container_width=True):
            st.session_state.pantalla = "inicio"
            st.rerun()

    with col_top_2:
        st.markdown(
            f"""
            <div style="text-align:center; margin-top:0.35rem;">
                <span class="info-chip">Nivel {st.session_state.nivel_actual}</span>
                <span class="info-chip">Dificultad {st.session_state.dificultad_actual}</span>
                <span class="info-chip">{len(ejercicios_actuales)} ejercicios disponibles</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_top_3:
        if ejercicios_actuales:
            progreso = (st.session_state.indice_ejercicio + 1) / len(ejercicios_actuales)
            st.progress(progreso)

    st.markdown('</div>', unsafe_allow_html=True)

    if ejercicios_actuales:
        ejercicio = ejercicios_actuales[st.session_state.indice_ejercicio]

        st.markdown(
            f"""
            <div class="exercise-card">
                <div class="exercise-title">Ejercicio {ejercicio['id']}</div>
                <div class="exercise-meta">
                    Sección: {ejercicio.get('Seccion', 'Sin sección')}
                </div>
                <div class="exercise-box">
                    <div class="exercise-label">Enunciado</div>
                    <div class="exercise-text">{ejercicio['Enunciado']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        nombre_imagen = ejercicio.get("Imagen", "").strip()
        if nombre_imagen:
            ruta_imagen = Path("Imagenes") / nombre_imagen
            if ruta_imagen.exists():
                col_img_1, col_img_2, col_img_3 = st.columns([1, 2.2, 1])
                with col_img_2:
                    st.image(str(ruta_imagen), use_container_width=True)

        tipo_respuesta = ejercicio.get("Tipo_respuesta", "texto")

        st.write("")
        st.subheader("✍️ Tu respuesta")

        if tipo_respuesta == "texto":
            respuesta_usuario = st.text_area(
                "Escribe aquí tu respuesta",
                key=f"respuesta_{ejercicio['id']}",
                height=120,
                placeholder="Escribe tu respuesta aquí..."
            )

            col_resp_1, col_resp_2 = st.columns(2)

            with col_resp_1:
                comprobar = st.button("Comprobar respuesta", use_container_width=True)

            with col_resp_2:
                siguiente = st.button("Siguiente ejercicio", use_container_width=True)

            if comprobar:
                solucion = ejercicio.get("Solucion", "")

                if isinstance(solucion, list):
                    solucion_texto = ", ".join([str(x).strip().lower() for x in solucion])
                else:
                    solucion_texto = str(solucion).strip().lower()

                respuesta_normalizada = respuesta_usuario.strip().lower()

                if respuesta_normalizada == solucion_texto:
                    st.success("✅ Correcto. Muy bien hecho.")
                else:
                    st.error("❌ No es correcto. Revisa tu respuesta e inténtalo de nuevo.")

            if siguiente:
                st.session_state.indice_ejercicio += 1
                if st.session_state.indice_ejercicio >= len(ejercicios_actuales):
                    st.session_state.indice_ejercicio = 0
                st.rerun()

        elif tipo_respuesta == "coordenadas":
            tabla = ejercicio.get("Tabla", {})
            saltos = tabla.get("SALTO", [])
            longitudes_vacias = [""] * len(saltos)

            df = pd.DataFrame({
                "SALTO": saltos,
                "LONGITUD": longitudes_vacias
            })

            tabla_editable = st.data_editor(
                df,
                num_rows="fixed",
                use_container_width=True,
                key=f"tabla_{ejercicio['id']}"
            )

            col_resp_1, col_resp_2, col_resp_3 = st.columns(3)

            with col_resp_1:
                dibujar = st.button("Dibujar puntos", use_container_width=True)

            with col_resp_2:
                comprobar = st.button("Comprobar respuesta", use_container_width=True)

            with col_resp_3:
                siguiente = st.button("Siguiente ejercicio", use_container_width=True)

            if dibujar or comprobar:
                try:
                    x = tabla_editable["SALTO"].tolist()
                    y = [float(str(v).replace(",", ".")) for v in tabla_editable["LONGITUD"].tolist()]

                    fig, ax = plt.subplots()
                    ax.scatter(x, y)
                    ax.plot(x, y)
                    ax.set_xlabel("Salto")
                    ax.set_ylabel("Longitud")
                    ax.set_title("Representación de los saltos")
                    ax.grid(True)
                    st.pyplot(fig)

                    if comprobar:
                        solucion = ejercicio.get("Solucion", [])

                        def respuestas_iguales(resp, sol, tol=1e-2):
                            if len(resp) != len(sol):
                                return False
                            return all(abs(r - s) <= tol for r, s in zip(resp, sol))

                        if respuestas_iguales(y, solucion):
                            st.success("✅ Correcto. Has representado bien los datos.")
                        else:
                            st.error("❌ Hay valores incorrectos en la representación.")

                except ValueError:
                    st.error("Revisa los valores introducidos. Todas las longitudes deben ser numéricas.")
    else:
        st.warning("No hay ejercicios para el nivel y la dificultad seleccionados.")

    if siguiente:
        st.session_state.indice_ejercicio += 1
        if st.session_state.indice_ejercicio >= len(ejercicios_actuales):
            st.session_state.indice_ejercicio = 0
        st.rerun()
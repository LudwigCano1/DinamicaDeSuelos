###############################################################
##
##  Desarrollado por: Cano Pacheco Ludwig Luiggi, 20184022G
##  Curso: Dinámica de Suelos
##  Ciclo: 2022-2
##  Practica Calificada 1: Pregunta 1
##
###############################################################


import numpy as np
import math as m
import streamlit as st
import plotly_express as px


st.set_page_config(page_title="S1GdL",page_icon=":cat:",layout="wide")

#------------------------------------------------------------
# Definición de funciones para calcular
# - El factor de amplificación dinámica
# - El ángulo de fase
def FAD(beta,xi):
    return 1/(m.sqrt((1-beta**2)**2+(2*xi*beta)**2))
def phi(beta,xi):
    if beta == 1:
        return m.pi/2
    else:
        vtemp = m.atan(-2*xi*beta/(1-beta**2))
        if beta < 1: vtemp += m.pi
        return vtemp
#------------------------------------------------------------


#------------------------------------------------------------
# Definición de rango de valores de Beta y Xi
beta_i = 0; beta_f = 2; delta_beta = 0.001
beta_set = np.arange(beta_i,beta_f,delta_beta,dtype=float)
xi_set = [0.01,0.05,0.1,0.2,0.3,0.4,0.5,0.707,1]
#-----------------------------------------------------------

def IntPlot_FAD(beta):
    c1,c2,c3,c4,c5,c6 = st.columns(6,gap="small")
    with c1:
        st.write("Seleccione el valor de ξ1:")
    with c2:
        x1= st.slider("FAD_x1",min_value=1,max_value=100,value=5,label_visibility="hidden")/100
    with c3:
        color1 = st.color_picker("C1_FAD","#FF0012",label_visibility="hidden")
    with c4:
        st.write("Seleccione el valor de ξ2:")
    with c5:
        x2= st.slider("FAD_x2",min_value=1,max_value=100,value=15,label_visibility="hidden")/100
    with c6:
        color2 = st.color_picker("C2_FAD","#0098FF",label_visibility="hidden")
    FAD_set_1 = []
    FAD_set_2 = []
    for B in beta:
        FAD_set_1.append(FAD(B,x1))
        FAD_set_2.append(FAD(B,x2))
    plot1 = px.line(x=[0],y=[0],labels={"x":"β=ω/ωo","y":"FAD"},range_x=[beta[0],beta[-1]],range_y=[0,5])
    #plot2 = px.line(x=beta,y=phi_set,labels={"x":"β=ω/ωo","y":"Ángulo de fase ϕ/π"},range_x=[beta[0],beta[-1]],range_y=[0,1])
    plot1.add_scatter(x=beta,y=FAD_set_1,mode="lines",name=f"ξ1 = {x1:.2f}",line={"color":color1})
    plot1.add_scatter(x=beta,y=FAD_set_2,mode="lines",name=f"ξ2 = {x2:.2f}",line={"color":color2})
    st.plotly_chart(plot1,use_container_width=True)

def IntPlot_phi(beta):
    c1,c2,c3,c4,c5,c6 = st.columns(6,gap="small")
    with c1:
        st.write("Seleccione el valor de ξ1 (%):")
    with c2:
        x1= st.number_input("phi_x1",min_value=0.00,max_value=1.00,value=0.05,step=0.01,label_visibility="hidden")
    with c3:
        color1 = st.color_picker("C1_phi","#FF0012",label_visibility="hidden")
    with c4:
        st.write("Seleccione el valor de ξ2 (%):")
    with c5:
        x2= st.number_input("phi_x2",min_value=0.00,max_value=1.00,value=0.20,step=0.01,label_visibility="hidden")
    with c6:
        color2 = st.color_picker("C2_phi","#0098FF",label_visibility="hidden")
    phi_set_1 = []
    phi_set_2 = []
    for B in beta:
        phi_set_1.append(phi(B,x1)/m.pi)
        phi_set_2.append(phi(B,x2)/m.pi)
    plot2 = px.line(x=[0],y=[0],labels={"x":"β=ω/ωo","y":"Ángulo de fase ϕ/π"},range_x=[beta[0],beta[-1]],range_y=[0,1])
    plot2.add_scatter(x=beta,y=phi_set_1,mode="lines",name=f"ξ1 = {x1:.2f}",line={"color":color1})
    plot2.add_scatter(x=beta,y=phi_set_2,mode="lines",name=f"ξ2 = {x2:.2f}",line={"color":color2})
    st.plotly_chart(plot2,use_container_width=True)



def Preg_1():
    st.header("1. Vibración Forzada Amortiguada")
    st.subheader("1.1. Descripción del movimiento")
    st.write("La ecuación de movimiento de un sistema amortiguado de un grado de libertad sujeto a una carga armónica es:")
    st.latex(r"""\begin{equation}
    m\ddot{u}+c\dot{u}+ku=Q_0 \sin{\Omega t}
    \end{equation}""")
    st.write("Luego de dividir esta ecuación entre m, se puede escribir como:")
    st.latex(r"""\begin{equation}
    \ddot u +2\xi\omega_0 \dot{u}+\omega_0^2 u=\frac{Q_0}{m}\sin{\Omega t}
    \end{equation}""")
    st.write("donde:")
    st.latex(r"""\xi=\frac{c}{2m\omega_0} \text{\ \ \ \ \ y\ \ \ \ \ } \omega_0^2=\frac{k}{m}""")
    st.write("De la ecuación (2) se obtienen las soluciones general y particular:")
    st.latex(r"""\begin{align}
    u_c(t)=&e^{-\xi \omega_0 t}(C_1\sin{\omega_d t}+C_2\cos{\omega_d t})\\
    u_p(t)=&C_3\sin{\Omega t}+C_4\cos{\Omega t}
    \end{align}""")
    st.write("Siendo la frencuencia circular de la vibración amortiguada:")
    st.latex(r"""\omega_d=\omega_0\sqrt{1-\xi^2}""")
    st.write("Debido a la disminución de la amplitud de la solucion general, lo que predominará será la solución particular, es decir, la respuesta a la fuerza armónica externa.")
    st.write("La velocidad y la aceleración correspondientes son:")
    st.latex(r"""\begin{align}
    \dot u_p(t)=&C_3\Omega \cos{\Omega t}-C_4\Omega \sin{\Omega t}\\
    \ddot u_p(t)=&-\Omega^2 C_3 \sin{\Omega t}-\Omega^2 C_4 \cos{\Omega t}
    \end{align}""")
    st.write("Reemplazando estas ecuaciones en la ecuación de movimiento, y por igualdad de coeficientes, se tiene:")
    st.latex(r"""\begin{align}
    C_3=&\frac{Q_0}{k} \frac{1-\beta^2}{(1-\beta^2)^2+(2\xi\beta)^2}\\
    C_4=&\frac{Q_0}{k} \frac{-2\xi\beta}{(1-\beta^2)^2+(2\xi\beta)^2}
    \end{align}""")
    st.write("donde:")
    st.latex(r"""\beta={\Omega}/{\omega_0}""")
    st.write("La respuesta estacionaria también se puede escribir como:")
    st.latex(r"""\begin{split}
    u=&A\sin(\Omega t + \phi)\\
    u=&A\sin(\Omega t)\cos(\phi)+A\cos(\Omega t)\sin(\phi)\\
    \text{de donde:}\\
    C_3\sin{\Omega t}+C_4\cos{\Omega t}=&[A\cos(\phi)]\sin(\Omega t)+[A\sin(\phi)]\cos(\Omega t)\\
    C_3=&A\cos(\phi)\\
    C_4=&A\sin(\phi)\\
    A=&\sqrt{C_3^2+C_4^2}=\frac{Q_0}{k}\\
    \phi=&\tan^{-1}\left(\frac{C_4}{C_3}\right)=\tan^{-1}\left(\frac{-2\xi\beta}{1-\beta^2}\right)
    \end{split}""")




    st.latex(r"""\begin{equation}
    FAD=\frac{1}{\sqrt{(1-\beta ^2)^2+(2\xi \beta)^2}}
    \end{equation}""")
    st.subheader("Comparación de FAD variando el valor de ξ")
    IntPlot_FAD(beta_set)
    st.subheader("Comparación de ϕ/π variando el valor de ξ")
    IntPlot_phi(beta_set)

def Preg_2():
    st.header("Vibración Amortiguada con Movimiento en la Base")

st.sidebar.title("Sistemas de 1 Grado de Libertad")
st.sidebar.write("**Curso:** Dinámica de Suelos")
st.sidebar.write("**Ciclo:** 2022-2")
st.sidebar.write("**Desarrollado por:** Cano Pacheco Ludwig Luiggi")
st.sidebar.write("")
preguntas = st.sidebar.radio("Preguntas",options=["P1: Vibración Forzada Amortiguada","P2: Vibración Amortiguada con Movimiento en la Base"])

if preguntas == "P1: Vibración Forzada Amortiguada":
    Preg_1()
else:
    Preg_2()

#-----------------------------------------------------------

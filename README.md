# 🖥️ Calculadora GUI Estética: Distribuciones, Autómatas y Simulación COVID

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&style=for-the-badge)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Numerics-brightgreen?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-red?style=for-the-badge)

---

Una **aplicación de escritorio en Python** con interfaz gráfica **minimalista y clara**, que combina herramientas de:

- 📊 Estadística (generador de distribuciones aleatorias)  
- 🧩 Autómatas celulares 1D y 2D  
- 🦠 Simulación de propagación de COVID-19  

Ideal para fines educativos, experimentos interactivos y visualización de fenómenos complejos.

---

## ✨ Funcionalidades Principales

| Módulo | Descripción | Características | Exportación |
|--------|------------|----------------|------------|
| **Distribuciones Aleatorias** | Genera variables aleatorias | Continuas: `normal`, `uniform_cont`, `exponential`, `weibull`, `gamma`, `erlang`<br>Discretas: `uniform_disc`, `bernoulli`, `binomial`, `poisson`<br>Generador: `NumPy` o `LCG` | CSV / Excel |
| **Autómata 1D** | Evolución de celdas según reglas de Wolfram | Inicialización aleatoria, visualización histórica de hasta 300 pasos, reglas 0-255 | CSV |
| **Juego de la Vida 2D** | Simulación Life-like (B/S) | Configuración de reglas estilo `B3/S23`, inicialización aleatoria ~35% celdas vivas | PNG / CSV |
| **Simulación COVID-19 2D** | Autómata 2D con estados de infección | Estados: Vacío, Susceptible, Infectado, Recuperado, Fallecido<br>Parámetros: tamaño, densidad, probabilidad contagio, probabilidad muerte diaria, días recuperación, pasos | CSV / Excel |

---

## 🎨 Estética y Diseño

- Tema **claro y minimalista**  
  - Fondo: `#f5f7fb`  
  - Paneles: `#ffffff`  
  - Color de acento: `#2b7cff`  
  - Texto: `#0f1724`  
- Interfaz organizada en **pestañas (notebook)**:
  - Panel izquierdo: controles y explicación de cada módulo  
  - Panel derecho: visualización de gráficos interactivos  
- Uso de **Tkinter + Matplotlib** para gráficos y animaciones  

---

## 🛠️ Instalación

1. Clona o descarga este repositorio:  

```bash
git clone https://github.com/usuario/calculadora-gui-estetica.git
cd calculadora-gui-estetica
Instala las dependencias:

bash
Copiar código
pip install numpy pandas matplotlib pillow openpyxl
Ejecuta la aplicación:

bash
Copiar código
python calculadora_gui_estetica.py
📚 Uso Detallado
1️⃣ Generador de Distribuciones
Selecciona el tipo de distribución

Ingresa los parámetros según corresponda:

Distribución	Parámetros
Normal	mu (media), sigma (desviación estándar)
Exponencial	scale (media)
Uniforme continua	a (min), b (max)
Weibull	k (shape), lambda (scale)
Gamma / Erlang	k (shape), theta (scale)
Bernoulli	p (probabilidad de éxito)
Binomial	n (ensayos), p (probabilidad)
Poisson	lam (λ)

Selecciona generador (numpy o lcg) y seed opcional

Haz clic en "Generar y graficar"

Exporta los datos a CSV o Excel

2️⃣ Autómata 1D
Ingresa la regla de Wolfram (0-255)

Ingresa el tamaño del autómata (N celdas)

Botones disponibles:

Iniciar 1D aleatorio → genera estado inicial aleatorio

Paso 1D → avanza un paso según la regla

Exportar 1D CSV → guarda la historia completa

3️⃣ Juego de la Vida 2D
Ingresa regla estilo B3/S23 (Birth/Survive)

Ingresa tamaño del tablero N×N

Botones disponibles:

Iniciar 2D aleatorio → inicializa tablero con 35% celdas vivas

Paso 2D → aplica reglas Life-like

Exportar 2D → PNG o CSV del tablero actual

4️⃣ Simulación COVID-19
Configura parámetros:

Tamaño del grid N×N

Densidad población (0-1)

Probabilidad de contagio por vecino

Probabilidad de muerte diaria

Días para recuperación

Pasos de simulación

Botones disponibles:

Ejecutar simulación → muestra grid final y gráficos temporales

Exportar historial → CSV o Excel de infectados, recuperados, muertos y susceptibles

Colores del grid final:

🟦 Blanco: vacío

🟩 Verde: susceptible

🟥 Rojo: infectado

🟦 Azul: recuperado

⬛ Gris: fallecido

🔧 Notas Técnicas
La simulación COVID aplica reglas probabilísticas de contagio, recuperación y muerte.

Los autómatas celulares 1D y 2D permiten observar la evolución de sistemas dinámicos discretos.

El LCG incluido sirve para comparar resultados frente al generador de NumPy.

Exportaciones permiten análisis posterior en Excel o procesamiento estadístico adicional.

👨‍💻 Autor
Jefferson Justo
Proyecto educativo y experimental en Python, con enfoque en simulaciones estadísticas y celulares.

📄 Licencia
Este proyecto está disponible bajo la licencia MIT.

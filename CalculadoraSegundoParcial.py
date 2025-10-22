import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Colores y estética
BG = "#f0f0f0"
PANEL = "#e0e0e0"
ACCENT = "#4f46e5"
TEXT = "#000000"
PAD = 8

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Estadística y Autómatas")
        self.root.geometry("1100x700")
        self.root.configure(bg=BG)

        # Crear pestañas
        self.tab_control = ttk.Notebook(root)
        self.tab_dist = tk.Frame(self.tab_control, bg=BG)
        self.tab_ca = tk.Frame(self.tab_control, bg=BG)
        self.tab_control.add(self.tab_dist, text="Distribuciones")
        self.tab_control.add(self.tab_ca, text="Autómatas y COVID")
        self.tab_control.pack(expand=1, fill="both")

        # Construir cada pestaña
        self._build_tab_distribuciones(self.tab_dist)
        self._build_tab_automas(self.tab_ca)

    # -------------------- PESTAÑA DISTRIBUCIONES --------------------
    def _build_tab_distribuciones(self, parent):
        left = tk.Frame(parent, bg=PANEL, padx=PAD, pady=PAD)
        left.pack(side='left', fill='y', padx=PAD, pady=PAD)
        right = tk.Frame(parent, bg=BG, padx=PAD, pady=PAD)
        right.pack(side='right', fill='both', expand=True, padx=PAD, pady=PAD)

        tk.Label(left, text="Generador de Variables Aleatorias", bg=PANEL, fg=TEXT, font=('Segoe UI',12,'bold')).pack(anchor='w')

        # Cuadro explicativo
        expl = (
            "Ingrese parámetros según la distribución elegida:\n"
            "- Normal: mu (media), sigma (desviación)\n"
            "- Exponencial: scale (media)\n"
            "- Uniforme cont.: a (mínimo), b (máximo)\n"
            "- Weibull: k (shape), lambda (scale)\n"
            "- Gamma/Erlang: k (shape entero para Erlang), theta (scale)\n"
            "- Bernoulli: p (probabilidad éxito)\n"
            "- Binomial: n (ensayos), p (probabilidad)\n"
            "- Poisson: lam (lambda)\n"
        )
        tk.Label(left, text=expl, bg=PANEL, fg=TEXT, justify='left', wraplength=300).pack(anchor='w', pady=(6,12))

        # Selección de distribución
        tk.Label(left, text="Distribución:", bg=PANEL).pack(anchor='w')
        self.dist_kind = tk.StringVar(value='normal')
        kinds = ['uniform_cont','exponential','normal','weibull','gamma','erlang','uniform_disc','bernoulli','binomial','poisson']
        ttk.Combobox(left, values=kinds, textvariable=self.dist_kind, state='readonly').pack(fill='x', pady=(4,8))

        # -------------------- CAJAS DE TEXTO POR PARÁMETRO --------------------
        tk.Label(left, text="Normal: mu", bg=PANEL).pack(anchor='w')
        self.param_mu = tk.Entry(left); self.param_mu.insert(0,"0"); self.param_mu.pack(fill='x', pady=2)
        tk.Label(left, text="Normal: sigma", bg=PANEL).pack(anchor='w')
        self.param_sigma = tk.Entry(left); self.param_sigma.insert(0,"1"); self.param_sigma.pack(fill='x', pady=2)

        tk.Label(left, text="Uniforme cont.: a", bg=PANEL).pack(anchor='w')
        self.param_a = tk.Entry(left); self.param_a.insert(0,"0"); self.param_a.pack(fill='x', pady=2)
        tk.Label(left, text="Uniforme cont.: b", bg=PANEL).pack(anchor='w')
        self.param_b = tk.Entry(left); self.param_b.insert(0,"1"); self.param_b.pack(fill='x', pady=2)

        tk.Label(left, text="Exponencial: scale", bg=PANEL).pack(anchor='w')
        self.param_scale = tk.Entry(left); self.param_scale.insert(0,"1"); self.param_scale.pack(fill='x', pady=2)

        tk.Label(left, text="Weibull: k (shape)", bg=PANEL).pack(anchor='w')
        self.param_k = tk.Entry(left); self.param_k.insert(0,"1.5"); self.param_k.pack(fill='x', pady=2)
        tk.Label(left, text="Weibull: lambda (scale)", bg=PANEL).pack(anchor='w')
        self.param_lambda = tk.Entry(left); self.param_lambda.insert(0,"1"); self.param_lambda.pack(fill='x', pady=2)

        tk.Label(left, text="Gamma/Erlang: k", bg=PANEL).pack(anchor='w')
        self.param_kg = tk.Entry(left); self.param_kg.insert(0,"2"); self.param_kg.pack(fill='x', pady=2)
        tk.Label(left, text="Gamma/Erlang: theta", bg=PANEL).pack(anchor='w')
        self.param_theta = tk.Entry(left); self.param_theta.insert(0,"1"); self.param_theta.pack(fill='x', pady=2)

        tk.Label(left, text="Bernoulli: p", bg=PANEL).pack(anchor='w')
        self.param_p = tk.Entry(left); self.param_p.insert(0,"0.5"); self.param_p.pack(fill='x', pady=2)

        tk.Label(left, text="Binomial: n", bg=PANEL).pack(anchor='w')
        self.param_n = tk.Entry(left); self.param_n.insert(0,"10"); self.param_n.pack(fill='x', pady=2)
        tk.Label(left, text="Binomial: p", bg=PANEL).pack(anchor='w')
        self.param_np = tk.Entry(left); self.param_np.insert(0,"0.5"); self.param_np.pack(fill='x', pady=2)

        tk.Label(left, text="Poisson: lam", bg=PANEL).pack(anchor='w')
        self.param_lam = tk.Entry(left); self.param_lam.insert(0,"3"); self.param_lam.pack(fill='x', pady=2)

        # Entradas comunes
        tk.Label(left, text="Tamaño muestra (n):", bg=PANEL).pack(anchor='w')
        self.dist_n_entry = tk.Entry(left); self.dist_n_entry.insert(0,"2000"); self.dist_n_entry.pack(fill='x', pady=(4,8))

        tk.Label(left, text="Generador (numpy ó lcg):", bg=PANEL).pack(anchor='w')
        self.dist_gen = tk.StringVar(value='numpy')
        ttk.Combobox(left, values=['numpy','lcg'], textvariable=self.dist_gen, state='readonly').pack(fill='x', pady=(4,8))

        tk.Label(left, text="Seed (opcional, int):", bg=PANEL).pack(anchor='w')
        self.dist_seed = tk.Entry(left); self.dist_seed.pack(fill='x', pady=(4,8))

        # Botones generar y exportar
        btn_frame = tk.Frame(left, bg=PANEL)
        btn_frame.pack(fill='x', pady=(8,0))
        tk.Button(btn_frame, text="Generar y graficar", bg=ACCENT, fg='white', command=self._dist_generate).pack(side='left', expand=True, fill='x', padx=(0,6))
        tk.Button(btn_frame, text="Exportar muestras", bg='#6b7280', fg='white', command=self._dist_export).pack(side='left', expand=True, fill='x')

        # Área de gráfico
        fig = Figure(figsize=(8,6), dpi=100)
        self.ax_hist = fig.add_subplot(111)
        self.ax_hist.set_title("Histograma")
        self.canvas_hist = FigureCanvasTkAgg(fig, master=right)
        self.canvas_hist.get_tk_widget().pack(fill='both', expand=True)
        self.current_samples = None

    # -------------------- FUNCIONES DISTRIBUCIONES --------------------
    def _dist_generate(self):
        kind = self.dist_kind.get()
        n = int(self.dist_n_entry.get())
        seed_val = self.dist_seed.get()
        seed = int(seed_val) if seed_val else None
        if seed is not None:
            np.random.seed(seed)

        # Generar según distribución
        try:
            if kind == 'normal':
                mu = float(self.param_mu.get())
                sigma = float(self.param_sigma.get())
                samples = np.random.normal(mu, sigma, n)
            elif kind == 'uniform_cont':
                a = float(self.param_a.get())
                b = float(self.param_b.get())
                samples = np.random.uniform(a, b, n)
            elif kind == 'exponential':
                scale = float(self.param_scale.get())
                samples = np.random.exponential(scale, n)
            elif kind == 'weibull':
                k = float(self.param_k.get())
                lam = float(self.param_lambda.get())
                samples = lam * np.random.weibull(k, n)
            elif kind == 'gamma':
                k = float(self.param_kg.get())
                theta = float(self.param_theta.get())
                samples = np.random.gamma(k, theta, n)
            elif kind == 'erlang':
                k = int(self.param_kg.get())
                theta = float(self.param_theta.get())
                samples = np.random.gamma(k, theta, n)
            elif kind == 'bernoulli':
                p = float(self.param_p.get())
                samples = np.random.binomial(1, p, n)
            elif kind == 'binomial':
                n_trial = int(self.param_n.get())
                p = float(self.param_np.get())
                samples = np.random.binomial(n_trial, p, n)
            elif kind == 'poisson':
                lam = float(self.param_lam.get())
                samples = np.random.poisson(lam, n)
            else:
                messagebox.showerror("Error","Distribución no implementada")
                return
        except Exception as e:
            messagebox.showerror("Error en parámetros", str(e))
            return

        self.current_samples = samples
        self.ax_hist.clear()
        self.ax_hist.hist(samples, bins=50, color=ACCENT, alpha=0.7)
        self.ax_hist.set_title(f"Histograma: {kind}")
        self.canvas_hist.draw()

    def _dist_export(self):
        if self.current_samples is None:
            messagebox.showwarning("Aviso","Primero genere muestras")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV","*.csv"),("Excel","*.xlsx")])
        if file_path:
            if file_path.endswith(".csv"):
                pd.DataFrame(self.current_samples, columns=["Muestras"]).to_csv(file_path, index=False)
            else:
                pd.DataFrame(self.current_samples, columns=["Muestras"]).to_excel(file_path, index=False)
            messagebox.showinfo("Éxito","Archivo guardado correctamente")

    # -------------------- PESTAÑA AUTÓMATAS --------------------
    def _build_tab_automas(self, parent):
        left = tk.Frame(parent, bg=PANEL, padx=PAD, pady=PAD)
        left.pack(side='left', fill='y', padx=PAD, pady=PAD)
        right = tk.Frame(parent, bg=BG, padx=PAD, pady=PAD)
        right.pack(side='right', fill='both', expand=True, padx=PAD, pady=PAD)

        tk.Label(left, text="Simulación Autómatas Celulares", bg=PANEL, fg=TEXT, font=('Segoe UI',12,'bold')).pack(anchor='w')

        # Selección de tipo
        tk.Label(left, text="Tipo de autómata:", bg=PANEL).pack(anchor='w')
        self.auto_kind = tk.StringVar(value='1D')
        ttk.Combobox(left, values=['1D','2D','COVID'], textvariable=self.auto_kind, state='readonly').pack(fill='x', pady=(4,8))

        # Tamaño de tablero
        tk.Label(left, text="Filas:", bg=PANEL).pack(anchor='w')
        self.rows_entry = tk.Entry(left); self.rows_entry.insert(0,"20"); self.rows_entry.pack(fill='x', pady=2)
        tk.Label(left, text="Columnas:", bg=PANEL).pack(anchor='w')
        self.cols_entry = tk.Entry(left); self.cols_entry.insert(0,"20"); self.cols_entry.pack(fill='x', pady=2)

        # Evoluciones
        tk.Label(left, text="Pasos:", bg=PANEL).pack(anchor='w')
        self.steps_entry = tk.Entry(left); self.steps_entry.insert(0,"50"); self.steps_entry.pack(fill='x', pady=2)

        # Botón para ejecutar simulación
        tk.Button(left, text="Simular", bg=ACCENT, fg='white', command=self._simulate_automata).pack(fill='x', pady=(8,0))

        # Área de gráfico
        fig2 = Figure(figsize=(8,6), dpi=100)
        self.ax_auto = fig2.add_subplot(111)
        self.ax_auto.set_title("Autómata Celular")
        self.canvas_auto = FigureCanvasTkAgg(fig2, master=right)
        self.canvas_auto.get_tk_widget().pack(fill='both', expand=True)
        self.current_grid = None

    # -------------------- FUNCIONES AUTÓMATAS --------------------
    def _simulate_automata(self):
        kind = self.auto_kind.get()
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
            steps = int(self.steps_entry.get())
        except ValueError:
            messagebox.showerror("Error","Filas, columnas y pasos deben ser enteros")
            return

        # Generar tablero inicial aleatorio
        grid = np.random.choice([0,1], size=(rows, cols))
        self.current_grid = grid.copy()

        # Simulación
        self.ax_auto.clear()
        self.ax_auto.set_title(f"Autómata: {kind}")
        if kind == '1D':
            for t in range(steps):
                self.ax_auto.imshow(grid, cmap='binary')
                self.canvas_auto.draw()
                grid = self._next_step_1D(grid)
        elif kind == '2D':
            for t in range(steps):
                self.ax_auto.imshow(grid, cmap='binary')
                self.canvas_auto.draw()
                grid = self._next_step_2D(grid)
        elif kind == 'COVID':
            for t in range(steps):
                self.ax_auto.imshow(grid, cmap='coolwarm')
                self.canvas_auto.draw()
                grid = self._simulate_covid(grid)
        else:
            messagebox.showerror("Error","Tipo no implementado")
            return

    # -------------------- FUNCIONES INTERNAS AUTÓMATAS --------------------
    def _next_step_1D(self, grid):
        new_grid = np.zeros_like(grid)
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                total = np.sum(grid[i, max(0,j-1):min(grid.shape[1],j+2)])
                new_grid[i,j] = 1 if total==1 else 0
        return new_grid

    def _next_step_2D(self, grid):
        new_grid = grid.copy()
        rows, cols = grid.shape
        for i in range(rows):
            for j in range(cols):
                total = np.sum(grid[max(0,i-1):min(rows,i+2), max(0,j-1):min(cols,j+2)]) - grid[i,j]
                if grid[i,j]==1 and (total<2 or total>3):
                    new_grid[i,j]=0
                elif grid[i,j]==0 and total==3:
                    new_grid[i,j]=1
        return new_grid

    def _simulate_covid(self, grid):
        new_grid = grid.copy()
        rows, cols = grid.shape
        for i in range(rows):
            for j in range(cols):
                if grid[i,j]==1:
                    for ni in range(max(0,i-1), min(rows,i+2)):
                        for nj in range(max(0,j-1), min(cols,j+2)):
                            if grid[ni,nj]==0 and np.random.rand()<0.3:
                                new_grid[ni,nj]=1
        return new_grid

# -------------------- EJECUCIÓN --------------------
if __name__=="__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()

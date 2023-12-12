import tkinter as tk
from experta import *

class PlantDiseaseDiagnosis(KnowledgeEngine):
    def __init__(self, result_label):
        super().__init__()
        self.result_label = result_label

    @Rule(Fact(leaf_type="ancha"), Fact(symptoms="manchas"), Fact(extreme_conditions="sí"))
    def disease_1(self):
        self.result_label.config(text="Diagnóstico:\nPosible enfermedad fúngica por humedad.\nConsejo:\nMejorar la ventilación y considerar un fungicida.")

    @Rule(Fact(leaf_type="ancha"), Fact(symptoms="manchas"), Fact(extreme_conditions="no"))
    def disease_2(self):
        self.result_label.config(text="Diagnóstico:\nDeficiencia nutricional o ataque de plagas.\nConsejo:\nVerificar la nutrición y examinar presencia de plagas.")

    @Rule(Fact(leaf_type="ancha"), Fact(symptoms="marchitamiento"), Fact(extreme_conditions="sí"))
    def disease_3(self):
        self.result_label.config(text="Diagnóstico:\nSobre riego o raíces pobres.\nConsejo:\nRevisar el sistema de riego y la salud de las raíces.")

    @Rule(Fact(leaf_type="ancha"), Fact(symptoms="marchitamiento"), Fact(extreme_conditions="no"))
    def disease_4(self):
        self.result_label.config(text="Diagnóstico:\nFalta de agua o estrés por calor.\nConsejo:\nAumentar el riego y proporcionar sombra.")

    @Rule(Fact(leaf_type="ancha"), Fact(symptoms="decoloración"), Fact(extreme_conditions="sí"))
    def disease_5(self):
        self.result_label.config(text="Diagnóstico:\nQuemaduras por químicos o estrés por frío.\nConsejo:\nEvitar químicos agresivos y proteger de temperaturas extremas.")

    @Rule(Fact(leaf_type="ancha"), Fact(symptoms="decoloración"), Fact(extreme_conditions="no"))
    def disease_6(self):
        self.result_label.config(text="Diagnóstico:\nFalta de nutrientes o luz insuficiente.\nConsejo:\nRevisar la fertilización y las condiciones de luz.")

    @Rule(Fact(leaf_type="ancha"), Fact(symptoms="pérdida de hojas"), Fact(extreme_conditions="sí"))
    def disease_7(self):
        self.result_label.config(text="Diagnóstico:\nShock por trasplante o condiciones extremas.\nConsejo:\nAsegurar cuidados post-trasplante y protección contra extremos.")

    @Rule(Fact(leaf_type="ancha"), Fact(symptoms="pérdida de hojas"), Fact(extreme_conditions="no"))
    def disease_8(self):
        self.result_label.config(text="Diagnóstico:\nEnfermedad natural de la planta o estrés por envejecimiento.\nConsejo:\nMantenimiento normal y revisión general.")

    @Rule(Fact(leaf_type="estrecha"), Fact(symptoms="manchas"), Fact(extreme_conditions="sí"))
    def disease_9(self):
        self.result_label.config(text="Diagnóstico:\nPosible infección fúngica o daño por heladas.\nConsejo:\nTratar con fungicida y proteger de bajas temperaturas.")

    @Rule(Fact(leaf_type="estrecha"), Fact(symptoms="manchas"), Fact(extreme_conditions="no"))
    def disease_10(self):
        self.result_label.config(text="Diagnóstico:\nDeficiencia de nutrientes o enfermedades bacterianas.\nConsejo:\nRevisar la nutrición y considerar tratamiento bacteriano.")
    @Rule(Fact(leaf_type="estrecha"), Fact(symptoms="marchitamiento"), Fact(extreme_conditions="sí"))
    def disease_11(self):
        self.result_label.config(text="Diagnóstico:\nEstrés por trasplante o enfermedades radiculares.\nConsejo:\nVerificar las raíces y mejorar las condiciones de trasplante.")

    @Rule(Fact(leaf_type="estrecha"), Fact(symptoms="marchitamiento"), Fact(extreme_conditions="no"))
    def disease_12(self):
        self.result_label.config(text="Diagnóstico:\nDeshidratación o calor excesivo.\nConsejo:\nAumentar el riego y proporcionar sombra.")

    @Rule(Fact(leaf_type="estrecha"), Fact(symptoms="decoloración"), Fact(extreme_conditions="sí"))
    def disease_13(self):
        self.result_label.config(text="Diagnóstico:\nQuemaduras por exposición a químicos o estrés por temperaturas extremas.\nConsejo:\nEvitar productos químicos dañinos y proteger de temperaturas extremas.")

    @Rule(Fact(leaf_type="estrecha"), Fact(symptoms="decoloración"), Fact(extreme_conditions="no"))
    def disease_14(self):
        self.result_label.config(text="Diagnóstico:\nDeficiencia de nutrientes o exposición insuficiente a la luz.\nConsejo:\nAjustar la fertilización y mejorar la exposición a la luz.")

    @Rule(Fact(leaf_type="estrecha"), Fact(symptoms="pérdida de hojas"), Fact(extreme_conditions="sí"))
    def disease_15(self):
        self.result_label.config(text="Diagnóstico:\nEstrés por cambios bruscos de ambiente o enfermedades.\nConsejo:\nEstabilizar el entorno y revisar posibles enfermedades.")

    @Rule(Fact(leaf_type="estrecha"), Fact(symptoms="pérdida de hojas"), Fact(extreme_conditions="no"))
    def disease_16(self):
        self.result_label.config(text="Diagnóstico:\nCiclo natural de la planta o posible ataque de plagas.\nConsejo:\nObservar la planta para detectar plagas, mantener cuidados habituales.")

    @Rule(Fact(leaf_type="agujas"), Fact(symptoms="manchas"), Fact(extreme_conditions="sí"))
    def disease_17(self):
        self.result_label.config(text="Diagnóstico:\nPosible infección fúngica o daño por heladas.\nConsejo:\nAplicar fungicida y proteger de temperaturas extremas.")

    @Rule(Fact(leaf_type="agujas"), Fact(symptoms="manchas"), Fact(extreme_conditions="no"))
    def disease_18(self):
        self.result_label.config(text="Diagnóstico:\nProblemas nutricionales o enfermedades bacterianas.\nConsejo:\nRevisar la nutrición y considerar tratamientos específicos.")

    @Rule(Fact(leaf_type="agujas"), Fact(symptoms="marchitamiento"), Fact(extreme_conditions="sí"))
    def disease_19(self):
        self.result_label.config(text="Diagnóstico:\nExceso de riego o enfermedades radiculares.\nConsejo:\nControlar el riego y examinar la salud de las raíces.")

    @Rule(Fact(leaf_type="agujas"), Fact(symptoms="marchitamiento"), Fact(extreme_conditions="no"))
    def disease_20(self):
        self.result_label.config(text="Diagnóstico:\nNecesidad de riego o exposición insuficiente a luz.\nConsejo:\nAumentar el riego y asegurar suficiente luz solar.")
   
    @Rule(Fact(leaf_type="agujas"), Fact(symptoms="decoloración"), Fact(extreme_conditions="sí"))
    def disease_21(self):
        self.result_label.config(text="Diagnóstico:\nPosible daño por frío o exposición a químicos.\nConsejo:\nProteger de las heladas y evitar el uso de químicos dañinos.")

    @Rule(Fact(leaf_type="agujas"), Fact(symptoms="decoloración"), Fact(extreme_conditions="no"))
    def disease_22(self):
        self.result_label.config(text="Diagnóstico:\nDeficiencia de nutrientes o luz inadecuada.\nConsejo:\nRevisar y ajustar la fertilización, mejorar la exposición a la luz.")

    @Rule(Fact(leaf_type="agujas"), Fact(symptoms="pérdida de hojas"), Fact(extreme_conditions="sí"))
    def disease_23(self):
        self.result_label.config(text="Diagnóstico:\nEstrés por trasplante o condiciones ambientales adversas.\nConsejo:\nAsegurar un cuidado adecuado post-trasplante y proteger de extremos ambientales.")

    @Rule(Fact(leaf_type="agujas"), Fact(symptoms="pérdida de hojas"), Fact(extreme_conditions="no"))
    def disease_24(self):
        self.result_label.config(text="Diagnóstico:\nCaída natural de agujas o posible enfermedad.\nConsejo:\nMantenimiento normal, pero estar atento a otros síntomas de enfermedad.")

def start_diagnosis():
    if(leaf_type_var.get() == "" or symptoms_var.get() == "" or extreme_conditions_var.get() == ""):
        result_label.config(text="Por favor, seleccione una opción para cada campo.")
        return
    engine = PlantDiseaseDiagnosis(result_label)
    engine.reset()
    engine.declare(Fact(leaf_type=leaf_type_var.get()))
    engine.declare(Fact(symptoms=symptoms_var.get()))
    engine.declare(Fact(extreme_conditions=extreme_conditions_var.get()))
    engine.run()

window = tk.Tk()
window.title("Diagnóstico de Enfermedades en Plantas")

frame = tk.Frame(window, padx=20, pady=20)
frame.pack()

leaf_type_var = tk.StringVar()
symptoms_var = tk.StringVar()
extreme_conditions_var = tk.StringVar()

tk.Label(frame, text="Tipo de Hoja:",font=("Arial", 16,'bold')).grid(row=0, column=0, sticky='w')
tk.Radiobutton(frame, text="Ancha", variable=leaf_type_var, value="ancha",tristatevalue=0,font=("Arial", 14)).grid(row=1, column=0, sticky='w')
tk.Radiobutton(frame, text="Estrecha", variable=leaf_type_var, value="estrecha",tristatevalue=0,font=("Arial", 14)).grid(row=2, column=0, sticky='w')
tk.Radiobutton(frame, text="Agujas", variable=leaf_type_var, value="agujas",tristatevalue=0,font=("Arial", 14)).grid(row=3, column=0, sticky='w')

tk.Label(frame, text="Síntomas Visibles:",font=("Arial", 16,'bold')).grid(row=4, column=0, sticky='w')
tk.Radiobutton(frame, text="Manchas", variable=symptoms_var, value="manchas",tristatevalue=0,font=("Arial", 14)).grid(row=5, column=0, sticky='w')
tk.Radiobutton(frame, text="Marchitamiento", variable=symptoms_var, value="marchitamiento",tristatevalue=0,font=("Arial", 14)).grid(row=6, column=0, sticky='w')
tk.Radiobutton(frame, text="Decoloración", variable=symptoms_var, value="decoloración",tristatevalue=0,font=("Arial", 14)).grid(row=7, column=0, sticky='w')

tk.Label(frame, text="Exposición a Condiciones Extremas:",font=("Arial", 16,'bold')).grid(row=8, column=0, sticky='w')
tk.Radiobutton(frame, text="Sí", variable=extreme_conditions_var, value="sí",tristatevalue=0,font=("Arial", 14)).grid(row=9, column=0, sticky='w')
tk.Radiobutton(frame, text="No", variable=extreme_conditions_var, value="no",tristatevalue=0,font=("Arial", 14)).grid(row=10, column=0, sticky='w')

tk.Button(frame, text="Diagnóstico", command=start_diagnosis, bg="blue", fg="white", font=("Arial", 16)).grid(row=11, column=0)


result_label = tk.Label(frame, text="", font=("Arial", 16))
result_label.grid(row=0, column=1, rowspan=12, sticky='w')

window.mainloop()

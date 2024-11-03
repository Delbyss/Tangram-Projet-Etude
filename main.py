import tkinter as tk

# Initialiser la fenêtre principale
window = tk.Tk()
window.title("Relier deux points")
window.geometry("500x500")

# Créer un canevas pour dessiner les points et la ligne
canvas = tk.Canvas(window, width=500, height=500, bg="white")
canvas.pack()

# Positions initiales des points
point1_position = (100, 100)
point2_position = (300, 300)

# Dessiner les points et la ligne
point1 = canvas.create_oval(point1_position[0] - 5, point1_position[1] - 5, 
                            point1_position[0] + 5, point1_position[1] + 5, 
                            fill="red", tags="point1")

point2 = canvas.create_oval(point2_position[0] - 5, point2_position[1] - 5, 
                            point2_position[0] + 5, point2_position[1] + 5, 
                            fill="blue", tags="point2")

line = canvas.create_line(point1_position[0], point1_position[1], 
                          point2_position[0], point2_position[1], 
                          fill="black", width=2)

# Fonction pour mettre à jour la ligne entre les points
def update_line():
    x1, y1 = canvas.coords(point1)[0:2]
    x2, y2 = canvas.coords(point2)[0:2]
    canvas.coords(line, x1+5, y1+5, x2+5, y2+5)

# Fonction pour rendre les points déplaçables
def make_draggable(point):
    def on_drag(event):
        # Déplacer le point avec la souris
        x, y = event.x, event.y
        canvas.coords(point, x - 5, y - 5, x + 5, y + 5)
        update_line()  # Mettre à jour la ligne pour qu'elle reste connectée
    canvas.tag_bind(point, "<B1-Motion>", on_drag)

# Rendre les points déplaçables
make_draggable(point1)
make_draggable(point2)

# Lancer la boucle principale de Tkinter
window.mainloop()

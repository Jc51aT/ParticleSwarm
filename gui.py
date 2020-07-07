import tkinter as tk

root = tk.Tk()
root.title("Particle Swarm visulization")
root.maxsize(900,600)
root.config(bg='black')

UI_Frame = tk.Frame(root, width=600, height=200, bg='grey')
UI_Frame.grid(row=0, column=0, padx=10, pady=5)

canvas = tk.Canvas(root, width=600, height=380, bg='white') 
canvas.grid(row=1, column=0, padx=10, pady=5)




root.mainloop()

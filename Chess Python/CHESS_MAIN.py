#Python Ajedrez
from DESK import Tablero

game="START"
action=None
tabl=Tablero(8,8)
#tabl.Imprimir_Tablero_Piezas()
#tabl.Imprimir_Tablero_Base()
tabl.Imprimir_Tablero_Juego()
print("Type your next action.\nM to move\nS to select\nE to close:")
while(game!="END"):
	c1_1=-1;c1_2=-1;c2_1=-1;c2_2=-1
	action=input("Action: ")
	if action=="M":
		while(c1_1<0 or c1_1>tabl.Width-1):
			try:
				c1_1=int(input("X coord of the piece to move: "))
			except:
				c1_1=-1
		while(c1_2<0 or c1_2>tabl.Height-1):
			try:
				c1_2=int(input("Y coord of the piece to move: "))
			except:
				c1_2=-1
		
		while(c2_1<0 or c2_1>tabl.Width-1):
			try:
				c2_1=int(input("X coord of the piece to place: "))
			except:
				c2_1=-1
		while(c2_2<0 or c2_2>tabl.Height-1):
			try:
				c2_2=int(input("Y coord of the piece to place: "))
			except:
				c2_2=-1
		tabl.Move([c1_1,c1_2],[c2_1,c2_2])
	elif action=="S":
		while(c1_1<0 or c1_1>tabl.Width-1):
			try:
				c1_1=int(input("X coord of the piece to move: "))
			except:
				c1_1=-1
		while(c1_2<0 or c1_2>tabl.Height-1):
			try:
				c1_2=int(input("Y coord of the piece to move: "))
			except:
				c1_2=-1
		
		tabl.Select([c1_1,c1_2])
	elif action=="E":
		game="END"
	

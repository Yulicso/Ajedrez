#Python Ajedrez
	
class Pieza:
	def __init__(self,_idd="X",_slot=[0,0],_isFree=False):
		self.IsPosFree=_isFree
		self.PiezaID=_idd
		self.slot=[_slot[0],_slot[1]]
	
	def Shot_Piece(self):
		return(self.PiezaID)
	
	def Show_Slot(self):
		return(self.slot)
	
	def Show_Free(self):
		return(self.IsPosFree)
	
	def Show_Info(self):
		return(f"{self.Shot_Piece()} Slot: {self.Show_Slot()} Is free: {self.Show_Free()}")

	def Set_Slot(self,slot):
		self.slot=slot

	def Move_Slot(self,_Pieza):
		_PiezaSlot=_Pieza.Show_Slot()
		if _Pieza!=self:
			if self.slot!=_PiezaSlot:
				tex=f"Moved to slot {_PiezaSlot}"
				self.slot=_PiezaSlot
				return(tex)
			else:
				return("Cant Move")
		else:
			return("IT'S ME!!!!")

class Tablero:
	def __init__(self,_w,_h):
		self.Width=_w
		self.Height=_h
		self.Tablero=[]
		self.TableroP=[]
		self.Crear_Tablero_Base()
		self.Crear_Tablero_Piezas()
	
	def Crear_Tablero_Base(self):
		for i in range(self.Height):
			for j in range(self.Width):
				if i%2==0:
					if j%2!=0:
						_id="⬛"
					else:
						_id="⬜"
				else:
					if j%2==0:
						_id="⬛"
					else:
						_id="⬜"
				try:
					self.Tablero.append(Pieza(_id,[i,j]))
				except:
					print("error1")
	
	def Crear_Tablero_Piezas(self):
		for i in range(self.Height):
			for j in range(self.Width):
				free=False
				if i==1:
					_id="♙"
				elif i==6:
					_id="♟"
				elif (i==0 or i==7)and(j==0 or j==7):
					_id="♜"
				else:
					_id=". "
					free=True
				try:
					self.TableroP.append(Pieza(_id,[i,j],free))
				except:
					print("error2")
	
	def Imprimir_Tablero_Base(self,_resalt=None):
		brekMax=self.Width-1
		brek=0
		fil=0
		for i in range(len(self.Tablero)):
			print(self.Tablero[i].Shot_Piece(),end=" ")
			if brek==brekMax:
				fil+=1
				brek=0
				print()
			else:
				brek+=1
		print()
        
	def Imprimir_Tablero_Piezas(self,_resalt=None):
		brekMax=self.Width-1
		brek=0
		fil=0
		for i in range(len(self.TableroP)):
			print(self.TableroP[i].Shot_Piece(),end=" ")
			if brek==brekMax:
				fil+=1
				brek=0
				print()
			else:
				brek+=1
		print()
	
	def Imprimir_Tablero_Juego(self):
		brekMax=self.Width-1
		brek=0
		fil=0
		for i in range(len(self.TableroP)):
			if self.TableroP[i].Show_Free()==False:
				print(self.TableroP[i].Shot_Piece(),end=" ")
			else:
				print(self.Tablero[i].Shot_Piece(),end=" ")
			if brek==brekMax:
				fil+=1
				brek=0
				print()
			else:
				brek+=1
	
	def Tablero_Get_Slot(self,slot):
		for i in range(len(self.TableroP)):
			if self.TableroP[i].Show_Slot()==slot:
				return([self.TableroP[i],i])
	
	def Move(self,pos1,pos2):
		Pice_1=self.Tablero_Get_Slot(pos1)[0]
		id_1=self.Tablero_Get_Slot(pos1)[1]
		Pice_2=self.Tablero_Get_Slot(pos2)[0]
		id_2=self.Tablero_Get_Slot(pos2)[1]
		if Pice_1.Show_Free()==False and Pice_2.Show_Free()==True:
			print()
			print(f"moving {Pice_1.Shot_Piece()} from {Pice_1.Show_Slot()} to {Pice_2.Show_Slot()}")
			tempPice1=Pice_1
			tempSlot1=Pice_1.Show_Slot()
			tempPice2=Pice_2
			tempSlot2=Pice_2.Show_Slot()
			
			Pice_2=tempPice1
			Pice_1=tempPice2
			
			Pice_2.Set_Slot(tempSlot2)
			Pice_1.Set_Slot(tempSlot1)
			self.TableroP[id_1]=Pice_1
			self.TableroP[id_2]=Pice_2
			
			self.Imprimir_Tablero_Juego()
			print()

try:
	game="START"
	action=None
	tabl=Tablero(8,8)
	#tabl.Imprimir_Tablero_Piezas()
	#tabl.Imprimir_Tablero_Base()
	tabl.Imprimir_Tablero_Juego()
	while(game!="END"):
		c1_1=-1;c1_2=-1;c2_1=-1;c2_2=-1
		action=input("Type your next action, example(M to move , E to close):\nAction: ")
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
			tabl.Move([c1_2,c1_1],[c2_2,c2_1])
		elif action=="E":
			game="END"
		
except:
    print("error ext")


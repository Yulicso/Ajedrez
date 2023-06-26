#Python Ajedrez

class Icon:
	def __init__(self):
		self.Peon	=	["♙ ","♟ "]
		self.Tower	=	["♖ ","♜ "]
		self.Alfil	=	["♗ ","♝ "]
		self.Horse	=	["♘ ","♞ "]
		self.King	=	["♔ ","♚ "]
		self.Queen	=	["♕ ","♛ "]
		self.Empty	=	["⬛","⬜"]
	
	def Piece_Peon(self,color):
		if color=="Black":
			return(self.Peon[0])
		elif color=="White":
			return(self.Peon[1])
	
	def Piece_Tower(self,color):
		if color=="Black":
			return(self.Tower[0])
		elif color=="White":
			return(self.Tower[1])
	
	def Piece_Alfil(self,color):
		if color=="Black":
			return(self.Alfil[0])
		elif color=="White":
			return(self.Alfil[1])
	
	def Piece_Horse(self,color):
		if color=="Black":
			return(self.Horse[0])
		elif color=="White":
			return(self.Horse[1])
	
	def Piece_King(self,color):
		if color=="Black":
			return(self.King[0])
		elif color=="White":
			return(self.King[1])
	
	def Piece_Queen(self,color):
		if color=="Black":
			return(self.Queen[0])
		elif color=="White":
			return(self.Queen[1])
	
	def Piece_Empty(self,color):
		if color=="Black":
			return(self.Empty[0])
		elif color=="White":
			return(self.Empty[1])
	
	def Get_Piece_Icon(self,piece,color):
		if piece=="P":
			return(self.Piece_Peon(color))
		elif piece=="T":
			return(self.Piece_Tower(color))
		elif piece=="A":
			return(self.Piece_Alfil(color))
		elif piece=="H":
			return(self.Piece_Horse(color))
		elif piece=="K":
			return(self.Piece_King(color))
		elif piece=="Q":
			return(self.Piece_Queen(color))
		elif piece=="E":
			return(self.Piece_Empty(color))

class Piece:
	def __init__(self,_id="X",_slot=[0,0],_isFree=False,_team="test"):
		self.Team=_team
		self.IsPosFree=_isFree
		self.PiezaID=_id
		self.Slot=[_slot[0],_slot[1]]
		self.FirstMove=True
		self.PlaceSlots=[]
	
	def Update_Place_Slots(self,_tablero):
		if self.PiezaID in Icon().Peon:
			if self.Team=="Black":
				_dir=1
			elif self.Team=="White":
				_dir=-1
			
			if self.FirstMove==True:
				self.PlaceSlots=[ [ self.Slot[0],self.Slot[1]+(1*_dir) ] , [ self.Slot[0],self.Slot[1]+(2*_dir) ] ]
			else:
				if _tablero.Tablero_Get_Slot([self.Slot[0],self.Slot[1]+(1*_dir)])[0].Show_Free()==True:
					self.PlaceSlots=[ [self.Slot[0],self.Slot[1]+(1*_dir)] ]
				else:self.PlaceSlots=[]
					
	
	def Show_Piece(self):
		return(self.PiezaID)
	
	def Show_Slot(self):
		return(self.Slot)
	
	def Show_Place_Slots(self):
		print("Slots to move:")
		for i in range(len(self.PlaceSlots)):
			print(self.PlaceSlots[i])
	
	def Show_Free(self):
		return(self.IsPosFree)
	
	def Show_Team(self):
		return(self.Team)
	
	def Show_Info(self):
		return(f"{self.Show_Piece()}\nTeam: {self.Team}\nSlot: xy{self.Show_Slot()}")

	def Set_Slot(self,slot):
		if self.Show_Free()==False:
			self.FirstMove=False
		self.Slot=slot

class Tablero:
	def __init__(self,_w,_h):
		self.Width=_w
		self.Height=_h
		self.Turn="Black"
		self.Tablero=[]
		self.TableroP=[]
		self.Crear_Tablero_Base()
		self.Crear_Tablero_Piezas()
	
	def Crear_Tablero_Base(self):
		for i in range(self.Height):
			for j in range(self.Width):
				if i%2==0:
					if j%2!=0:
						_id=Icon().Get_Piece_Icon("E","Black")
					else:
						_id=Icon().Get_Piece_Icon("E","White")
				else:
					if j%2==0:
						_id=Icon().Get_Piece_Icon("E","Black")
					else:
						_id=Icon().Get_Piece_Icon("E","White")
				try:
					self.Tablero.append(Piece(_id,[j,i]))
				except:
					#The try and catch are used to catch
					# any error during the proces of adding more things
					print("error_create_base")
	
	def Crear_Tablero_Piezas(self):
		for i in range(self.Height):
			for j in range(self.Width):
				free=False
				tim=""
				if i==0 or i==1:
					tim="Black"
				elif i==6 or i==7:
					tim="White"
				else:
					tim="slot"
				if i==1:
					_id=Icon().Get_Piece_Icon("P","Black")
				elif i==6:
					_id=Icon().Get_Piece_Icon("P","White")
				elif i==0:
					if(j==0 or j==7):
						_id=Icon().Get_Piece_Icon("T","Black")
					elif(j==1 or j==6):
						_id=Icon().Get_Piece_Icon("H","Black")
					elif(j==2 or j==5):
						_id=Icon().Get_Piece_Icon("A","Black")
					elif(j==3):
						_id=Icon().Get_Piece_Icon("Q","Black")
					elif(j==4):
						_id=Icon().Get_Piece_Icon("K","Black")
				elif i==7:
					if(j==0 or j==7):
						_id=Icon().Get_Piece_Icon("T","White")
					elif(j==1 or j==6):
						_id=Icon().Get_Piece_Icon("H","White")
					elif(j==2 or j==5):
						_id=Icon().Get_Piece_Icon("A","White")
					elif(j==3):
						_id=Icon().Get_Piece_Icon("K","White")
					elif(j==4):
						_id=Icon().Get_Piece_Icon("Q","White")
				else:
					_id=". "
					free=True
				try:
					self.TableroP.append(Piece(_id,[j,i],free,tim))
				except:
					#The try and catch are used to catch
					# any error during the proces of adding more things
					print("error_create_pieces")
	
	def Imprimir_Tablero_Base(self,_resalt=None):
		brekMax=self.Width-1
		brek=0
		fil=0
		for i in range(len(self.Tablero)):
			print(self.Tablero[i].Show_Piece(),end=" ")
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
			print(self.TableroP[i].Show_Piece(),end=" ")
			if brek==brekMax:
				fil+=1
				brek=0
				print()
			else:
				brek+=1
		print()
	
	def Imprimir_Tablero_Juego(self):
		for i in range(len(self.TableroP)):
			self.TableroP[i].Update_Place_Slots(self)
		brekMax=self.Width-1
		brek=0
		fil=0
		for i in range(len(self.TableroP)):
			if self.TableroP[i].Show_Free()==False:
				print(self.TableroP[i].Show_Piece(),end="")
			else:
				print(self.Tablero[i].Show_Piece(),end="")
			if brek==brekMax:
				fil+=1
				brek=0
				print()
			else:
				brek+=1
		print("Turn of",self.Turn)
	
	def Tablero_Get_Slot(self,slot):
		for i in range(len(self.TableroP)):
			if self.TableroP[i].Show_Slot()==slot:
				return([self.TableroP[i],i])
	
	def Move(self,pos1,pos2):
		Pice_1=self.Tablero_Get_Slot(pos1)[0]
		id_1=self.Tablero_Get_Slot(pos1)[1]
		Pice_2=self.Tablero_Get_Slot(pos2)[0]
		id_2=self.Tablero_Get_Slot(pos2)[1]
		if Pice_1.Show_Free()==False and Pice_2.Show_Free()==True and Pice_1.Show_Team()==self.Turn:
			print()
			print(f"moving {Pice_1.Show_Piece()} from {Pice_1.Show_Slot()} to {Pice_2.Show_Slot()}")
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
			
			self.Turn="White" if self.Turn=="Black" else "Black"
			self.Imprimir_Tablero_Juego()
			print()
		else:
			error_msg=[
				"Invalid move. You can't move an empty slot",
				"Invalid move. You can't move a piece that's not your color",
				"Invalid move. Cant't move there, Team piece is in the slot",
				"Invalid move. Cant't move there, Enemy piece is in the slot"
			]
			if Pice_1.Show_Free()==False and Pice_1.Show_Team()!=self.Turn:
				print(error_msg[1])
			else:
				if Pice_1.Show_Free()==True:
					print(error_msg[0])
				else:
					if Pice_2.Show_Free()==False:
						if Pice_2.Show_Team()==self.Turn:
							print(error_msg[2])
						else:
							print(error_msg[3])
	def Select(self,pos):
		select_piece=self.Tablero_Get_Slot(pos)[0]
		if select_piece.Show_Free()==False and select_piece.Show_Team()==self.Turn:
			select_piece.Show_Place_Slots()
		else:
			error_msg=[
				"Invalid. You can't select an empty slot",
				"Invalid. You can't select a piece that's not your color"
			]
			if select_piece.Show_Free()==False and select_piece.Show_Team()!=self.Turn:
				print(error_msg[1])
			elif select_piece.Show_Free()==True:
				print(error_msg[0])

try:
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
		
except:
    print("error ext")


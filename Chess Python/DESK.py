from ICONS import Icon
from PIECES import Piece

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
	
	def Imprimir_Tablero_Base(self):
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
        
	def Imprimir_Tablero_Piezas(self):
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
	
	def Imprimir_Tablero_Juego(self,ArrSel=[]):
		for i in range(len(self.TableroP)):
			self.TableroP[i].Update_Place_Slots(self)
		brekMax=self.Width-1
		brek=0
		fil=0
		for i in range(len(self.TableroP)):
			
			if self.TableroP[i].Show_Free()==False:
				if len(ArrSel)>0:
					if self.TableroP[i].Show_Slot() in (ArrSel):
						print(Icon().Get_Piece_Icon("S",self.TableroP[i].Show_Free()),end="")
					else:
						print(self.TableroP[i].Show_Piece(),end="")
				else:
					print(self.TableroP[i].Show_Piece(),end="")
			else:
				if len(ArrSel)>0:
					if self.Tablero[i].Show_Slot() in (ArrSel):
						print(Icon().Get_Piece_Icon("S",self.TableroP[i].Show_Free()),end="")
					else:
						print(self.Tablero[i].Show_Piece(),end="")
				else:
					print(self.Tablero[i].Show_Piece(),end="")
			if brek==brekMax:
				fil+=1
				brek=0
				print()
			else:
				brek+=1
	
	def Coord_In_Tablero(self,_coord):
		if (_coord[0] in [i for i in range(self.Width)]) and (_coord[1] in [i for i in range(self.Height)]):
			return(True)
		else:
			return(False)
	
	def Tablero_Get_Slot(self,slot):
		for i in range(len(self.TableroP)):
			if self.TableroP[i].Show_Slot()==slot:
				return([self.TableroP[i],i])
	
	def Move(self,pos1,pos2):
		Pice_1=self.Tablero_Get_Slot(pos1)[0]
		id_1=self.Tablero_Get_Slot(pos1)[1]
		Pice_2=self.Tablero_Get_Slot(pos2)[0]
		id_2=self.Tablero_Get_Slot(pos2)[1]
		
		if (Pice_1.Show_Free()==False) and (Pice_2.Show_Free()==True) and (Pice_1.Show_Team()==self.Turn) and (pos2 in Pice_1.Show_Place_Slots()):
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
			print("Turn of",self.Turn)
			print()
		else:
			error_msg=[
				"Invalid move. You can't move an empty slot",
				"Invalid move. You can't move a piece that's not your color",
				"Invalid move. Cant't move there, Team piece is in the slot",
				"Invalid move. Cant't move there, Enemy piece is in the slot",
				"Invalid move. Destination Slot not in Patho Slolts"
			]
			if (pos2 in Pice_1.Show_Place_Slots()):
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
			else:
				print(error_msg[4])
	def Select(self,pos):
		select_piece=self.Tablero_Get_Slot(pos)[0]
		if select_piece.Show_Free()==False and select_piece.Show_Team()==self.Turn:
			select_piece.Show_Place_Slots(True)
			self.Imprimir_Tablero_Juego(select_piece.Show_Place_Slots())
		else:
			error_msg=[
				"Invalid. You can't select an empty slot",
				"Invalid. You can't select a piece that's not your color"
			]
			if select_piece.Show_Free()==False and select_piece.Show_Team()!=self.Turn:
				print(error_msg[1])
			elif select_piece.Show_Free()==True:
				print(error_msg[0])
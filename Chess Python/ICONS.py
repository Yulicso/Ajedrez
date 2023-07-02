class Icon:
	def __init__(self):
		self.Peon	=	["♙ ","♟ "]
		self.Tower	=	["♖ ","♜ "]
		self.Alfil	=	["♗ ","♝ "]
		self.Horse	=	["♘ ","♞ "]
		self.King	=	["♔ ","♚ "]
		self.Queen	=	["♕ ","♛ "]
		self.Empty	=	["⬛","⬜"]
		self.Select =   ["▒▒","▓▓"]
	
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
	
	def Piece_Select(self,color):
		if color==True:
			return(self.Select[0])
		elif color==False:
			return(self.Select[1])
	
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
		elif piece=="S":
			return(self.Piece_Select(color))

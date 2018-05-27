def Crossover(Pop, Pcros):
	Npop = len(Pop)
	Num_Op = Npop * Pcros
	Cross_Desc = []

	ii = 0

	while ii < Num_Op:
		Parent1 = Random(Pop)
		Parent2 = Random(Pop) #it must be different from Parent1
		
		Point_Cross_X = Random(1, min(Lenght_X(Parent1), Lenght_X(Parent2)))
		Point_Cross_Y = Random(1, min(Lenght_Y(Parent1), Lenght_Y(Parent2)))

		X11 = Left(X1, Point_Cross_X)
		X21 = Left(X2, Point_Cross_X)
		X12 = Right(X1, Point_Cross_X)
		X22 = Right(X2, Point_Cross_X)
		
		Y11 = Left(Y1, Point_Cross_Y)
		Y21 = Left(Y2, Point_Cross_Y)
		Y12 = Right(Y1, Point_Cross_Y)
		Y22 = Right(Y2, Point_Cross_Y)

		X[3] = X11 + X22
		X[4] = X12 + X21
		X[5] = X11 + X22
		X[6] = X12 + X21
		
		Y[3] = Y11 + Y22
		Y[4] = Y12 + Y21
		Y[5] = Y11 + Y22
		Y[6] = Y12 + Y21

		jj = 0

		while jj < 4:
			Descendant[jj] = Individual(X[2 + jj], Y[2 + jj])
			
			if Unical(Descendant[jj], Pop+Cross_Desc) == True:
				Cross_Desc += Descendant[jj]
			
			jj+=1

		i+=1
		



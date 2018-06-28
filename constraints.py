#maximum number of roles to which an user can belong(e.g. 30)
def cardinality_constraint_of_role(individual, max_n):
	summa = 0
	for gene in individual[0]:
		semi_summa = 0
		for allele in gene:
			if allele == '1':
				semi_summa += 1
		if semi_summa > max_n:
			return 1
		summa += semi_summa

	return summa
	"""

	if all(gene.count('1') < max_n for gene in individual[0]):
		a = sum(gene > 0 for gene in individual[0])
		print a
		return a
	else:
		return 1
	"""


#maximum number of roles to which a permission can belong(e.g. 30)
def cardinality_constraint_of_permission(individual, max_n):
	summa = 0
	for gene in individual[1]:
		semi_summa = 0
		for allele in gene:
			if allele == '1':
				semi_summa += 1
		if semi_summa > max_n:
			return 1
		summa += semi_summa
	
	return summa


#maximum number of users to which a role can have (e.g. 30, role_position as the role of CEO)
def cardinality_constraint_of_user(individual, role_position, max_n):
	summa = 0
	for gene in individual[0]:
		if gene[role_position] == '1':
			summa += 1
	if summa > max_n:
		return 1
	
	return summa


#maximum number of permissions to which a role can have (e.g. 30, role_position as the role of CEO)
def cardinality_constraint_of_permission_role(individual, role_position, max_n):
	summa = 0
	for gene in individual[1]:
		if gene[role_position] == '1':
			summa += 1
	if summa > max_n:
		return 1
	
	return summa


#one individual cannot be a member of both mutually exclusion roles (e.g. 7, 10)
def mutually_exclusive_roles(individual, role_position_1, role_position_2):
	summa = 0
	for gene in individual[0]:
		if gene[role_position] == '1' and gene[role_position_2] == '1':
			summa += 1
	if summa > max_n:
		return 1
	
	return summa



#the mutually exclusive permissions cannot be assigned to the same role (e.g. 8, 20)
def mutually_exclusive_permissions(individual, permission_position_1, permission_role_position_2):
	summa = 0
	for gene in individual[1]:
		if gene[role_position] == '1' and gene[role_position_2] == '1':
			summa += 1
	if summa > max_n:
		return 1
	
	return summa
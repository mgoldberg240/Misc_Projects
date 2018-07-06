# Data will come in in some form like
# coords = [[0, 0], [1, 0], [1, 1], [2, 0]]
# data = [mini_id,tgt,op]
# As of July 6 2018, this is not for use and does nothing

def process_data():
	def make_minis(n,data,coords): # combine these into one
		# coords = [[0, 0], [1, 0], [1, 1], [2, 0]]
		# data = [1,3,'+'] # [mini_id,tgt,op] --- tgt is already parsed from int to str
		minis = np.zeros([n,n])
		minis = puzzle.astype(int)


		for pairs in coords:
			minis[pairs[0],pairs[1]] = data[0]


		
	def targets_ops(data)# when all minis filled out...
		data = [[1,3,'+'],[0,12,'*'],[2,435,'+'],[4,311,'!'],[3,666,'/']]
		data.sort(key=lambda x: x[0]) # order by mini_id

		targets = []
		operators = []
		for mini_data in data:
			targets.append(mini_data[1])
			operators.append(mini_data[2])

		return targets, operators
	return minis,targets,operators
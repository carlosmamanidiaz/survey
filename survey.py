questions = []
answers = []

def get_answer(question, options):

	questions.append(question)
	print(question)
	print('Options-----\n')
	for i,j in options.items():
		print(i + ". " + j)
	option = input('\nPlease select an option: ')

	while not option in list(options.keys()):
		print(f'\nIncorect option. Only valid {list(options.keys())}\n')
		print('Options-----\n')
		for i,j in options.items():
			print(i + ". " + j)
		option = input('\nPlease select an option: ')
	answers.append(options[option])
	print()



ques1 = "Do you need speed storing data?"
opts1 = {"A": "Yes", "B": "No"}
get_answer(ques1, opts1)

ques2 = "How much is your budget?"
opts2 = {"A": "Low", "B": "Medium", "C": "High"}
get_answer(ques2, opts2)

ques3 = "Do you have an IT team?"
opts3 = {"A": "Yes", "B": "No"}
get_answer(ques3, opts3)

ques4 = "Do you have a Data Security team?"
opts4 = {"A": "Yes", "B": "No"}
get_answer(ques4, opts4)

ques5 = "How much is your budget?"
opts5 = {"A": "Low", "B": "Medium", "C": "High"}
get_answer(ques5, opts5)

ques6 = "How much is your budget?"
opts6 = {"A": "Low", "B": "Medium", "C": "High"}
get_answer(ques6, opts6)


print(questions)
print(answers)
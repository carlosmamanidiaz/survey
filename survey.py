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

ques4 = "Does your IT team have knowledge of server and database maintenance?"
opts4 = {"A": "Yes", "B": "No"}
get_answer(ques4, opts4)

ques5 = "Do you have a Data Security team?"
opts5 = {"A": "Yes", "B": "No"}
get_answer(ques5, opts5)

ques6 = "Is the scalability of your database an important factor for your application?"
opts6 = {"A": "Yes", "B": "No"}
get_answer(ques6, opts6)

ques7 = "Is the storage capacity too high?"
opts7 = {"A": "Yes", "B": "No"}

get_answer(ques7, opts7)

ques8 = 'Does the application need your data to be more than 99.99% available?'
opts8 = {"A": "Yes", "B": "No"}

get_answer(ques8, opts8)

ques9 = 'Does the application need 99.99% performance?'
opts9 = {"A": "Yes", "B": "No"}

get_answer(ques9, opts9)

ques10 = 'Data needs to be quickly accessible from anywhere in the world?'
opts10 = {"A": "Yes", "B": "No"}

get_answer(ques10, opts10)


#Tree decision



print(questions)
print(answers)
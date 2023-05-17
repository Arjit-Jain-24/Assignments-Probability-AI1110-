from playsound import playsound
import random

def my_playlist():
	my_list = []
	while len(my_list)<=20:
		number = random.randint(1, 20)
		if number not in my_list:
			my_list.append(number)
			number_str = str(number)
			playsound(f'/home/theprofessor/Desktop/project_probability/songs/'+ number_str +'.mp3')

for times in range(0,5):
    my_playlist()

import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_frame = pandas.DataFrame(data)



#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}



# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()
Nato_string = [new_dict[letter] for letter in user_input]
print(Nato_string)


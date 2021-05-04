import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(new_dict)
# {"A": "Alfa", "B": "Bravo"}

user_typed_correct = False
while not user_typed_correct:
    user_input = input("name \n").upper()

    try:
        nato_list = [new_dict[letter] for letter in user_input]
    except KeyError:
        print("invalid entry")
        pass
    else:
        user_typed_correct = True
        print(nato_list)

# print(nato_list)



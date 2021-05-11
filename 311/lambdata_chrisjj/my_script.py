# Yup
import pandas as pd

from lambdata_chrisjj.my_mod import state_abbr, add_column

print('Hello Lambda! This is my assignment for DS311')

df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]})
newlist = [5, 10, 15, 20, 25]
print(f'Before adding column:\n{df.head()}')
add_column(df, newlist, 'z')
print(f'After adding column:\n{df.head()}')


userInput = input('Enter State name to convert to its abbreviation: ')
print(state_abbr(userInput))

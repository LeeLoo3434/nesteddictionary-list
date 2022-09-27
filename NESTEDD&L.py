# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# # # 
# x[1][0]= "15"
# print(x)
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]["lastname"]= Bryant 
# # In the sports_directory, change 'Messi' to 'Andres'
# sports_directory ['soccer'][0] = "Andres"
# # Change the value 20 in z to 30
# z[0][y] = 30 

# NEXT BLOCK OF CODE #2

# from cgi import print_arguments
# from curses import keyname


# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
# #     ]
# def iterateDictionary(students):
#     for i in (range(len(students))):
#         print (students[i])
#     return students[i]

# print(iterateDictionary(students))

# create a function iterateDictionary2(key_name, some_list) that givven  a list of dictionaries and a key  name, 
# the function prints the value stored in that key for each dictionary. 
# def iterate_dictionary2(key_name,some_list):
#     for element in some_list:
#         print(element[key_name])


# iterate_dictionary2("first_name",students)

# iterate_dictionary2("last_name",students)

# iterate through a dictionary with list values 
# create a function printInfo(some_dict) that given a dictionary whoes values are all list 
# print the name of each key along with  the size of it's list 
# then prints the associated values within each keys list 
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
def printInfo(some_dict):
    for key in some_dict.keys():
        print(f'{len(some_dict[key])} {key}')
        for element in some_dict[key]:
            print (element)
printInfo(dojo)

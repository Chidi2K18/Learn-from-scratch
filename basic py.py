#LIST##################################################################################
#ordered, changeable and allows dupes
#Ordered: meaning that new items will be placed at the end of the list
#Changeable: you can change, add and remove items from the list after its creation
#items can be indexed, like [0] and [1]
new_list = [1,2,3,4,'fish']
tropical = ["mango", "pineapple", "papaya"]
new_list[3] = 'boblina'
new_list[0:2] = 'buns', 'nuns'
new_list.extend(tropical)
#print(len(new_list))
#print(new_list[0:3])

#a shorthand for loop that prints all items in your given list
#[print(x) for x in new_list]
#short hand for loop that only prints if a condition is met
[print(x) for x in new_list if "fish" in new_list]

# if 'fish' in new_list:
#     print(new_list[:-1])
#TUPLE#################################################################################
#Ordered: meaning that new items will be placed at the end of the list
#UnChangeable: you cannot change , add or remove items after the tuple has been made
#dupes allowed
#set
#any data type is accepted even mixed
new_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(new_tuple)
#dict
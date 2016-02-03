shopping_list = ["eggs"]

def add_list(new_item):
    global shopping_list   
    if len(shopping_list) == 1:
        shopping_list[0] = new_item
    elif len(shopping_list) > 1:
        if shopping_list.count(new_item) != 0:
            print "You have already added this item to your list."
        else:
            shopping_list.append(new_item)
    return shopping_list

def remove_item(current_item):
    global shopping_list
    if shopping_list.count(current_item) == 0:
        print "%s is not on your list." % (current_item)
    else:
        shopping_list.remove(current_item)
    return shopping_list

new_item = raw_input("What would you like to add to your shopping list?").lower()
current_item = raw_input("What would you like to remove from your shopping list?")
print add_list(new_item)
print remove_item(current_item)
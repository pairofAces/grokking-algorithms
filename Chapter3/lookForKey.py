#-------create summary------#

# Recursion Example from book


''' 

'Pseudo'

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not None:
        box = pile.grab_a_book()
        for item in box:
            if item.is_a_book():
                pile.append(item)
            elif item.is_a_key():
                print "found the key!"
'''

# Recursive example

'''
'Pseudo'

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)   <----- Recursion
        elif item.is_a_key():
            print "found the key"
'''
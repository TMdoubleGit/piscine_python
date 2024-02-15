# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmichel- <tmichel-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/25 15:36:29 by tmichel-          #+#    #+#              #
#    Updated: 2024/01/25 16:00:44 by tmichel-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
    if (object == None):
        print("Nothing : None", object.__class__)
    elif (object != object):
        print("Cheese : nan", object.__class__)
    elif (object == 0 and object.__class__ == int):
        print("Zero : 0", object.__class__)
    elif (object == ""):
        print("Empty :", object.__class__)
    elif (object is False):
        print("Fake : False", object.__class__)
    else:
        print("Type not found")
        return(1)
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmichel- <tmichel-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/25 14:16:17 by tmichel-          #+#    #+#              #
#    Updated: 2024/01/25 15:20:43 by tmichel-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    if (object.__class__ == list):
        print("List :", object.__class__)
    elif (object.__class__ == tuple):
        print("Tuple :", object.__class__)
    elif (object.__class__ == set):
        print("Set :", object.__class__)
    elif (object.__class__ == dict):
        print("Dict :", object.__class__)
    elif (object.__class__ == str):
        print(object, "is in the kitchen :", object.__class__)
    else:
        print("Type not found")
    return (42)
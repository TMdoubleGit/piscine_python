# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmichel- <tmichel-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/25 16:05:54 by tmichel-          #+#    #+#              #
#    Updated: 2024/01/29 13:13:53 by tmichel-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

ac = len(sys.argv)

def isInt(object : any):
    try:
        int(object)
        return True
    except ValueError:
        return False

try: 
    assert ac == 2, "AssertionError: more than one argument is provided"
    assert isInt(sys.argv[1]) == True, "AssertionError: argument is not an integer"

    nb = sys.argv[1]
    if (int(nb) % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(e)

    
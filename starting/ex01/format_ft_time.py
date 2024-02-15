# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmichel- <tmichel-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/25 11:54:32 by tmichel-          #+#    #+#              #
#    Updated: 2024/01/25 14:14:24 by tmichel-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
import time

date = datetime.now()
elapsed_time = time.time()
formatted_elapsed_time = "{:,.4f}".format(time.time())
scientific_notation = "{:e}".format(elapsed_time)

date_clean = date.strftime("%b %d %Y")

print("Seconds since January 1, 1970: ", formatted_elapsed_time, " or ", scientific_notation, " in scientific notation")
print(date_clean)

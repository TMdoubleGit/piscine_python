# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmichel- <tmichel-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/25 11:54:32 by tmichel-          #+#    #+#              #
#    Updated: 2024/01/25 12:22:59 by tmichel-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
import time
import locale

locale.setlocale(locale.LC_NUMERIC, "en_GB.UTF-8")

date = datetime.now()
elapsed_time = time.time()
formatted_elapsed_time = "{:,.2f}".format(time.time())
scientific_notation = "{:e}".format(elapsed_time)

date_clean = date.strftime("%b %d %Y")

print("Seconds since January 1, 1970: ", formatted_elapsed_time, " or ", scientific_notation, " in scientific notation")
print(date_clean)

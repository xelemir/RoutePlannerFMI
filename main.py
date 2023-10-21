"""
Sample of germany.fmi

# Id : 0
# Timestamp : 1495108694
# Type : maxspeed
# Revision : 1

25115477
50790030
0 122317 53.52826330000000610 10.02327160000000106 0
1 122318 53.52975890000000447 10.02431610000000006 0
2 122320 53.53518340000000109 10.02931140000000099 0
3 122321 53.52797260000000534 10.02411430000000081 0
4 122322 53.52644350000000628 10.02880480000000141 0
5 122323 53.52881789999999995 10.02462870000000095 0
6 122324 53.52923870000000051 10.02413380000000132 0
7 122328 53.52830590000000655 10.02099500000000099 0
8 122329 53.53749640000000198 10.03100220000000142 0
9 122332 53.53903880000000015 10.03227550000000079 0
10 122338 53.54591050000000507 10.01560440000000085 0
11 122339 53.54613020000000034 10.01539630000000081 0
12 122340 53.54706850000000173 10.01455680000000115 0
13 122342 53.54778820000000650 10.00844800000000134 0
14 122343 53.54757370000000094 10.00466839999999991 0
"""

import numpy as np
from MapData import MapData


if __name__ == "__main__":
    # To improve performance, set progressbar to False
    data = MapData("germany.fmi", progressbar=True, timer=True)
    while True:
        
        # Enter coordinates in the format "lat, lon"
        coordinates = input("Enter coordinates: ").split()
        for i in range(len(coordinates)):
            coordinates[i] = coordinates[i].replace(",", "")
        
        nearest_combination = data.find_nearest_lat_lon(float(coordinates[0]), float(coordinates[1]))
        
        print(nearest_combination[1:3])
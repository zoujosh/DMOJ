def touching(x1,y1,x2,y2,x3,y3,x4,y4):
    if min(x1,x2) > max(x3,x4) or min(x3,x4) > max(x1,x2):
        return False
    if min(y1,y2) > max(y3,y4) or min(y3,y4) > max(y1,y2):
        return False
    if x1 == x2:
        slope1 = 0
        intersecting_x = x1
    else:
        slope1 = (y2-y1)/(x2-x1)
        y_intersect1 = y2 - (slope1 * x2)
    
    if x3 == x4:
        slope2 = 0
        intersecting_x = x3
    else:
        slope2 = (y4-y3)/(x4-x3)
        y_intersect2 = y4 - (slope2 * x4)
    
    if x1 == x2 and x3 == x4:
        if x1 == x3:
            return True
        else:
            return False
    elif x1 == x2 and x3 != x4:
        intersecting_y = (slope2 * intersecting_x) + y_intersect2    
    elif x1 != x2 and x3 == x4:
        intersecting_y = (slope1 * intersecting_x) + y_intersect1
    else:
        if slope1 == slope2:
            if y_intersect1 != y_intersect2:
                return False
            else:
                return True
        else:
            intersecting_x = (y_intersect1 - y_intersect2)/(slope2-slope1)
            intersecting_y = (slope1 * intersecting_x) + y_intersect1
            
    if (intersecting_x <= x3 and intersecting_x >= x4) or (intersecting_x >= x3 and intersecting_x <= x4):
        if (intersecting_y <= y3 and intersecting_y >= y4) or (intersecting_y >= y3 and intersecting_y <= y4):
            return True
        else:
            return False
    else:
        return False

x1,y1,x2,y2 = map(int,input().split())

buildings = int(input())

count = 0

for i in range(buildings):
    corners = input().split()
    corners = [int(j) for j in corners]
    total_corners = corners[0]
    corners.pop(0)
    for k in range(total_corners):
        if k == total_corners - 1:
           if touching(x1,y1,x2,y2,corners[k*2],corners[(k*2)+1],
                       corners[0],corners[1]):
               count += 1
               break
        else:
            if touching(x1,y1,x2,y2,corners[k*2],corners[(k*2)+1],
                        corners[(k*2)+2],corners[(k*2)+3]):
                count += 1
                break

print(count)
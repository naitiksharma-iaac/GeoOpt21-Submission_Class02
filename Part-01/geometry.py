import rhino3dm as rg

def createcircleandpoint(N1, N2, R, t):
    
    #Creating Point with rhino3dm
    cnt_pt = rg.Point3d(N1,N2,0)

    #Creating Circle from the Center Point
    cir = rg.Circle(cnt_pt,R)

    #creating parameter point
    pt =  cir.PointAt(t)

    return cir, pt
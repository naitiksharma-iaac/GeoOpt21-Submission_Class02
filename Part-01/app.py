from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/mycirclewithpoint1",
    name="MyCircleWithPoint",
    inputs=[
        hs.HopsInteger("First Number", "N1", "Number in X", hs.HopsParamAccess.ITEM, default= 2),
        hs.HopsInteger("Second Number", "N2", "Number in Y", hs.HopsParamAccess.ITEM, default= 3),
        hs.HopsNumber("Radius", "R", "Specify radius of circle", hs.HopsParamAccess.ITEM, default= 7.0),
        hs.HopsNumber("Parameter","t","Parameter on curve to evaluate", hs.HopsParamAccess.ITEM, default= 0.5)
    ],
    outputs=[
        hs.HopsCurve("Circle", "curve", "Circle", hs.HopsParamAccess.ITEM),
        hs.HopsPoint("point on circle", "parameter","Point on circle at parameter", hs.HopsParamAccess.ITEM)
    ]
)

def mycirclewithpoint1 (N1, N2, R, t):
    crv = geo.createcircleandpoint(N1, N2, R, t)
    pnt = geo.createcircleandpoint(t)
    return crv, pnt


if __name__ == "__main__":
    app.run(debug=True)
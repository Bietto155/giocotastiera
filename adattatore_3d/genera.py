import math, cadquery as cq
# Quote da disegno (mm)
H = 180.0          # altezza totale
T_SQ = 14.0        # spessore flangia quadra
T_RD = 15.0        # spessore flangia tonda
SQ = 240.0         # flangia quadra
SQ_IN = 148.0      # luce quadra
D_RD = 285.0       # flangia tonda
D_BC = 240.0       # interasse fori flangia tonda
D_IN = 150.0       # luce tonda
WALL = 15.0        # parete corpo (Sez. A-A)

z1 = T_RD; z2 = H - T_SQ   # corpo tra le due flange (151)

# Flangia tonda (z=0..15)
rd = cq.Workplane("XY").circle(D_RD/2).extrude(T_RD)
# Flangia quadra (z=166..180)
sq = cq.Workplane("XY").workplane(offset=z2).rect(SQ, SQ).extrude(T_SQ)
# Corpo: raccordo tondo -> quadro
outer = (cq.Workplane("XY").workplane(offset=z1).circle(D_IN/2+WALL)
         .workplane(offset=z2-z1).rect(SQ_IN+2*WALL, SQ_IN+2*WALL).loft())
body = rd.union(sq).union(outer)
# Luce interna passante
inner = (cq.Workplane("XY").workplane(offset=-1).circle(D_IN/2).extrude(z1+1)
         .faces(">Z").workplane().circle(D_IN/2)
         .workplane(offset=z2-z1).rect(SQ_IN, SQ_IN).loft()
         .faces(">Z").workplane().rect(SQ_IN, SQ_IN).extrude(T_SQ+1))
body = body.cut(inner)
# 8 fori Ø22 su Ø240, sfasati 22.5°
pts = [(D_BC/2*math.cos(math.radians(22.5+45*i)), D_BC/2*math.sin(math.radians(22.5+45*i))) for i in range(8)]
body = body.cut(cq.Workplane("XY").workplane(offset=-1).pushPoints(pts).circle(11).extrude(T_RD+2))
# 8 fori Ø12 flangia quadra
p2 = [(x*50, y*105) for x in (-1,1) for y in (-1,1)] + [(x*105, y*50) for x in (-1,1) for y in (-1,1)]
body = body.cut(cq.Workplane("XY").workplane(offset=z2-1).pushPoints(p2).circle(6).extrude(T_SQ+2))

cq.exporters.export(body, "adattatore_quadro_tondo.step")
cq.exporters.export(body, "adattatore_quadro_tondo.stl", tolerance=0.05, angularTolerance=0.1)
bb = body.val().BoundingBox(); print(bb.xlen, bb.ylen, bb.zlen, body.val().isValid(), round(body.val().Volume()/1000,1),"cm3")

import math
import time
    
def straight_forward_line():
  x=0
  y=0
  z=0
  r = 0.5
  with open("particle.mcfunction", "w") as f:
    for i in range (0,1800,36): 
      r = 0.5 + 0.5*math.cos(math.radians(i % 360))
      x = r * math.cos(math.radians(i % 360))
      y = r * math.sin(math.radians(i % 360))
      z += 0.1   
      x = round(x,4)
      y = round(y,4)
      z = round(z,4)
      f.write(f"execute anchored eyes run particle electric_spark ^{x} ^{y} ^{z} 0 0 0 0 1\n")
      f.write(f"execute anchored eyes run particle minecraft:dust{{scale:1.0f,color:[0.0f,0.2f,1f]}} ^{-x} ^{-y} ^{z} 0 0 0 0 1\n")

  #open and read the file after the appending:
  with open("particle.mcfunction") as f:
    print(f.read())
    
def straight_forward_helix(output="particle.mcfunction", max_z=10.0, angle_step_deg=5, z_step=0.03):
    """Generate a helix of particles up to max_z (blocks ahead)."""
    x = y = z = 0.0
    angle_deg = 0.0
    with open(output, "w") as f:
        z = 0.0
        while z <= max_z:
            angle = math.radians(angle_deg % 360)
            # sinusoidally varying radius
            r = 0.5 + 0.5 * math.cos(angle)
            # caret order: ^<x> ^<y> ^<z>  (lateral, vertical, forward)
            x = r * math.cos(angle) - r
            y = r * math.sin(angle)
            f.write(f"execute anchored eyes run particle minecraft:dust{{scale:1.0f,color:[0.0f,0.2f,1f]}} ^{round(x,4)} ^{round(y,4)} ^{round(z,4)} 0 0 0 0 1\n")
            # mirrored strand (optional)
             # mirror by rotating angle 180° to avoid sign mistakes
            a2 = angle + math.pi
            x2 = round(r * math.cos(a2), 4) + r 
            y2 = round(r * math.sin(a2), 4)

            f.write(f"execute anchored eyes run particle minecraft:dust{{scale:1.0f,color:[0.93333f, 0.99216f, 1.0f]}} ^{round(x2,4)} ^{round(y2,4)} ^{round(z,4)} 0 0 0 0 1\n")


            angle_deg += angle_step_deg
            z += z_step

    # show generated file for quick debug
    with open(output, "r") as f:
        print(f.read())  

straight_forward_helix("particle.mcfunction", max_z=10.0, angle_step_deg=5, z_step=0.05)
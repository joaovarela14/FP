#KRYPTONITE

print("Kryptonite phase classifier")

T = float(input("Temperature (K)? "))
P = float(input("Pressure (kPa)? "))

#reta tem como equação y=0.125x 

if P > 50.0 and T<400:
    phase = "SOLID"
elif T >= 400.0 and P>50:
    phase = "LIQUID"
elif 0<P<50 and 0<T<400 and P/T>0.125:
    phase="SOLID"
else:
    phase = "GAS"

print("At {:.1f} K and {:.3f} kPa, Kryptonite is in the {} phase.".format(T, P, phase))


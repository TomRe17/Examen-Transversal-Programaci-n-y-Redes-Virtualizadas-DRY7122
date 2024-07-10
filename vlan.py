VLAN = int(input("Ingrese el número de su VLAN: "))
if VLAN >= 1 and VLAN <= 1005:
    print("Su VLAN:", VLAN, "es de rango normal")
elif VLAN >= 1006 and VLAN <= 4096:
    print("Su VLAN: ",VLAN, "es de rango extendido")
else:
    print("Su VLAN: ",VLAN, "No pertenece a ningun rango")
    
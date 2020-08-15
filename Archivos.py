if __name__ == "__main__":
    arch = "Salida.txt"
    archivo = open(arch, "a")
    archivo.write("Ahorita vemos que pedo \n")
    archivo.write("Me estan dando ganas de bailar un pinche cumbion bien loco \n")
    archivo.close()
    with open(arch,"w") as fp:
        fp.write("que me ve ramirez que me ve ")
    with open(arch, "r") as fp:
        for line in fp.readlines():
            linea = line.split(",")
            print(linea)
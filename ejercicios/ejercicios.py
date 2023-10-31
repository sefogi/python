# Solicitamos al usuario que ingrese el tipo de pizza que desea
tipo_pizza = str(input("que tipo de piza quiere vegetariana o no vegetariana: "))

# Si el usuario ha elegido una pizza vegetariana
if tipo_pizza == "vegetariana":

    # Imprimimos una lista de ingredientes vegetarianos
    ingredientes_pizza_vegetariana = ["pimiento", "tofu"]
    print(f"los ingredientes vegetarianos son: {ingredientes_pizza_vegetariana}")
    ingrediente_selecionado = str(input("selecione solo un ingrediente: "))
    print("en este momento estamos relizando su pizza vegetariana")

# Si el usuario ha elegido una pizza no vegetarianaa
elif tipo_pizza == "no vegetariana":

    # Imprimimos una lista de ingredientes no vegetarianos
    ingredientes_pizza_no_vegetariana = ["peperoni", "jamon", "salmon"]
    print(f"los ingredientes no veganos son: {ingredientes_pizza_no_vegetariana}")
    ingrediente_selecionado = str(input("selecione solo un ingrediente: "))
    if ingrediente_selecionado ==  "peperoni":
        print("en este momento estamos realizando su pizza no vegetariana con peperoni mozarella y tomate")
    elif ingrediente_selecionado == "jamon":
        print("en este momento estamos realizando su pizza no vegetariana con jamon mozarella y tomate")
    elif ingrediente_selecionado == "salmon":
        print("en este momento estamos realizando su pizza no vegetariana con salmomn mozarella, tomate")






    
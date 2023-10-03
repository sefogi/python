#elif= significa caso contrario

ingreso_mensual = 5000
gasto_mensual = 8000

# if anidadas (con elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien pa, estas bien")
    else:
        print("estas gastando mucho, hay que ver si te alcanza")
        
    
    
    
elif ingreso_mensual > 1000:
    print("estas bien ecomomicamente en latinoamerica")

    
else:
    print("sos pobre")


#!/usr/bin/env python3

import cgi

# Obtener los datos del formulario
form = cgi.FieldStorage()
nombre = form.getvalue('nombre', 'Visitante')  # Valor predeterminado si no se proporciona
email = form.getvalue('email', 'No proporcionado')

# Generar la cabecera de la respuesta HTTP
print("Content-Type: text/html\n")

# Generar el contenido HTML de la respuesta
print(f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario Recibido</title>
    <style>
        body {{
            background-color: #111;  /* Fondo negro */
            color: #ff0000;  /* Texto rojo */
            font-family: 'Arial Black', sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
        h1 {{
            font-size: 3rem;
            text-transform: uppercase;
            letter-spacing: 0.1rem;
        }}
        p {{
            font-size: 1.5rem;
            margin-top: 20px;
            color: #fff;
        }}
        strong {{
            color: #ff0000;  /* Resaltar el email en rojo */
        }}
        header {{
            background: #222;
            padding: 20px;
            width: 100%;
            border-bottom: 2px solid #ff0000;
        }}
        footer {{
            position: fixed;
            bottom: 0;
            width: 100%;
            background: #222;
            padding: 10px 0;
            border-top: 2px solid #ff0000;
            color: #fff;
            font-size: 0.9rem;
        }}
        .verbenas {{
            margin-top: 30px;
            font-size: 1.2rem;
            text-shadow: 2px 2px 4px #ff0000;
        }}
        .icon-metal {{
            margin-top: 20px;
            font-size: 3rem;
        }}
    </style>
</head>
<body>
    <header>
        <h1>¡Gracias por tu solicitud, {nombre}!</h1>
    </header>
    <main>
        <p>Guardamos tu email <strong>{email}</strong> para futuras comunicaciones sobre las fiestas de Campillos y sus verbenas cercanas.</p>
        <div class="verbenas">
            <p>Las verbenas están a la vuelta de la esquina, ¡prepara tu mejor atuendo metalero y que empiece la fiesta!</p>
        </div>
        <div class="icon-metal">🤘</div>
    </main>
    <footer>
        <p>Campillos, Málaga - ¡Donde las verbenas y el metal se encuentran!</p>
    </footer>
</body>
</html>
""")

# #!/usr/bin/env python3

# import cgi

# # Obtener los datos del formulario
# form = cgi.FieldStorage()
# nombre = form.getvalue('nombre', 'Visitante')  # Valor predeterminado si no se proporciona
# email = form.getvalue('email', 'No proporcionado')

# # Generar la cabecera de la respuesta HTTP
# print("Content-Type: text/html\n")

# # Generar el contenido HTML de la respuesta
# print(f"""
# <!DOCTYPE html>
# <html lang="es">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Formulario Recibido</title>
# </head>
# <body>
#     <h1>Muchas gracias por su solicitud, {nombre}.</h1>
#     <p>Guardamos su email <strong>{email}</strong> para futuras comunicaciones sobre las fiestas de Campillos y sus verbenas cercanas.</p>
# </body>
# </html>
# """)
	
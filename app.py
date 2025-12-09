from flask import Flask, render_template, request

app = Flask(__name__)

# Cantidad de productos por página
PRODUCTOS_POR_PAGINA = 15   # podés cambiarlo a 20, 30, etc.

# Datos de ejemplo (se pueden cargar de una base en el futuro)
productos = [

    # --- NUEVOS EJEMPLOS (AGREGADOS ARRIBA) ---

    {
        "base": "RUG [02-10]", "bin": "557910", "exp_date": "12/26", "seller": 7,
        "bank": "Santander México", "price": "Consult", "level": "STANDARD",
        "class": "Debit", "type": "MASTERCARD", "country": "MX"
    },

    {
        "base": "RUG [02-10]", "bin": "481283", "exp_date": "12/27", "seller": 7,
        "bank": "Banorte", "price": "Consult", "level": "CLASSIC",
        "class": "Debit", "type": "VISA", "country": "MX"
    },

    {
        "base": "RUG [02-10]", "bin": "540104", "exp_date": "12/28", "seller": 7,
        "bank": "Nu México", "price": "Consult", "level": "GOLD",
        "class": "Credit", "type": "MASTERCARD", "country": "MX"
    },

    {
        "base": "RUG [02-10]", "bin": "542878", "exp_date": "12/29", "seller": 7,
        "bank": "Santander México", "price": "Consult", "level": "PREMIUM",
        "class": "Credit", "type": "MASTERCARD", "country": "MX"
    },

    {
        "base": "RUG [02-10]", "bin": "75150", "exp_date": "12/30", "seller": 7,
        "bank": "Banorte", "price": "Consult", "level": "STANDARD",
        "class": "Debit", "type": "MASTERCARD", "country": "MX"
    },

    {
        "base": "RUG [02-10]", "bin": "01900", "exp_date": "12/31", "seller": 7,
        "bank": "Nu México", "price": "Consult", "level": "PLATINUM",
        "class": "Credit", "type": "AMERICAN EXPRESS", "country": "MX"
    },

    {
        "base": "RUG [02-10]", "bin": "526424", "exp_date": "12/26", "seller": 7,
        "bank": "Santander México", "price": "Consult", "level": "STANDARD",
        "class": "Debit", "type": "MASTERCARD", "country": "MX"
    },

    {
        "base": "RUG [02-10]", "bin": "52953", "exp_date": "12/27", "seller": 7,
        "bank": "Banorte", "price": "Consult", "level": "GOLD",
        "class": "Credit", "type": "MASTERCARD", "country": "MX"
    },

    {
        "base": "RUG [02-10]", "bin": "540104", "exp_date": "12/28", "seller": 7,
        "bank": "Nu México", "price": "Consult", "level": "STANDARD",
        "class": "Debit", "type": "MASTERCARD", "country": "MX"
    },

    # --- MÉXICO (TUS PRODUCTOS ORIGINALES) ---

    {"base": "RUG [02-10]", "bin": "554718", "exp_date": "03/30", "seller": 7,
     "bank": "Banco Santander, S.A", "price": "1,298$MXN", "level": "STANDARD",
     "class": "Debit", "type": "MASTERCARD", "country": "MX"},

    {"base": "RUG [02-10]", "bin": "526777", "exp_date": "08/32", "seller": 7,
     "bank": "Nu Bn Servicios Mexico S.A. De C.V.", "price": "925$MXN", "level": "GOLD",
     "class": "Credit", "type": "MASTERCARD", "country": "MX"},

    {"base": "CONTROL [02-10]", "bin": "416916", "exp_date": "04/28", "seller": 73,
     "bank": "Bancoppel S.A. Institucion De Banca Multiple", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "MX"},

    {"base": "OBSCURE [02-10]", "bin": "557920", "exp_date": "07/28", "seller": 7,
     "bank": "Scotiabank Inverlat, S.A.", "price": "1,403$MXN", "level": "STANDARD",
     "class": "Debit", "type": "MASTERCARD", "country": "MX"},

    {"base": "OBSCURE [02-10]", "bin": "526498", "exp_date": "04/28", "seller": 7,
     "bank": "Banco Inbursa, S.A.", "price": "Consult", "level": "PREPAID",
     "class": "Debit", "type": "MASTERCARD", "country": "MX"},

    {"base": "OBSCURE [02-10]", "bin": "415231", "exp_date": "01/27", "seller": 7,
     "bank": "Bbva Bancomer, S.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "MX"},

    {"base": "OBSCURE [02-10]", "bin": "547046", "exp_date": "12/27", "seller": 7,
     "bank": "Santander Consumo, S.A. De C.V. Sofom, E.R.", "price": "Consult", "level": "GOLD",
     "class": "Credit", "type": "MASTERCARD", "country": "MX"},

    {"base": "OBSCURE [02-10]", "bin": "415231", "exp_date": "10/25", "seller": 7,
     "bank": "Bbva Bancomer, S.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "MX"},

    # --- ARGENTINA ---
    {"base": "OBSCURE [02-10]", "bin": "439818", "exp_date": "01/29", "seller": 7,
     "bank": "Banco Provincia de Buenos Aires", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "AR"},

    {"base": "OBSCURE [02-10]", "bin": "525562", "exp_date": "04/27", "seller": 9,
     "bank": "Global Processing S.A.", "price": "Consult", "level": "PREPAID",
     "class": "Debit", "type": "MASTERCARD", "country": "AR"},

    {"base": "OBSCURE [02-10]", "bin": "554730", "exp_date": "02/27", "seller": 7,
     "bank": "Mercadolibre S.R.L.", "price": "Consult", "level": "PREPAID",
     "class": "Debit", "type": "MASTERCARD", "country": "AR"},

    {"base": "OBSCURE [02-10]", "bin": "525855", "exp_date": "09/28", "seller": 6,
     "bank": "Bancar Tecnología S.A.", "price": "Consult", "level": "PREPAID",
     "class": "Debit", "type": "MASTERCARD", "country": "AR"},

    # --- PERÚ ---
    {"base": "ENEMY [02-10]", "bin": "411823", "exp_date": "07/29", "seller": 73,
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "PREPAID",
     "class": "Credit", "type": "VISA", "country": "PE"},

    {"base": "ENEMY [02-10]", "bin": "498503", "exp_date": "12/28", "seller": 73,
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "PE"},

    {"base": "ENEMY [02-10]", "bin": "498503", "exp_date": "02/29", "seller": 73,
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "PE"},

    {"base": "ENEMY [02-10]", "bin": "498503", "exp_date": "01/29", "seller": 73,
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "PE"},

    {"base": "ENEMY [02-10]", "bin": "498503", "exp_date": "10/28", "seller": 73,
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "PE"},

    {"base": "ENEMY [02-10]", "bin": "498503", "exp_date": "11/27", "seller": 73,
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "PE"},

    {"base": "ENEMY [02-10]", "bin": "498503", "exp_date": "01/27", "seller": 73,
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "PE"},

    {"base": "ENEMY [02-10]", "bin": "498503", "exp_date": "05/29", "seller": 3,
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "MASTERCARD", "country": "PE"},

    {"base": "ENEMY [02-10]", "bin": "498503", "exp_date": "05/28", "seller": 73,
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "CLASSIC",
     "class": "Debit", "type": "VISA", "country": "PE"}
]

# ---------------- PAGINACIÓN ---------------- #

@app.route("/")
def catalogo():
    pagina = request.args.get("pagina", 1, type=int)

    inicio = (pagina - 1) * PRODUCTOS_POR_PAGINA
    fin = inicio + PRODUCTOS_POR_PAGINA

    productos_pagina = productos[inicio:fin]

    total_paginas = (len(productos) + PRODUCTOS_POR_PAGINA - 1) // PRODUCTOS_POR_PAGINA

    return render_template("index.html",
                           productos=productos_pagina,
                           pagina_actual=pagina,
                           total_paginas=total_paginas)

# ----------------- NUEVAS SECCIONES ------------------

@app.route("/categorias")
def categorias():
    return render_template("categorias.html")

@app.route("/gratis")
def gratis():
    return render_template("gratis.html")

# -------- SUB-SECCIONES DE CATEGORÍAS -------- #

@app.route("/sistemas")
def sistemas():
    return render_template("sistemas.html")

@app.route("/proxys")
def proxys():
    return render_template("proxys.html")

@app.route("/cracking")
def cracking():
    return render_template("cracking.html")

@app.route("/vpns")
def vpns():
    return render_template("vpns.html")

if __name__ == "__main__":
    app.run(debug=True)

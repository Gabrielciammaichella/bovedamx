from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo (se pueden cargar de una base en el futuro)
productos = [
    # --- MÉXICO ---
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

    {"base": "OBSCURE [02-10]", "bin": "525562", "exp_date": "04/27", "seller": 7, 
     "bank": "Global Processing S.A.", "price": "Consult", "level": "PREPAID", 
     "class": "Debit", "type": "MASTERCARD", "country": "AR"},

    {"base": "OBSCURE [02-10]", "bin": "554730", "exp_date": "02/27", "seller": 7, 
     "bank": "Mercadolibre S.R.L.", "price": "Consult", "level": "PREPAID", 
     "class": "Debit", "type": "MASTERCARD", "country": "AR"},

    {"base": "OBSCURE [02-10]", "bin": "525855", "exp_date": "09/28", "seller": 7, 
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

    {"base": "ENEMY [02-10]", "bin": "498503", "exp_date": "05/28", "seller": 73, 
     "bank": "Banco Interamericano De Finanzas, S.A.E.M.A.", "price": "Consult", "level": "CLASSIC", 
     "class": "Debit", "type": "VISA", "country": "PE"},
]

@app.route("/")
def catalogo():
    return render_template("index.html", productos=productos)

if __name__ == "__main__":
    app.run(debug=True)

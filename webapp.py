# webapp.py (Flask UI)
from flask import Flask, render_template, request, redirect, url_for, flash
from src.sweet_shop import SweetShop
from src.sweet import Sweet

app = Flask(__name__)
app.secret_key = 'supersecretkey'

shop = SweetShop()

@app.route('/')
def index():
    sweets = shop.view_sweets()
    return render_template('index.html', sweets=sweets)

@app.route('/add', methods=['GET', 'POST'])
def add_sweet():
    if request.method == 'POST':
        try:
            sid = request.form['id']
            if not sid.isdigit():
                raise ValueError("ID must be a valid integer.")
            name = request.form['name']
            category = request.form['category']
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])

            sweet = Sweet(int(sid), name, category, price, quantity)
            shop.add_sweet(sweet)
            flash('Sweet added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('add_sweet'))

    return render_template('add_sweet.html')

@app.route('/delete/<int:sid>')
def delete_sweet(sid):
    try:
        shop.delete_sweet(sid)
        flash('Sweet deleted.', 'info')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('index'))

@app.route('/purchase/<int:sid>', methods=['POST'])
def purchase_sweet(sid):
    try:
        qty_str = request.form['quantity']
        if not qty_str.strip():
            raise ValueError("Amount of items must be selected for purchase.")
        qty = int(qty_str)
        if qty <= 0:
            raise ValueError("No items chosen for purchase.")
        shop.purchase(sid, qty)
        flash('Purchase successful!', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('index'))

@app.route('/restock/<int:sid>', methods=['POST'])
def restock_sweet(sid):
    try:
        qty_str = request.form['quantity']
        if not qty_str.strip():
            raise ValueError("Amount of items must be selected for restocking.")
        qty = int(qty_str)
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0.")
        shop.restock(sid, qty)
        flash('Restocked successfully!', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
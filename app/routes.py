from flask import render_template, request, redirect, url_for, flash
from . import app, db
from .models import Product, Transaction

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    products = Product.query.all()
    low_stock = [p for p in products if p.stock <= p.minimum]
    return render_template('index.html', products=products, low_stock=low_stock)

@app.route('/add_product', methods=['POST'])
def add_product():
    barcode = request.form['barcode']
    name = request.form['name']
    minimum = int(request.form.get('minimum', 0))

    if Product.query.filter_by(barcode=barcode).first():
        flash('Producto ya existe')
        return redirect(url_for('index'))

    product = Product(barcode=barcode, name=name, minimum=minimum)
    db.session.add(product)
    db.session.commit()
    flash('Producto agregado')
    return redirect(url_for('index'))

@app.route('/transaction', methods=['POST'])
def transaction():
    barcode = request.form['barcode']
    quantity = int(request.form['quantity'])
    tx_type = request.form['type']

    product = Product.query.filter_by(barcode=barcode).first()
    if not product:
        flash('Producto no encontrado')
        return redirect(url_for('index'))

    if tx_type == 'OUT' and product.stock < quantity:
        flash('Stock insuficiente')
        return redirect(url_for('index'))

    product.stock = product.stock + quantity if tx_type == 'IN' else product.stock - quantity
    tx = Transaction(product_id=product.id, quantity=quantity, type=tx_type)
    db.session.add(tx)
    db.session.commit()
    flash('Transaccion registrada')
    return redirect(url_for('index'))

@app.route('/history')
def history():
    transactions = Transaction.query.order_by(Transaction.timestamp.desc()).all()
    return render_template('history.html', transactions=transactions)

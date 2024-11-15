from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm, AddProductForm


@app.route('/')
@app.route('/index')
def index():
    """shop URL"""
    return render_template("index.html" , title='index page')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'you are requesting to login{form.username.data}')
        return redirect(url_for("index"))
    return render_template('Login.html', title='login page', form=form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    """register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'you are requesting to register{form.username.data}')
        return redirect(url_for("login"))
    return render_template('register.html', title='Register page', form=form)


@app.route('/add-product', methods = ['GET', 'POST'])
def add_product():
    """add product URL"""
    form = AddProductForm()
    if form.validate_on_submit():
        flash(f'you are requesting to Add a Product{form.product_name.data}')
        return redirect(url_for("index"))
    return render_template('add_product.html', title='Add Product page', form=form)


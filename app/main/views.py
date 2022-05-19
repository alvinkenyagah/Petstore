import secrets
from flask import render_template,abort,redirect, url_for,request,flash,session
from flask_login import login_required
from . import main
from ..models import Category,Addproduct
from .. import db,photos
from .forms import  Addproducts


# from ..email import mail_message


@main.route ('/')
def index():
    msg= 'heeloo'
    return render_template('index.html',msg=msg)


@main.route('/quiz',methods=['GET','POST'])

def quiz():
    return render_template('quiz.html')

@main.route('/product',methods=['GET','POST'])
def product():
    return render_template('products.html')

@main.route('/addcategory',methods=['GET','POST'])
def addcategory():
    if request.method=='POST':
        getcategory=request.form.get('category')
        category=Category(name=getcategory)
        db.session.add(category)
        flash(f"The category {getcategory} was added to your database","sucess")
        db.session.commit()
        return redirect(url_for('main.addcategory'))
    return render_template('products/addcategory.html',category='category')

@main.route('/addproduct', methods=['GET','POST'])
def addproduct():
    form = Addproducts(request.form)
    categories = Category.query.all()
    if request.method=="POST"and 'image_1' in request.files:
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.description.data
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        addproduct = Addproduct(name=name,price=price,discount=discount,stock=stock,colors=colors,desc=desc,category_id=category,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addproduct)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('main.admin'))
    return render_template('products/addproduct.html', form=form, title='Add a Product',categories=categories)


@main.route('/admin')
def admin():
    products = Addproduct.query.all()
    print(products)
    return render_template('admin/index.html', title='Admin page',products=products)

@main.route('/category')
def categories():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/category.html', title='categories',categories=categories)

@main.route('/updatecategory/<int:id>',methods=['GET','POST'])
def updatecat(id):
    # if 'email' not in session:
    #     flash('Login first please','danger')
    #     return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')  
    if request.method =="POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('main.category'))
    category = updatecat.name
    return render_template('products/addcategory.html', title='Update cat',updatecat=updatecat)


@main.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    form = Addproducts(request.form)
    product = Addproduct.query.get_or_404(id)
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        product.name = form.name.data 
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data 
        product.colors = form.colors.data
        product.desc = form.description.data
        product.category_id = category
        product.brand_id = brand
        if request.files.get('image_1'):
            try:
                # os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                # os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                # os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('/admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.description.data = product.desc
    brand = product.brand.name
    category = product.category.name
    return render_template('products/addproduct.html', form=form, title='Update Product',getproduct=product,categories=categories)

from flask_wtf import FlaskForm,Form
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,TextAreaField,SelectField,FloatField,IntegerField,FileField
from wtforms.validators import DataRequired,Email,EqualTo
from flask_wtf.file import FileAllowed,FileRequired
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter your username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class Addproducts(Form):
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price',validators= [DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock',validators= [DataRequired()])
    colors = StringField('Colors',validators= [DataRequired()])
    description = TextAreaField('Description',validators= [DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
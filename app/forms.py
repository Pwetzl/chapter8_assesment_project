from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
 
class LoginForm(FlaskForm):

    username = StringField ('Username', validators= [DataRequired(), Length(8, 15)])
    password = PasswordField ('Password', validators= [DataRequired()])
    remember_me = BooleanField ('Remember me')
    submit = SubmitField ('login')

class RegisterForm(FlaskForm):

    username = StringField ('Username', validators= [DataRequired(), Length(8, 15)])
    password = PasswordField ('Password', validators= [DataRequired()])
    submit = SubmitField ('Register')

class AddProductForm(FlaskForm):

    product_name = StringField ('Product Name', validators= [DataRequired(), Length(8, 15)])
    product_description = StringField ('Product Description ', validators= [DataRequired(), Length(8, 15)])
    stock_available = SelectField ('Stock Available', choices=[('1', '1'), ('2', '2'), ('3', '3')])

    submit = SubmitField ('Add product')


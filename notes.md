# export FLASK_APP=run.py
# export FLASK_DEBUG=1
# flask run
# from flask_blog import db
# db.create_all()
# from flask_blog import User, Post
# user_2 = User(username='john doe', email='jd@demo.com', password='password')
# db.session.create_all()
# db.session.add(<user>)
# db.session.commit()
# User.query.all()
# >>> User.query.first()
# User('john doe, 'jd@demo.com', 'default.jpg')
# >>> User.query.filter_by(username='Corey'))
#   File "<stdin>", line 1
#     User.query.filter_by(username='Corey'))
#                                           ^
# SyntaxError: invalid syntax
# >>> User.query.filter_by(username='Corey')
# <flask_sqlalchemy.BaseQuery object at 0x1043b8860>
# >>> User.query.filter_by(username='Corey').all()

>>> from flask_bcrypt import Bcrypt
>>> bcrypt=Bcrypt()
>>> bcrypt.generate_password_hash('testing')
b'$2b$12$L/9ILKuBt43ih.9fEVxeYOCRbHtcXU9OY.394YL3Adc2f9hVarFyK'
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$whokBL4vjizTRv/COQD2YuaHtIpCZfAavPeU/7n7lZyCXIxRVYKJO'
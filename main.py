# Manual imports
from website.views import home
from website.views import auth
from website.views import chat
from website.views import shop
from website.views import user
from website.views import blog
from website.views import doctors
from website.views import search
from website.views.app import app


app.register_blueprint(home.home,        url_prefix='/',         method=['GET', 'POST'])
app.register_blueprint(auth.auth,        url_prefix='/auth',     method=['GET', 'POST'])
app.register_blueprint(chat.chat,        url_prefix='/chat',     method=['GET', 'POST'])
app.register_blueprint(shop.shop,        url_prefix='/shop',     method=['GET', 'POST'])
app.register_blueprint(user.user,        url_prefix='/user',     method=['GET', 'POST'])
app.register_blueprint(blog.blog,        url_prefix='/blog',     method=['GET', 'POST'])
app.register_blueprint(doctors.doctors,  url_prefix='/doctors',  method=['GET', 'POST'])
app.register_blueprint(search.search,    url_prefix='/search',   method=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)

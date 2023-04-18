from flask import Flask, escape, request, Response, render_template, redirect, make_response, session
import base64

app = Flask(__name__)
# Set secure cookie so people can't just authenticate themselves!
app.config['SESSION_COOKIE_SECURE'] = True
app.config['REMEMBER_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
app.secret_key = "&Trym7By!=4jK7bAg(_8-jR[Hs]+]"

# Create a class to hold information about a pickle
class Pickle:
    def __init__(self, name, description, price, image):
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.image_data = base64.b64encode(self.read_image_from_disk()).decode('utf-8')
    def read_image_from_disk(self):
        with open("static/img/" + self.image, 'rb') as f:
            return f.read()

@app.route('/')
def hello():
    # If the auth cookie is true, show admin panel
    if 'auth' not in session or session['auth'] == False:
        return redirect('/signin')
    # Otherwise, show the login page
    else:
        return render_template('admin.html', title='Admin Panel')


# Preview a pickle. Take GET parameters name, description, price, image.
@app.route('/preview', methods=['GET'])
def preview():
    # Make sure user is authenticated
    if 'auth' not in session or session['auth'] == False:
        return redirect('/signin')
    else:
        name = request.args.get('name')
        description = request.args.get('description')
        price = request.args.get('price')
        image = request.args.get('image')

        # Create a pickle object
        pickle = Pickle(name, description, price, image)

        return render_template('preview.html', pickle=pickle, title='Preview Pickle')

# Get method to /signin will render the login page
@app.route('/signin')
def login():
    return render_template('login.html', title='Login')

# Create a logout route
@app.route('/logout')
def logout():
    # Delete the auth cookie
    session.pop('auth', None)
    # Redirect to the login page
    return redirect('/signin')

@app.route('/favicon.ico')
def favicon():
    return Response(open('static/img/favicon.ico', 'rb').read(), mimetype='image/x-icon')

# Post method to /login will authenticate the admin
@app.route('/signin', methods=['POST'])
def admin_auth():
    username = request.form.get("username")
    password = request.form.get("password")

    # Read the admin password from a file
    with open("flag.txt", "r") as f:
        admin_password = f.read()

    if username == "admin" and password == admin_password:
        # Set the flask secure cookie
        session['auth'] = True
        return redirect('/')
    else:
        # Display a 401 error and a message
        return Response(status=401, response="Invalid username or password")

@app.route('/source')
def source():
    # Return the source code of the app fron the current directory
    # TODO: Remove in production.
    with open(__file__, 'r') as f:
        return Response(f.read(), mimetype='text/plain')
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a more secure secret key

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if the username and password are correct
        if request.form['username'] == 'deekshibapv@gmail.com' and request.form['password'] == 'password':
            # Set the username in the session
            session['username'] = request.form['username']
            # Redirect to the custom5.html page
            return redirect(url_for('custom_page'))
        else:
            # Display an error message if the login credentials are incorrect
            return render_template('login.html', error='Invalid username or password')

    # Render the login page template
    return render_template('login.html')

@app.route("/index")
def custom_page():
    # Check if the user is logged in
    if 'username' in session:
        # Render the custom5.html page
        return render_template("index.html")
    else:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)

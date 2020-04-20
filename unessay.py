from flask import Flask, request, render_template, redirect, url_for, flash


app = Flask(__name__) 


# @app.route('/loggedIn') 


@app.route('/loggedIn/<user>')
def loggedIn(user=None):
    return render_template("login.html", user=user)


#default is GET so we add POST here since this is the only place they'll submit a form to a URL, no need elsewhere
@app.route('/', methods= ['GET', 'POST'])
def index():
    error= None
    if request.method == 'POST':
        #username must be root and password must be 123456. Determined here, else invalid password
        if request.form['username'] != 'root' or request.form['password'] != '123456':
            error= 'Invalid login, please try again.'
        else:
            return redirect(url_for('loggedIn', user= request.form['username'])) 
    return render_template("home.html", error= error) 



#main
if __name__ == "__main__":
    app.run(debug=True)







#####################             NOTES             #####################

    #@app.route('/', methods=['GET', 'POST'])
    #def index():
        #if request.method == 'POST':  # postman app can help test/visualize this
            #return 'You are using post'
        #else:
            #return 'u r using get

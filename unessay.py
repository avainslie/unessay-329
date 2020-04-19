from flask import Flask, request, render_template, redirect, url_for, flash
# request gives us info how a user requested a source(web page)

app = Flask(__name__) # help it determine the root path
#app.secret_key='what ever you want'

# templates dir for html files and static for css files

#@app.route('/')
#def index():
    #return 'Method used: %s' % request.method
# routing/mapping -- route a URL to a return value (see comment two lines below). GET method
# the @ signifies a decorator which is a way to wrap a function and modify its behaviour
#@app.route('/') # this can be changed to like /about if you wanted an about page for ex. Ties a URL to python function
#def index():
    #return 'This is the homepage' # always need a return statement


@app.route('/loggedIn', methods= ['GET', 'POST']) # by default it only handles GET so we add POST to that as well
@app.route('/loggedIn/<user>', methods= ['GET', 'POST'])
def loggedIn(user=None): # by default set user to none, can override with a name tho
    return render_template("login.html", user=user) # the user=user part goes with the html file

@app.route('/', methods= ['GET', 'POST'])  # variables in URL are always in angle brackets
# if the variable was an integer you need to say <int: ur_number>
def index():
    error= None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error= 'Invalid login, please try again.'
            #flash('wrong login')
            #return redirect(url_for('index'))

        else:
            return redirect(url_for('loggedIn', user= request.form['username'])) # how to say here that user= 'username'????. url_for generates an endpoint
    return render_template("home.html", error= error) # look in template dir for the file

# i know i have to redirect to refresh but how do i tell it to do that when i press refresh?? aka submit form again?
        #return redirect(url_for('index'))

if __name__ == "__main__": # checks we only start webserver if file called directly, if its the main file
    app.run(debug=True)

#####################             NOTES             #####################

    #@app.route('/', methods=['GET', 'POST'])
    #def index():
        #if request.method == 'POST':  # postman app can help test/visualize this
            #return 'You are using post'
        #else:
            #return 'u r using get

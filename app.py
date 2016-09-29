from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth", methods = ['POST'])
def authenticate():
    if request.form['username'] == 'donald' and request.form['password'] == 'duck':
        return render_template('result.html', to_return = 'Success, you have logged in!')
    return return_template('result.html', to_return = 'Failure, please use correct credentials')

    
if __name__ == "__main__":
    app.debug = True 
    app.run()

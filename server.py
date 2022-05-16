from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)
    # Create a new instance of the Flask class called "app"
@app.route('/')  
def hello():
    return "Hello World!"        # The "

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def hiName(name):
    print(name)
    return 'Hi ' +name+ '!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    print(num)
    print(word)
    return (word * int(num))

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

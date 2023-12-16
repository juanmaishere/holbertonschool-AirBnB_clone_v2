from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('user_input')
    print(f"User entered: {user_input}")
    user_input2 = request.form.get('user_input2')
    print(f"User entered: {user_input2}")
    user_input3 = request.form.get('user_input3')
    print(f"User entered: {user_input3}")

    # You can perform additional actions with the user input here

    return f"User entered: {user_input} User entered: {user_input2} User entered: {user_input3}"

if __name__ == '__main__':
    app.run(debug=True)
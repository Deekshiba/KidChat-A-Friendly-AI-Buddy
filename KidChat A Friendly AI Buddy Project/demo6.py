from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from flask import Flask, json, render_template, request, jsonify, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a more secure secret key

class IntentAdapter(LogicAdapter):

    def can_process(self, statement):
        # The intent adapter can process any input
        return True

    def process(self, input_statement, additional_response_selection_parameters):
        response = None
        for intent_data in training_data:
            if input_statement.text.lower() in intent_data['patterns']:
                response = random.choice(intent_data['responses'])
                break
        
        if not response:
            response = self.bot.storage.get_random()

        statement = Statement(response)
        statement.confidence = 1

        return statement

bot = ChatBot(
    "chatbot",
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Sorry, I don't have an answer.",
            "maximum_similarity_threshold": 0.90,
        },
        {
            "import_path": "chatterbot.logic.MathematicalEvaluation"
        },
        {
            "import_path": "chatterbot.logic.UnitConversion"
        },
        {
            "import_path": "__main__.IntentAdapter"
        }
    ],
)


# Load the JSON data from a file
with open('training_data.json', 'r') as file:
    training_data = json.load(file)

# Now, training_data is a list containing all the intents, patterns, and responses
# You can access individual intents and their corresponding data like this:
for intent_data in training_data:
    intent = intent_data['intent']
    patterns = intent_data['patterns']
    responses = intent_data['responses']
    
@app.route("/")
def main():
    if 'username' in session:
        return render_template("demo5.html")
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop('username', None)

        if request.form['password'] == 'password':  # Replace 'password' with your actual password
            session['username'] = request.form['username']
            return redirect(url_for('main'))

        return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/get_response", methods=["POST"])
def get_response():
    if 'username' not in session:
        return jsonify({"bot_response": "Please login to use the chatbot."})

    user_message = request.form["user_message"]

    # Check if the user wants to end the chat
    if user_message.lower() == 'exit':
        return jsonify({"bot_response": "Chat Ended...."})

    # Create a Statement object with search_text attribute set
    statement = Statement(user_message)
    statement.search_text = user_message

    bot_response = str(bot.get_response(statement))

    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
    

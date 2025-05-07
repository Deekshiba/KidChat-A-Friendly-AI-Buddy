from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a more secure secret key

class PuzzleAdapter(LogicAdapter):
    def can_process(self, statement):
        return True

    def process(self, input_statement, additional_response_selection_parameters):
        response = None
        for puzzle_data in puzzle_data_list:
            if input_statement.text.lower() in puzzle_data['questions']:
                response = random.choice(puzzle_data['responses'])
                break

        if not response:
            response = self.bot.storage.get_random()

        statement = Statement(response)
        statement.confidence = 1

        return statement

bot = ChatBot(
    "puzzle_bot",
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Sorry, I don't have an answer.",
            "maximum_similarity_threshold": 0.90,
        },
        {
            "import_path": "__main__.PuzzleAdapter"
        }
    ],
)

puzzle_data_list = [
    {
        "questions": ["what has keys but can't open locks?", "key"],
        "responses": ["Correct! The answer is key.", "You got it! The answer is key.", "Well done! The answer is key."],
        "hint": "It is something you might use to play a musical instrument.",
        "clue_given": False
    },
    {
        "questions": ["what comes once in a minute, twice in a moment, but never in a thousand years?", "m"],
        "responses": ["Correct! The answer is m.", "You got it! The answer is m.", "Well done! The answer is m."],
        "hint": "It's a letter of the alphabet.",
        "clue_given": False
    },
    {
        "questions": ["what is full of holes but still holds water?", "sponge"],
        "responses": ["Correct! The answer is sponge.", "You got it! The answer is sponge.", "Well done! The answer is sponge."],
        "hint": "It's something you might use in the shower.",
        "clue_given": False
    },
    {
        "questions": ["what has a head, a tail, but no body?", "coin"],
        "responses": ["Correct! The answer is coin.", "You got it! The answer is coin.", "Well done! The answer is coin."],
        "hint": "It's something you might find in your pocket.",
        "clue_given": False
    },
    {
        "questions": ["I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "echo"],
        "responses": ["Correct! The answer is echo.", "You got it! The answer is echo.", "Well done! The answer is echo."],
        "hint": "It's something you might hear in a canyon.",
        "clue_given": False
    },
    {
        "questions": ["What has a neck but no head?", "bottle"],
        "responses": ["Correct! The answer is bottle.", "You got it! The answer is bottle.", "Well done! The answer is bottle."],
        "hint": "It's commonly used to hold beverages.",
        "clue_given": False
    },
    {
        "questions": ["What has to be broken before you can use it?", "egg"],
        "responses": ["Correct! The answer is egg.", "You got it! The answer is egg.", "Well done! The answer is egg."],
        "hint": "It's a common breakfast food.",
        "clue_given": False
    },
    {
        "questions": ["What goes up but never comes down?", "age"],
        "responses": ["Correct! The answer is age.", "You got it! The answer is age.", "Well done! The answer is age."],
        "hint": "It's something that increases over time.",
        "clue_given": False
    },
    {
        "questions": ["What has many keys but can't open a single lock?", "piano"],
        "responses": ["Correct! The answer is piano.", "You got it! The answer is piano.", "Well done! The answer is piano."],
        "hint": "It's a musical instrument.",
        "clue_given": False
    },
    {
        "questions": ["What is always in front of you but can't be seen?", "future"],
        "responses": ["Correct! The answer is future.", "You got it! The answer is future.", "Well done! The answer is future."],
        "hint": "It's something that hasn't happened yet.",
        "clue_given": False
    },
    {
        "questions": ["What has hands but cannot clap?", "clock"],
        "responses": ["Correct! The answer is clock.", "You got it! The answer is clock.", "Well done! The answer is clock."],
        "hint": "It's used to tell time.",
        "clue_given": False
    },
    {
        "questions": ["What has one eye but can't see?", "needle"],
        "responses": ["Correct! The answer is needle.", "You got it! The answer is needle.", "Well done! The answer is needle."],
        "hint": "It's used for sewing.",
        "clue_given": False
    },
    {
        "questions": ["What is so delicate that saying its name breaks it?", "silence"],
        "responses": ["Correct! The answer is silence.", "You got it! The answer is silence.", "Well done! The answer is silence."],
        "hint": "It's the absence of sound.",
        "clue_given": False
    },
    {
        "questions": ["What has a head, a tail, is brown, and has no legs?", "penny"],
        "responses": ["Correct! The answer is penny.", "You got it! The answer is penny.", "Well done! The answer is penny."],
        "hint": "It's a type of coin.",
        "clue_given": False
    },
    {
        "questions": ["What can you catch but not throw?", "cold"],
        "responses": ["Correct! The answer is cold.", "You got it! The answer is cold.", "Well done! The answer is cold."],
        "hint": "It's a common illness.",
        "clue_given": False
    },
    {
        "questions": ["The more you take, the more you leave behind. What am I?", "footsteps"],
        "responses": ["Correct! The answer is footsteps.", "You got it! The answer is footsteps.", "Well done! The answer is footsteps."],
        "hint": "It's left behind when you walk.",
        "clue_given": False
    },
    {
        "questions": ["What can travel around the world while staying in a corner?", "stamp"],
        "responses": ["Correct! The answer is stamp.", "You got it! The answer is stamp.", "Well done! The answer is stamp."],
        "hint": "It's used to send mail.",
        "clue_given": False
    },
    {
        "questions": ["What belongs to you but is used more by others?", "name"],
        "responses": ["Correct! The answer is name.", "You got it! The answer is name.", "Well done! The answer is name."],
        "hint": "It's something people call you by.",
        "clue_given": False
    },
    {
        "questions": ["What has a head, a tail, is brown, and has no legs?", "penny"],
        "responses": ["Correct! The answer is penny.", "You got it! The answer is penny.", "Well done! The answer is penny."],
        "hint": "It's a form of currency.",
        "clue_given": False
    },
    {
        "questions": ["What can you break, even if you never pick it up or touch it?", "promise"],
        "responses": ["Correct! The answer is promise.", "You got it! The answer is promise.", "Well done! The answer is promise."],
        "hint": "It's something you make to someone.",
        "clue_given": False
    },
    {
        "questions": ["What gets wetter as it dries?", "towel"],
        "responses": ["Correct! The answer is towel.", "You got it! The answer is towel.", "Well done! The answer is towel."],
        "hint": "It's used to dry yourself after a shower.",
        "clue_given": False
    },
    {
        "questions": ["What can you hold in your right hand, but never in your left hand?", "left hand"],
        "responses": ["Correct! The answer is left hand.", "You got it! The answer is left hand.", "Well done! The answer is left hand."],
        "hint": "It's a body part.",
        "clue_given": False
    },
    {
        "questions": ["What comes once in a year, twice in a month, but never in a week?", "e"],
        "responses": ["Correct! The answer is e.", "You got it! The answer is e.", "Well done! The answer is e."],
        "hint": "It's a letter of the alphabet.",
        "clue_given": False
    },
    {
        "questions": ["What has one eye but cannot see?", "needle"],
        "responses": ["Correct! The answer is needle.", "You got it! The answer is needle.", "Well done! The answer is needle."],
        "hint": "It's used for sewing.",
        "clue_given": False
    },
    {
        "questions": ["I'm tall when I'm young, and I'm short when I'm old. What am I?", "candle"],
        "responses": ["Correct! The answer is candle.", "You got it! The answer is candle.", "Well done! The answer is candle."],
        "hint": "It's something that can be lit.",
        "clue_given": False
    },
    {
        "questions": ["What has to be broken before you can use it?", "egg"],
        "responses": ["Correct! The answer is egg.", "You got it! The answer is egg.", "Well done! The answer is egg."],
        "hint": "It's a common breakfast item.",
        "clue_given": False
    },
    {
        "questions": ["What has keys but can't open locks?", "keyboard"],
        "responses": ["Correct! The answer is keyboard.", "You got it! The answer is keyboard.", "Well done! The answer is keyboard."],
        "hint": "It's something you use to type on a computer.",
        "clue_given": False
    },
    {
        "questions": ["What gets wet while drying?", "towel"],
        "responses": ["Correct! The answer is towel.", "You got it! The answer is towel.", "Well done! The answer is towel."],
        "hint": "It's something you use to dry off after a shower.",
        "clue_given": False
    },
    {
        "questions": ["What has a bottom at the top?", "legs"],
        "responses": ["Correct! The answer is legs.", "You got it! The answer is legs.", "Well done! The answer is legs."],
        "hint": "They help you move around.",
        "clue_given": False
    },
    {
        "questions": ["What has a head and a tail but no body?", "coin"],
        "responses": ["Correct! The answer is coin.", "You got it! The answer is coin.", "Well done! The answer is coin."],
        "hint": "It's used as money.",
        "clue_given": False
    },
    {
        "questions": ["What is full of holes but still holds water?", "sponge"],
        "responses": ["Correct! The answer is sponge.", "You got it! The answer is sponge.", "Well done! The answer is sponge."],
        "hint": "It's used for cleaning.",
        "clue_given": False
    },
    {
        "questions": ["What can you break, even if you never pick it up or touch it?", "promise"],
        "responses": ["Correct! The answer is promise.", "You got it! The answer is promise.", "Well done! The answer is promise."],
        "hint": "It's something you give to someone.",
        "clue_given": False
    },
    {
        "questions": ["I'm light as a feather, yet the strongest man can't hold me for much longer than a minute. What am I?", "breath"],
        "responses": ["Correct! The answer is breath.", "You got it! The answer is breath.", "Well done! The answer is breath."],
        "hint": "It's something you do without thinking.",
        "clue_given": False
    },
    {
        "questions": ["What has to be broken before you can use it?", "egg"],
        "responses": ["Correct! The answer is egg.", "You got it! The answer is egg.", "Well done! The answer is egg."],
        "hint": "It's a common breakfast item.",
        "clue_given": False
    },
    {
        "questions": ["What has keys but can't open locks?", "keyboard"],
        "responses": ["Correct! The answer is keyboard.", "You got it! The answer is keyboard.", "Well done! The answer is keyboard."],
        "hint": "It's something you use to type on a computer.",
        "clue_given": False
    }
]

list_trainer = ListTrainer(bot)

for item in puzzle_data_list:
    questions = item["questions"]
    responses = item["responses"]
    list_trainer.train(questions)
    list_trainer.train(responses)

user_answer = None
current_question = None

@app.route("/")
def main():
    global current_question
    if 'username' in session:
        current_question = random.choice(puzzle_data_list)
        return render_template("puzzle_demo.html", question=current_question['questions'][0])
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop('username', None)

        if request.form['password'] == 'password':
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
    global user_answer, current_question

    if 'username' not in session:
        return jsonify({"bot_response": "Please login to use the chatbot."})

    user_message = request.form["user_message"]

    if user_answer is None:
        user_answer = user_message.lower()
        if user_answer == current_question['questions'][1]:
            bot_response = str(random.choice(current_question['responses']))
            puzzle_data_list.remove(current_question)
            if puzzle_data_list:
                current_question = random.choice(puzzle_data_list)
            else:
                current_question = None
        else:
            current_question['clue_given'] = False
            bot_response = "Try again!"

    else:
        if user_message.lower() == current_question['questions'][1]:
            bot_response = str(random.choice(current_question['responses']))
            puzzle_data_list.remove(current_question)
            if puzzle_data_list:
                current_question = random.choice(puzzle_data_list)
            else:
                current_question = None
            user_answer = None
        else:
            if not current_question['clue_given']:
                bot_response = current_question['hint']
                current_question['clue_given'] = True
            else:
                bot_response = "Sorry, that's incorrect. The answer is " + current_question['questions'][1]

    if current_question:
        return jsonify({"bot_response": bot_response, "question": current_question['questions'][0]})
    else:
        return jsonify({"bot_response": "You have completed all the puzzles!", "question": ""})

if __name__ == "__main__":
    app.run(debug=True)
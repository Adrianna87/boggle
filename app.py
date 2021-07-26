from flask import Flask, session, request, render_template,jsonify
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"

boggle_game = Boggle()

@app.route("/")
def main():
  # make boggle board
  board = boggle_game.make_board()
  session['board'] = board
  highscore = session.get("highscore", 0)
  nplays = session.get("nplays", 0)
  
  # Why is it "board=board" etc?
  return render_template("index.html", 
  board=board, highscore=highscore, nplays=nplays)

@app.route("/submit-word")
def dictionary():
  # Copied but I understand what the code is doing.
  # Still having trouble coming up with the code on my own.
  word = request.args["word"]
  board = session["board"]
  response = boggle_game.check_valid_word(board, word)

  return jsonify({'result': response})


@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update nplays, update high score if appropriate."""

    # ???
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)

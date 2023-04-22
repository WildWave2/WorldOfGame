from flask import Flask
import Utils

SCORES_FILE_NAME = Utils.SCORES_FILE_NAME

app = Flask(__name__)


def get_score():
    try:
        with open(SCORES_FILE_NAME, 'r') as f:
            score = f.read().strip()
            return int(score)
    except Exception as e:
        return str(e)


@app.route('/')
def score_server():
    score = get_score()
    if isinstance(score, int):
        return f'''
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is <div id="score">{score}</div></h1>
                </body>
            </html>
        '''
    else:
        return f'''
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1><div id="score" style="color:red">{score}</div></h1>
                </body>
            </html>
        '''


def main():

    import threading
    flask_thread = threading.Thread(target=app.run)
    flask_thread.daemon = True
    flask_thread.start()

    from Live import main as live_main
    live_main()

if __name__ == '__main__':
    main()

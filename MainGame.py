from Live import main as live_main
from MainScores import score_server
from multiprocessing import Process

if __name__ == '__main__':
    # Start the Flask server in a separate process
    score_process = Process(target=score_server)
    score_process.start()

    # Start the game
    live_main()

    # Stop the Flask server process when the game is over
    score_process.terminate()
    score_process.join()

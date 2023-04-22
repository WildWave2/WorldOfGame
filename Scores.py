import Utils

SCORES_FILE_NAME = Utils.SCORES_FILE_NAME
POINTS_OF_WINNING = 0


def update_score(difficulty):
    try:
        score_file = SCORES_FILE_NAME
        with open(score_file, 'r') as f:
            file_contents = f.read().strip()
            if not file_contents:
                current_score = 0
            else:
                current_score = int(file_contents)
            new_score = current_score + int(difficulty) * 3 + 5
    except FileNotFoundError:
        print(f"Error: file '{score_file}' not found")
        new_score = int(difficulty) * 3 + 5
    except ValueError:
        print(f"Error: file '{score_file}' contains non-numeric characters")
        return -1

    with open(score_file, 'w') as f:
        f.write(str(new_score))

    return new_score




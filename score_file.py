from pathlib import Path

def read_best_score(path_file) :
    if path_file.is_file() and path_file.exists():
        score_content = path_file.read_text()
        return score_content
    else:
        return '* There is no file with the specified name'
    
def change_best_score_file(score_file_content, best_score_file, best_score):
    if int(score_file_content) < int(best_score):
        best_score_file.write_text(str(best_score))
        
import difflib
import tkinter as tk
from tkinter import filedialog

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return list(set(" ".join([line.strip() for line in lines]).split(" ")))

def find_similar_words(query, word_list, k=3):
    similarities = [(difflib.SequenceMatcher(None, query, word).ratio(), word) for word in word_list]
    suggestions = sorted(similarities, key=lambda x: x[0], reverse=True)[:k]
    suggestions = [suggestion[1] for suggestion in suggestions] 
    suggestions = [''.join(char for char in text if char.isalpha()) for text in suggestions]
    return suggestions

def load_file():
    file_path = filedialog.askopenfilename(title="Select a Text File")
    if file_path:
        print("File Path : ",file_path)
        return read_file(file_path)
    else:
        return []

def main():
    words = []
    root = tk.Tk()
    root.withdraw()  
    
    # Hide the main window

    while not words:
        words = load_file()

    user_input = input("Input >> ").strip()
    suggestions = find_similar_words(user_input, words)
    if suggestions:
        print("Output >>", ', '.join(suggestions))
    else:
        print("No suggestions found.")
    
    # root.mainloop()

if __name__ == "__main__":
    main()


from graph import Graph,Vertex
import string
import random
import os
import re

def get_words_from_text(text_path):
    if not os.path.exists(text_path):
        raise FileNotFoundError(f"File not found: {text_path}")

    with open(text_path, 'rb') as file:
        text = file.read().decode('utf-8')



        text = ' '.join(text.split())
        text = text.lower()

        text = text.translate(str.maketrans('', '', string.punctuation))
 
    words = text.split()
    words = words[:1000]
    return words 

def make_graph(words):
    g = Graph()

    previous_word = None

    for word in words:
        word_vertex =  g.get_vertex(word)

        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex 

    print(f"Graph vertices: {list(g.get_vertex_values())}")
    
    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    composition = []

    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    
    return composition

def main():
    words = get_words_from_text(os.path.join('texts','sorcerer_stone.txt'))

    if not words:
        raise ValueError("No words were found in the input text file.")
    
    g = make_graph(words)

    composition = compose(g,words,100)

    print(' '.join(composition))



if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
<<<<<<< HEAD






=======
>>>>>>> 9ae5d8cd81836a885b280013003fef9a5cb9735f

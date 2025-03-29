import streamlit as st 
import string
import random

class Vertex:
    def __init__(self,value):
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []

    def increment_edge(self,vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for vertex,weight in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        if not self.neighbors:
            return None
        return random.choices(self.neighbors,weights=self.neighbors_weights)[0]

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self,value):
        if value not in self.vertices:
            self.vertices[value] = Vertex(value)
    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)  
        return self.vertices[value]
    
    def get_next_word(self,current_vertex):
        next_word = self.vertices[current_vertex.value].next_word()
        if next_word is None:
            return random.choice(list(self.vertices.values()))
        return next_word
    
    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()


def get_words_from_text(text):
    text = ' '.join(text.split())
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    words = text.split()
    return words


def make_graph(words ,word_limit=None):
    g = Graph()

    if word_limit and word_limit > 0:
        words = words[:word_limit]

    previous_word = None 
    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex

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
    st.title('Markov Chain Text Composer')

    uploaded_file = st.file_uploader("Upload a text file",type=['txt'])

    if uploaded_file is not None:
        text = uploaded_file.getvalue().decode('utf-8')

        word_limit = st.slider('Word Limit',min_value = 10,value=1000)
                                

        output_length = st.slider('Output Length of words',min_value =10,value=1000)



        if st.button("Generate Text"):
            words = get_words_from_text(text)

            if not words:
                st.error("No words were found in the input text file.")
            else:
                effective_word_limit = None if word_limit == 0 else word_limit
                g = make_graph(words, effective_word_limit)    

                composition = compose(g,words,output_length)
                st.text_area("Generated Text:", ' '.join(composition),height=400)

    st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; font-size: 20px;">
        Made with ❤️ by Nihal Khan Ghauri
    </div>
    """,
    unsafe_allow_html=True
)

if __name__ == '__main__':
    main()






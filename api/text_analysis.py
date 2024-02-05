from flask import jsonify, request
from collections import Counter
from . import app
import wikipedia

base_path = "/v1"
word_freq_analysis_path = "/word-frequency-analysis"
search_history_path = "/search-history"

search_history = []

@app.route(base_path + word_freq_analysis_path, methods=['GET'])
def word_frequency_analysis():
    '''
    Get the top 'n' most frequent words from the 'topic' 
    '''
    topic = request.args.get('topic') #value of query parameter - topic
    n = int(request.args.get('n')) #value of query parameter - n

    try:
        page = wikipedia.page(topic) # get the wikipedia page for topic
        text = page.content # convert the content into text, easy to work on text
        top_words = get_top_words(text, n)# get n most frequent words
        search_history.append({'topic': topic, 'top_words': top_words}) # store search history in list
        return jsonify({'top_words': top_words}) # return n most frequent words in json format
    except wikipedia.exceptions.PageError:
        return jsonify({'error': 'Page not found'}), 404 # return if page is not found
    
@app.route(base_path + search_history_path, methods=['GET'])
def search_history_endpoint():
    '''
    Get the search history
    '''
    return jsonify(search_history)

def get_top_words(text, n):
    words = text.split() #split the words in the text
    word_count = Counter(words) # get the count of each word in words
    top_words = word_count.most_common(n) # get n most frequent words
    return top_words
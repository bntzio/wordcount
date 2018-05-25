from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['text']
    word_list = text.split()

    dictionary = {}
    for word in word_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    sorted_words = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    top_words = sorted_words[:3]

    return render(request, 'count.html', { 'text': text, 'count': len(word_list), 'dictionary': sorted_words, 'top': top_words })

def about(request):
    return render(request, 'about.html')

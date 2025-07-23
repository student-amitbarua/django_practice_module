# first_app/views.py
from django.shortcuts import render
import datetime

def home(request):
    d = {
        'author': 'rahim',
        'age': 20,
        'lst': ['python', 'is', 'best'],

        'list' : ['Apple', 'mango','orange'],

        'list_1': [{'cat'},
                    {'dog'},
                    {'bird'}
                    
                    ],

        'val' : [ 6, 4, 2],

        'name_lst': [
                      {'name': 'Jisan', 'age': 19},
                      {'name': 'Dev', 'age': 22},
                      {'name': 'piyal', 'age': 31},
                     ],

        'birthday' : datetime.datetime.now(),
        'courses': [
            {
                'id': 1,
                'name': 'python',
                'fees': 4000
            },
            {
                'id': 2,
                'name': 'java',
                'fees': 7000
            },
            {
                'id': 3,
                'name': 'C++',
                'fees': 8000
            }
        ]
    }
    return render(request, 'home.html', d)
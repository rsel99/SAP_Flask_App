from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, flash
import math
from flask_paginate import Pagination, get_page_args


def prime(number):
    # v1
    '''
    if number <= 1:
        return False
        
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    '''

    # v2
    '''
    if number <= 1:
        return False

    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
    '''

    # v3
    if number <= 1:
        return False
    if number == 2:
        return True
    elif number % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

# def seive(number):
#     # v4
#     prime = [True for i in range(number + 1)]
#     prime[0] = prime[1] = False

#     p = 2
#     while p**2 <= number:
#         if prime[p] == True:
#             for i in range(p**2, number + 1, p):
#                 prime[i] = False
#         p += 1
    

#     for i in range(2, number):



app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:number>", methods=['GET'])
def listNums(number):
    numbers = range(1, number + 1)

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page', per_page=18)
    partition = numbers[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=len(numbers), css_framework='bootstrap4')

    return render_template("listNums.html", qualifier=" ", number=number, numbers=partition, page=page, per_page=per_page, pagination=pagination)

@app.route("/<int:number>/odd", methods=['GET'])
def listOddNums(number):
    # v1
    # odds = [i for i in range(1, number + 1) if i % 2 != 0]
    
    # v2
    odds = range(1, number + 1, 2)

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page', per_page=18)
    partition = odds[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=len(odds), css_framework='bootstrap4')

    return render_template("listNums.html", qualifier=" Odd ", number=number, numbers=partition, page=page, per_page=per_page, pagination=pagination)

@app.route("/<int:number>/even", methods=['GET'])
def listEvenNums(number):
    # v1
    # evens = [i for i in range(1, number + 1) if i % 2 == 0]
    
    # v2
    evens = range(2, number + 1, 2)
    
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page', per_page=18)
    partition = evens[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=len(evens), css_framework='bootstrap4')

    return render_template("listNums.html", qualifier=" Even ", number=number, numbers=partition, page=page, per_page=per_page, pagination=pagination)

@app.route("/<int:number>/prime", methods=['GET'])
def listPrimeNums(number):
    primes = [i for i in range(1, number + 1) if prime(i)]

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page', per_page=18)
    partition = primes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=len(primes), css_framework='bootstrap4')

    return render_template("listNums.html", qualifier=" Prime ", number=number, numbers=partition, page=page, per_page=per_page, pagination=pagination)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

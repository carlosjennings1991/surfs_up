from flask import Flask

app = Flask(__name__)

# list_of_tuples = [
#     (1,2),
#     ('a', 'b'),
#     (99, 'WaffleHaüs'),
#     ('Australia', 25)
# ]

@app.route('/')
def hello_world():
    return 'Hello world' * 10
# def transformer(first, second):
#     return (str(first) + str(second)) * 2

# print([transformer(g, h) for g, h in list_of_tuples])
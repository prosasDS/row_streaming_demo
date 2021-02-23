from flask import Flask, Response, stream_with_context
import random 

APP = Flask(__name__)

@APP.route('/data_request/<int:rowcount>', methods=['GET'])

def get_request(rowcount):
    """returns n rows of fabricated data""" 
    def gen():
        for i in range(rowcount):

            class_target = round(random.uniform(0,1))
            print(class_target) ## just to see some output in terminal

            labels = ('Large','Medium','Small')
            ordinal_var = random.choice(labels)

            amount = round(random.uniform(100, 10000), 2)

            yield f"({class_target}, '{ordinal_var}', {amount})\n"
    return Response(stream_with_context(gen())) 

if __name__ == '__main__':
    APP.run(debug=True)
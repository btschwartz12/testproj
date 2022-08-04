# http://127.0.0.1/
# http://localhost:8000/?data=piper

"""https://forge.autodesk.com/en/docs/oauth/v2/tutorials/get-3-legged-token/

edit app: https://forge.autodesk.com/myapps/DCU%2520Config%2520%2526%2520System%2520Frequencies%2520Tool/view

On step 2


Cannot get callback url with full path just localhost """

from flask import Flask, request

app = Flask(__name__)

def process_code(code):
    print("******code: " + code)


@app.route('/')
def index():
    print('args:', request.args)  # display text in console

    #print('form:', request.form)
    #print('data:', request.data)
    #print('json:', request.json)
    #print('files:', request.files)
    text = request.args.get('data', 'none')
    code = request.args.get('code', 'none')
    process_code(code)
    text += "\npiper is a good dog"
    return text

@app.route('/callback/')
def callback():
    print('args:', request.args)  # display text in console

    #print('form:', request.form)
    #print('data:', request.data)
    #print('json:', request.json)
    #print('files:', request.files)
    text = request.args.get('data', 'none')
    code = request.args.get('code', 'none')

    text += "\nrowdy is a good dog"
    return text




if __name__ == '__main__':
    app.run(port=8000, debug=True)


from flask import *

app = Flask(__name__)


#チャンネル一覧
@app.route('/')
def index():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect('/login')

    return render_template('index.html')



if __name__ =='__main__':
    app.run()
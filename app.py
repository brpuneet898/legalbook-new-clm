from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai-generate-draft')
def ai_generate_draft():
    return render_template('aidraft.html')

if __name__ == '__main__':
    app.run(debug=True)
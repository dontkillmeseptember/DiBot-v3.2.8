from misc.util import Flask, Thread

app = Flask(__name__)

@app.route('/')
def home():
  return "DiBot V4.9.2"

def run():
  app.run(host='0.0.0.0', port=80)

def keep_alive():
  t = Thread(target=run)
  t.start()
from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form['data']
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('static/qrcode.png')
    return render_template('generate.html')

if __name__ == '__main__':
    app.run(debug=True)

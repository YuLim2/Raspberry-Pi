from flask import Flask, request
from flask import render_template
from db import Database
import RPi.GPIO as GPIO

app = Flask(__name__)
leddb = Database.Database()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/led/on")
def led_on():
    try:
        GPIO.output(8, GPIO.HIGH)
        #데이터 저장
        leddb.insertJson("led on!!")
        return "ok"
    except:
        return "fail"

@app.route("/led/off")
def led_off():
    try:
        GPIO.output(8, GPIO.LOW)
        #데이터 저장
        leddb.insertJson("led off!!")
        return "ok"
    except:
        return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

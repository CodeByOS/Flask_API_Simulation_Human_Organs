from flask import Flask, jsonify, request
import random
import time
app = Flask(__name__)

class CardiacSimulator:
    def __init__(self):
        self.condition = "normal"
    def get_status(self):
        return {
            "organ": "heart",
            "condition": self.condition
        }
    def get_parameters(self):
        return {
            "conditions" : ["normal", "tachycardie", "bradycardie", "arythmie", "hypertension"]
        }
    def simulate(self, condition):
        self.condition = condition
        return {
            "message": "Condition applied",
            "condition": condition
        }
    def generate_data(self):
        if self.condition == "tachycardie":
            hr = random.randint(110, 160)
        elif self.condition == "bradycardie":
            hr = random.randint(40, 55)
        elif self.condition == "arythmie":
            hr = random.randint(60, 100)
        return {
            "heart_rate": hr,
            "blood_pressure": {
                "systolic": random.randint(110, 140),
                "diastolic": random.randint(70, 90),
            },
                "timestamp": time.time()
        }
info = CardiacSimulator()
@app.get("/api/cardiac/status")
def status():
    return jsonify(info.get_status())
@app.get("/api/cardiac/data")
def data():
    return jsonify(info.generate_data())
@app.post("/api/cardiac/simulate/<condition>")
def simulate(condition):
    return  jsonify(info.simulate(condition))
@app.get("/api/cardiac/parameters")
def parameters():
    return jsonify(info.get_parameters())

if __name__ == "__main__":
    app.run(port=5001, debug=True)
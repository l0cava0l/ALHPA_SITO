# AlphaBot.py modificato per lo sviluppo
class AlphaBot(object):
    def __init__(self, in1=12, in2=13, ena=6, in3=20, in4=21, enb=26):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4
        self.ENA = ena
        self.ENB = enb
        print("AlphaBot inizializzato in modalità simulazione")

    def forward(self):
        print("AlphaBot: Avanti")

    def stop(self):
        print("AlphaBot: Stop")

    def backward(self):
        print("AlphaBot: Indietro")

    def left(self):
        print("AlphaBot: Sinistra")

    def right(self):
        print("AlphaBot: Destra")
        
    def setPWMA(self, value):
        print(f"AlphaBot: PWMA impostato a {value}")

    def setPWMB(self, value):
        print(f"AlphaBot: PWMB impostato a {value}")
        
    def setMotor(self, left, right):
        print(f"AlphaBot: Motore sinistro={left}, destro={right}")
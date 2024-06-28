from django.apps import AppConfig
#instalar si o si flask y paypalrestsdk
from flask import Flask, request, redirect, render_template
import paypalrestsdk


paypalrestsdk.configure({
    "mode": "sandbox", # Cambia a "live" cuando estés listo para producción
    "client_id": "AUBMcf79fg571ExKIy5bym8nmZYcYSls0x-UuQpRG5aHwjpff8nVTmzAFVgM-CoG2vhN3r1eXjJA4LzC",
    "client_secret": "EOBnORMK0aPtlalqCEY88dTU1ZCkqWUCLwsryBAt9ggVEBndvF2Bl311rIRnY3CscGYz2QDCu8A9Wpb4"
})

app = Flask(__name__)


@app.route('/')
def donation_page():
    return render_template('donation.html')

@app.route('/paypal/return')
def paypal_return():
    payment_id = request.args.get('paymentId')
    payment = paypalrestsdk.Payment.find(payment_id)
    
    if payment.execute({"payer_id": request.args.get('PayerID')}):
        print("Payment execute successfully")
        return "Payment executed successfully"
    else:
        print(payment.error)
        return "Payment failed"

@app.route('/paypal/cancel')
def paypal_cancel():
    return "Payment cancelled"

if __name__ == "__main__":
    app.run(debug=True)



class PortafolioappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PortafolioApp'

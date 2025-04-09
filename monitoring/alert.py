import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Logging Konfiguration
logging.basicConfig(
    filename='system_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_alert(subject, message):
    """Sendet E-Mail mit deinen Zugangsdaten"""
    sender_email = "lf8gruppe03@gmx.de"
    receiver_email = "lf8gruppe3@gmail.com"
    password = "hallosahr123"
    
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        with smtplib.SMTP_SSL('mail.gmx.net', 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        
        logging.info(f"E-Mail gesendet: {subject}")
    except Exception as e:
        logging.error(f"E-Mail Fehler: {str(e)}")

def check_threshold(value, name):
    """Angepasste Grenzwerte (Festplatte >61% löst Warnung aus)"""
    thresholds = {
        "CPU": {"soft": 80, "hard": 95},
        "RAM": {"soft": 75, "hard": 90},
        "Festplatte": {"soft": 61, "hard": 80}
    }
    
    soft = thresholds[name]["soft"]
    hard = thresholds[name]["hard"]
    
    if value > hard:
        alert_msg = f"🚨 KRITISCH! {name} >{hard}% (Aktuell: {value}%)"
        send_alert(f"ALARM: {name} >{hard}%", alert_msg)
    elif value > soft:
        warning_msg = f"⚠ WARNUNG! {name} >{soft}% (Aktuell: {value}%)"
        send_alert(f"Warnung: {name} >{soft}%", warning_msg)
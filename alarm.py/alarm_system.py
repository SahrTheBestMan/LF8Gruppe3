import smtplib
import logging
from datetime import datetime

# Konfiguration für Logdatei
logging.basicConfig(filename='system_monitor.log', level=logging.INFO)

def send_email(subject, message, to_email):
    """Versendet eine E-Mail bei Überschreiten eines Grenzwertes."""
    from_email = "lf8gruppe3@gmail.com"
    password = "SahrFlynnBehnaz"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, f"Subject: {subject}\n\n{message}")
    server.quit()

def log_event(message):
    """Protokolliert das Event in eine Logdatei"""
    logging.info(f"{datetime.now()} - {message}")

def check_limit(value, soft_limit, hard_limit, value_name):
    """Überprüft, ob der Wert die festgelegten Grenzwerte überschreitet"""
    if value > hard_limit:
        log_event(f"Hard limit überschritten: {value_name} ist {value}%")
        send_email(f"Hard Limit Alarm für {value_name}", f"{value_name} hat den Hard-Limit von {hard_limit}% überschritten!", "recipient@example.com")
    elif value > soft_limit:
        log_event(f"Soft limit überschritten: {value_name} ist {value}%")
        send_email(f"Soft Limit Alarm für {value_name}", f"{value_name} hat den Soft-Limit von {soft_limit}% überschritten!", "recipient@example.com")

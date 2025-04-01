import psutil

def check_memory_usage(soft_limit=80, hard_limit=90):
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    
    if memory_percent > hard_limit:
        send_alarm_email(f"Hardlimit reached! Memory usage: {memory_percent}%")
    elif memory_percent > soft_limit:
        log_warning(f"Softlimit reached! Memory usage: {memory_percent}%")
        
def send_alarm_email(message):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = "your_email@example.com"
    receiver_email = "receiver@example.com"
    password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Server Alarm"
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

def log_warning(message):
    with open("system_log.txt", "a") as log_file:
        from datetime import datetime
        log_file.write(f"{datetime.now()} - {message}\n")

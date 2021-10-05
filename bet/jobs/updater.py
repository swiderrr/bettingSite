from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from bet.functions import givePoint

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(givePoint, 'interval', days=1, start_date='2021-10-05 12:00:00')
    scheduler.start()
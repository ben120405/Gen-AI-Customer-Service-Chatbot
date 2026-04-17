import sys
import os
import schedule
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ingestion.vector_update import update_db

DATA_FOLDER = "data_sources/incoming"


def job():

    print("Checking for new knowledge files...")

    for file in os.listdir(DATA_FOLDER):

        if file.endswith(".csv"):

            path = os.path.join(DATA_FOLDER, file)

            update_db(path)


print("Scheduler started. Waiting for scheduled jobs...")

schedule.every(10).seconds.do(job)  # for testing

# production version
# schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
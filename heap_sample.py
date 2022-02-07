import datetime
import heapq

def email(frequency, details):
    current = datetime.datetime.now()
    while True:
        current += frequency
        yield current, details

if __name__ == "__main__":
        fast_email = email(datetime.timedelta(minutes=15), "fast email")
        slow_email = email(datetime.timedelta(minutes=40), "slow email")

        unified = heapq.merge(fast_email, slow_email)
        for _ in range(10):
                print(next(unified))

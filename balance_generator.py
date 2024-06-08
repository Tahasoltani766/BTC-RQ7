import random
import time
import os



def start_generator(file_path='balance.txt'):
    while True:
        previous_balance = 0.0
        current_balance = 0.0

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read().strip()
                if content:
                    previous_balance = float(content)

        # interval = random.uniform(1, 5)
        # time.sleep(interval)

        random_number = random.uniform(0.0000000000001, 0.0001)
        current_balance += random_number

        total_balance = previous_balance + current_balance

        with open(file_path, 'w') as file:
            file.write(f'{total_balance:.20f}')

        print(total_balance)



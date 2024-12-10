import time
import random
from functools import wraps

def exponential_retry(max_retries=5, base_delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    print(f"Attempt {attempt + 1}: Success!")
                    return result
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_retries - 1:
                        print("All retries failed!")
                        raise
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    print(f"Retrying in {delay:.2f} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator

@exponential_retry(max_retries=5, base_delay=1)
def unreliable_api_call():
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("API call failed!")
    return "Success!"

try:
    response = unreliable_api_call()
    print("Final Response:", response)
except Exception:
    print("API calls completely failed after retries.")

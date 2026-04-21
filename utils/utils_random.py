import random
import string
def random_alfanum(n:int)->str:
    return ''.join(random.choice(string.ascii_uppercase +string.ascii_uppercase + string.digits) for _ in range(n))

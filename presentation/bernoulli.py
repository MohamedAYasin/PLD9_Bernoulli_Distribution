import random

p_heads = 0.5
coin_flips = [random.random() < p_heads for _ in range(3)]
results = ['Heads' if flip else 'Tails' for flip in coin_flips]

print("Coin flips:", coin_flips)
print("Results:", results)
from itertools import product

# sample space of a dice roll
sample_space = list(product(range(1, 7), repeat=1))
# event: rolling an even number
event = [2, 4, 6]
# probability of the event
probability = len(event) / len(sample_space)
print("Sample Space:", sample_space)
print("Event:", event)
print("Probability of rolling an even number:", probability)
# sample space of a coin flip
sample_space_coin = ['Heads', 'Tails']
# event: flipping heads
event_coin = ['Heads']
# probability of the event
probability_coin = len(event_coin) / len(sample_space_coin)
print("Sample Space (Coin):", sample_space_coin)
print("Event (Coin):", event_coin)
print("Probability of flipping heads:", probability_coin)
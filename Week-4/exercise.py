# simulate dice rolls and calculate probabilities
import random
# simulate rolling a die 1000 times
die_rolls = [random.randint(1, 6) for _ in range(1000)]
# count the occurrences of each outcome
outcome_counts = {i: die_rolls.count(i) for i in range(1, 7)}

# probablity of totatl even numbers
even_count = sum(count for i, count in outcome_counts.items() if i % 2 == 0)
probability_even = even_count / len(die_rolls)
# calculate probabilities
probabilities = {i: count / len(die_rolls) for i, count in outcome_counts.items()}
print("Outcome Counts:", outcome_counts)
print("Probabilities:", probabilities)
print("Probability of rolling an even number:", probability_even)

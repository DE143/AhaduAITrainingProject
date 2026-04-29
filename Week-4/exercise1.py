# 1.  in a family of two childs, what is the probablity of two girls given if at least one of them is a girl?
# Sample space of two childs: {BB, BG, GB, GG}
# Event A: Two girls => {GG}
# Event B: At least one girl => {BG, GB, GG}
# P(A|B) = P(A ∩ B) / P(B) = 1/4 / 3/4 = 1/3
# Answer: 1/3
# in a code format:
def probability_two_girls_given_at_least_one_girl():
    # Sample space of two childs
    sample_space = ['BB', 'BG', 'GB', 'GG']
    
    # Event A: Two girls
    event_a = ['GG']
    
    # Event B: At least one girl
    event_b = ['BG', 'GB', 'GG']
    
    # P(A ∩ B)
    intersection = len(set(event_a) & set(event_b))
    
    # P(B)
    probability_b = len(event_b) / len(sample_space)
    
    # P(A|B)
    probability = intersection / len(event_b) if probability_b != 0 else 0
    
    return probability
result = probability_two_girls_given_at_least_one_girl()
print(f"The probability of two girls given at least one girl is: {result}")


# 2. in a basket there are 20 balls, 3 of which are red, 4 blue, 2 oraange and 11 white. what is the probablity of getting the blue balls, then one red ball?
def probability_blue_then_red():
    # Total balls
    total_balls = 20
    
    # Number of blue and red balls
    blue_balls = 4
    red_balls = 3
    
    # Probability of getting a blue ball first
    probability_blue = blue_balls / total_balls
    
    # After taking one blue ball, total balls left
    total_balls_after_blue = total_balls - 1
    
    # Probability of getting a red ball after taking one blue ball
    probability_red_after_blue = red_balls / total_balls_after_blue
    
    # Total probability of getting a blue ball then a red ball
    total_probability = probability_blue * probability_red_after_blue
    
    return total_probability

result2 = probability_blue_then_red()
print(f"The probability of getting a blue ball then a red ball is: {result2}")  


#  3. Ahadu bank ekyc registrs customers in two cities, Addis Ababa 60% of the customers and hawassa city registers 40% of the customers. 2 % of the customer from Addis Ababa are deffective and 1 % of the customer from Hawassa are deffective. If you pick a customer and deffective, what is the probability it come from Addis Ababa?
def probability_defective_from_addis_ababa():
    # Probabilities of customers from each city
    probability_addis_ababa = 0.60
    probability_hawassa = 0.40
    
    # Probabilities of defective customers from each city
    probability_defective_addis_ababa = 0.02
    probability_defective_hawassa = 0.01
    
    # Total probability of picking a defective customer
    total_probability_defective = (probability_addis_ababa * probability_defective_addis_ababa) + (probability_hawassa * probability_defective_hawassa)
    
    # Probability that a defective customer comes from Addis Ababa
    probability_addis_given_defective = (probability_addis_ababa * probability_defective_addis_ababa) / total_probability_defective if total_probability_defective != 0 else 0
    
    return probability_addis_given_defective

result3 = probability_defective_from_addis_ababa()
print(f"The probability that a defective customer comes from Addis Ababa is: {result3}")
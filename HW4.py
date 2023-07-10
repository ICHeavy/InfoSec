import matplotlib.pyplot as plt

def prob_same_birthday(n):
    k = 365  # number of possible birthdays
    p = 1
    for i in range(n):
        p *= (k - i) / k
    return 1 - p

# Calculate probabilities for n=2 to n=70
n_values = range(2, 71)
probabilities = [prob_same_birthday(n) for n in n_values]

# Plot the results
plt.plot(n_values, probabilities)
plt.xlabel('Number of people in the room')
plt.ylabel('Probability of two or more people sharing a birthday')
plt.show()

# Find the value of n where the probability is approximately 0.5
for n, p in zip(n_values, probabilities):
    if abs(p - 0.5) < 0.01:
        print(f"n = {n}, P = {p}")
 


from __future__ import print_function
import random

buzz = ('continuous testing', 'continuous integration',
    'continuous deployment', 'continuous improvement', 'devops')
adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
    'seriously')
# nouns = ('HCMUS', '20HCB1', 'MMTNC')
nouns = ('Ngoc Linh', 'Vu Linh', 'My Loan', 'Ngoc My')

def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
        sample(nouns), buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print(generate_buzz())  
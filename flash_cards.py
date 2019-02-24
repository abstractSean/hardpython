import random

vocab = {'Functional Group': ['Always attached to hydrocarbons',
                              'Group of atoms responsible for ' +
                              'specific reactions or properties'],
         'Organic Compounds': 'Anything that contains carbon',
         'Homologus Series': 'Compounds with the same general ' +
                             'formula and properties',
         'Alkene': 'Unsaturated hydrocarbon', 
         'Alkane': 'Saturated hydrocarbon',
         'Alcohol': 'An alkane with an OH functional group', 
         'Carboxylic Acid': 'An alkane with a COOH functional group',
        }

formulas = {'Ethane': ['C2H6', 'Alkane'], 
            'Ethene': ['C2H4', 'Alkene'],
            'Ethanoic': ['CH3COOH', 'Carboxylic Acid'],
            'Methane': ['CH4', 'Alkane'],
            'Ethanol': ['C2H5OH', 'Alcohol'],
           }


formula_keywords = list(formulas.keys())
formula_values = list(formulas.values())
formulas_only = [formula[0] for formula in formula_values]
formula_categories = list(set(formula[1] for formula in formula_values))

random.shuffle(formula_keywords)
random.shuffle(formula_values)
correct = 0
answerkeys = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}

def check_answer(answer, guess, questions_list, question, correct):

    if answer.lower() == guess.lower():
        correct += 1 
        print('{} is Correct!\n'.format(answer))
        #import pdb; pdb.set_trace()
        questions_list.remove(question)
    else:
        print('Nope!\n')

    return questions_list, correct

def test_formulas():
    
    for keyword in formula_keywords:
        print('What is the formula for {}?'.format(keyword))
        guess = input()
        
        answer = formulas[keyword][0]
       
        if answer.lower() == guess.lower():
            correct += 1
            print('{} is Correct!\n'.format(answer))
            formula_keywords.remove(keyword)
        else:
            print('Nope!\n')

    random.shuffle(formula_keywords)

while correct < len(formulas):
       
    
    for keyword in formula_keywords:
        print('What category is {} in?'.format(keyword))
        prompt = ('A) {}\n' +
                  'B) {}\n' +
                  'C) {}\n' +
                  'D) {}\n' 
                 )
                 
        print(prompt.format(*formula_categories))
        guess = input()

        formula_keywords, correct = check_answer(
                     answer = formulas[keyword][1],
                     guess = formula_categories[answerkeys[guess]],
                     questions_list = formula_keywords,
                     question = keyword,
                     correct = correct,
                    )


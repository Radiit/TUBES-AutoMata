
def transition_tab(transition):
    # < for > 
    transition[('q0', 'f')] = 'q1'
    transition[('q1', 'o')] = 'q2'
    transition[('q2', 'r')] = 'q3'
   
    # < space >
    transition[('q3', ' ')] = 'q4'
    
    # < variable a - z>
    variable = [ chr(i) for i in range(97, 123)]
    for i in variable:
        transition[('q4', i)] = 'q5'
    
    transition[('q5', ' ')] = 'q6'

    # # < range 0 - 9 >
    transition[('q6', 'r')] = 'q7'
    transition[('q7', 'a')] = 'q8'
    transition[('q8', 'n')] = 'q9'
    transition[('q9', 'g')] = 'q10'
    transition[('q10', 'e')] = 'q11'
    transition[('q11', '(')] = 'q12'
    transition[('q12', ' ')] = 'q12'
    # < number 0 - 9 > : range(number , number)
    for i in range(0,10):
        transition[('q12', str(i))] = 'q16'
    
    transition[('q16', ' ')] = 'q16'
    transition[('q16', ',')] = 'q15'
    transition[('q15', ' ')] = 'q15'
    
    for i in range(0,10):
        transition[('q15', str(i))] = 'q16'
    
    transition[('q16', ')')] = 'q17'
    transition[('q17', ':')] = 'ACCEPT'
    
    transition[('q20', '#')] = 'ACCEPT'
    return transition

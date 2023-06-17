
def transition_tab(transition):
    # Syntax for
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

    # in
    transition[('q6', 'i')] = 'q7'
    transition[('q7', 'n')] = 'q8'
    
    # < space >
    transition[('q8', ' ')] = 'q9' # to range
    # transition[('q8', ' ')] = 'q21' # to variable
    
    # # Variable
    # for i in range(97, 123):
    #     transition[('q21', chr(i))] = 'q21'
    # # end char to :
    # transition[('q21', ':')] = 'ACCEPT'
    
    # # < range 0 - 9 >
    transition[('q9', 'r')] = 'q10'
    transition[('q10', 'a')] = 'q11'
    transition[('q11', 'n')] = 'q12'
    transition[('q12', 'g')] = 'q13'
    transition[('q13', 'e')] = 'q14'
    transition[('q14', '(')] = 'q15'
    
    transition[('q15', ' ')] = 'q15'
    # range(number,
    for i in range(0,10):
        transition[('q15', str(i))] = 'q16'
    transition[('q16', ' ')] = 'q16'
    transition[('q16', ')')] = 'q30'
    
    transition[('q16', ',')] = 'q17'
    transition[('q17', ' ')] = 'q17'
    
    # # range(number, number   
    for i in range(0,10):
        transition[('q17', str(i))] = 'q18'
    transition[('q18', ' ')] = 'q18'
    transition[('q18', ',')] = 'q19'
    transition[('q18', ')')] = 'q29'
    
    # # range(number, number, number)
    transition[('q19', ' ')] = 'q19'
    for i in range(0,10):
        transition[('q19', str(i))] = 'q29'
    transition[('q29', ' ')] = 'q29'
    transition[('q29', ')')] = 'q30'
    transition[('q30', ':')] = 'ACCEPT'
     
    return transition

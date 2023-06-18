def transition_tab(transition):
    variable = [ chr(i) for i in range(97, 123)]
    operator = ['+', '-', '*', '/', '%', '=', '<', '>']
    #
    # Syntax for
    # < for > 
    transition[('q0', 'f')] = 'q1'
    transition[('q1', 'o')] = 'q2'
    transition[('q2', 'r')] = 'q3'
   
    # < space >
    transition[('q3', ' ')] = 'q4'
    
    # < variable a - z>
    for i in variable:
        transition[('q4', i)] = 'q5'
    
    transition[('q5', ' ')] = 'q6'

    # in
    transition[('q6', 'i')] = 'q7'
    transition[('q7', 'n')] = 'q8'
    
    # < space >
    transition[('q8', ' ')] = 'q9' # to range
    
    # Variable
    for i in range(97, 123):
        transition[('q9', chr(i))] = 'q30'
        
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
    transition[('q18', ')')] = 'q30'
    
    # # range(number, number, number)
    transition[('q19', ' ')] = 'q19'
    for i in range(0,10):
        transition[('q19', str(i))] = 'q29'
    transition[('q29', ' ')] = 'q29'
    transition[('q29', ')')] = 'q30'
    
    # ACCEPT
    transition[('q30', ':')] = 'q20'
    # transition[('q30', ':')] = 'ACCEPT'
    transition[('q20', ' ')] = 'q20' # loop diri sendiri
    
    for i in variable: # variabel a- z
        transition[('q20', i)] = 'q21'
    
    transition[('q21', ' ')] = 'q21'
    
    transition[('q21', '=')] = 'q23'
    
    transition[('q23', ' ')] = 'q23'
    
    # < variable a - z>
    for i in variable: # a - z
        transition[('q23', i)] = 'q25'
    for i in range(0,10):
        transition[('q23', str(i))] = 'q25'
    transition[('q25', ' ')] = 'q25'
       
    for i in operator:
        if i == '=' or i == '!' or i  == '*' or i == '/':
            transition['q25', str(i)] = 'q29'
            for i in operator :
                transition['q29', ' '] = 'q27'
                transition['q29', str(i)] = 'q27'

        elif i == '<' or i == '>':
            transition['q25', '<'] = 'q27'
            transition['q25', '>'] = 'q27'
            transition['q27', '='] = 'q27'
        else:
            transition['q25', str(i)] = 'q27'
    
    transition[('q27', ' ')] = 'q27'
    for i in variable: # a - z
        transition[('q27', i)] = 'ACCEPT'
    for i in range(0,10):
        transition[('q27', str(i))] = 'ACCEPT'
    return transition
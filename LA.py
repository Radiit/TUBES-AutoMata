import tables.transition as transition
from collections import defaultdict
def analyze(input_string):
    # Inisialisasi State 
    state_list = []; list(state_list.append(f'q{i}') for i in range(30+1))
    # Inisilisasi Nilai Awal
    transition_table = defaultdict(lambda: "ERROR", {})
     
    transition_table = transition.transition_tab(transition_table)
    
    idx = 0
    state = 'q0'
    current_token = ''
    
    while state != 'ACCEPT':
        current_char = input_string[idx]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == "q99":
            current_token = ''
        elif state == "ERROR":
            print("ERROR : Lexical Error")
            break
        print(state, current_token)
        idx += 1
    return state == "ACCEPT"
     
    
def main():
    input_string = """for a range(1,1):"""
    print(analyze(input_string))

main()
    
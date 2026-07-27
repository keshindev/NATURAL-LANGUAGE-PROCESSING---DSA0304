# DFA for strings ending with "ab"

transitions = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

start_state = 'q0'
final_states = ['q2']

string = input("Enter String: ")

state = start_state
path = [state]

valid = True

for ch in string:
    if ch not in ['a', 'b']:
        valid = False
        break
    state = transitions[state][ch]
    path.append(state)

if valid:
    print("Transition Path:")
    print(" -> ".join(path))

    if state in final_states:
        print("Accepted")
    else:
        print("Rejected")
else:
    print("Invalid Input")

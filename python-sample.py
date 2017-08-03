def wombat(state, time_left):
    turnLeft = {'action': 'turn', 'metadata': { 'direction': 'left'} }
    turnRight = {'action': 'turn', 'metadata': { 'direction': 'right'} } 
    shoot = {'action': 'shoot', 'metadata': { } }
    move = {'action': 'move', 'metadata': { } }
    #turnLeft = {'action': 'turn', 'metadata': { 'direction': 'left'} }
    
    command = turnLeft
    
    
    # Note that the function name MUST be wombat
    return {
        'command': command,
        'state': {
            'hello': 'world'
        }
    }

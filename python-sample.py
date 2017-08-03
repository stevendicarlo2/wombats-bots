def wombat(state, time_left):
    turnLeft = {'action': 'turn', 'metadata': { 'direction': 'left'} }
    turnRight = {'action': 'turn', 'metadata': { 'direction': 'right'} } 
    shoot = {'action': 'shoot', 'metadata': { } }
    move = {'action': 'move', 'metadata': { } }
    direction = state['arena'][3][3]['contents']['orientation']
    
    
    def itemAt(x, y):
        return state['arena'][y][x]['contents']['type']
    
    def itemInFront():
        if direction == 'w':
            return itemAt(2, 3)
        if direction == 'n':
            return itemAt(3, 2)
        if direction == 'e':
            return itemAt(4, 3)
        if direction == 's':
            return itemAt(3, 4)
        
    def atEdge():
        x = state['global-coords']
    
    def facingEdgeOfScreen():
        width = state['global-dimensions'][0] - 1
        height = state['global-dimensions'][1] - 1
        if direction == 'w':
            return state['global-coords'][0] == 0
        if direction == 'n':
            return state['global-coords'][1] == 0
        if direction == 'e':
            return state['global-coords'][0] == width
        if direction == 's':
            return state['global-coords'][1] == height        
    
    if itemInFront() in ['wombat', 'zakano', 'wood-barrier']:
        command = shoot
    elif itemInFront() in ['steel-barrier', 'poison', 'shot', 'fog']:
        command = turnLeft
    elif facingEdgeOfScreen():
        command = turnLeft
    elif itemInFront() in ['food', 'open']:
        command = move
    else:
        command = shoot
    
    
    
    # Note that the function name MUST be wombat
    return {
        'command': command,
        'state': state
    }

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
    def itemsInFront():
        if direction == 'w':
            return [itemAt(2, 3), itemAt(1, 3), itemAt(0, 3)]
        if direction == 'n':
            return [itemAt(3, 2), itemAt(3, 1), itemAt(3, 0)]
        if direction == 'e':
            return [itemAt(4, 3), itemAt(5, 3), itemAt(6, 3)]
        if direction == 's':
            return [itemAt(3, 4), itemAt(3, 5), itemAt(3, 6)]
        
    def shouldShoot():
        return 'wombat' in itemsInFront() or 'zakano' in itemsInFront()

    
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
    
    if shouldShoot():
        command = shoot
    elif itemInFront() in ['wombat', 'zakano', 'wood-barrier']:
        command = shoot
    elif itemInFront() in ['steel-barrier', 'poison', 'shot']:
        command = turnLeft
    elif facingEdgeOfScreen():
        command = turnLeft
    elif itemInFront() in ['food', 'open', 'fog']:
        command = move
    else:
        command = shoot
    
    
    
    # Note that the function name MUST be wombat
    return {
        'command': command,
        'state': state
    }

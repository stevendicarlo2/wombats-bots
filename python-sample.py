def wombat(state, time_left):
    turnLeft = {'action': 'turn', 'metadata': { 'direction': 'left'} }
    turnRight = {'action': 'turn', 'metadata': { 'direction': 'right'} } 
    shoot = {'action': 'shoot', 'metadata': { } }
    move = {'action': 'move', 'metadata': { } }
    direction = state['arena'][3][3]['orientation']
    
    
    def itemAt(x, y):
        return state['arena'][y][x]
    
    def itemInFront():
        if direction == w:
            return itemAt(2, 3)
        if direction == n:
            return itemAt(3, 2)
        if direction == e:
            return itemAt(4, 3)
        if direction == s:
            return itemAt(3, 4)
    
    if itemInFront in ['wombat', 'zakano', 'wood-barrier']:
        command = shoot
    if itemInFront in ['steel-barrier', 'poison', 'shot', 'fog']:
        command = turnLeft
    if itemInFront in ['food', 'open']:
        command = move
    
    
    
    
    # Note that the function name MUST be wombat
    return {
        'command': command,
        'state': state
    }

class Position:
    def __init__(self,x,y,traversable = True):
        self.x = x
        self.y = y
        self.traversable = traversable

    def __repr__(self):
        return f"Position = (x = {x.self},y = {y.self}) , traversable = {self.traversable}"
    
class Map:
    def __init__(self,width,height):
        self.grid = [[Position(x,y) for y in range(height)] for x in range(width)]
        self.width = width
        self.height = height

    def obstacle(self,x,y):
        if 0<=x<self.width and 0<=y<self.height:
            self.grid[x][y].traversable = False
    
    def valid(self,x,y):
        return 0<=x<self.width and 0<=y<self.height and self.rid[x][y].traversable
    
    def pos(self,x,y):
        return self.grid[x][y]
    
class Rover:
    def __init__(self, start_pos):
        self.battery = 100
        self.current_pos = start_pos

    def traverse(self,target,map):
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = [[False for _ in range(map.height)] for _ in range(map.width)]
        queue = []
        start = self.current_pos
        queue.append((start.x,start.y,0))
        visited[start.x][start.y] = True

        while queue:
            x,y,steps = queue.pop(0)

            if x == target.x and y == target.y:
                if steps <= self.battery:
                    self.battery = self.battery - steps
                    self.current_pos = map.pos(x,y)
                    return steps
                else:
                    return -1
                
            for dx,dy in direction:
                nx,ny = x+dx,y+dy
                if map.valid(nx,ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,steps+1))

        return -1
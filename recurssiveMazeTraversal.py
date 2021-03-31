from pprint import pprint 
import maze_helper as mh


def walked(explored,maze,path):
    for i in range(1,len(explored)):
        mh.add_walk_symbol(maze,explored[i])
    mh.add_walk_symbol(maze,path)
    mh.print_maze(maze)


def dfs(maze, position, explored = []):
    explored.append(position)
    paths = mh.get_adjacent_positions(maze,position)
    for path in paths:
        if path not in explored:
            if mh.symbol_at(maze,path) == "X":
                # print('sucess')
                walked(explored,maze,path)
            else:
                dfs(maze,path,explored)
    explored.pop()


#everything below here is for testing. Also please note that the origional sample maze function was not copy and pasted over, it was imported as seen in the below  line of code
#I copied the algorithm and adjusted the strings for different test cases. 

maze1 = mh.sample_maze()

def my_sample_maze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])
    return maze

def my_sample_maze3():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", "X", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])
    return maze

def my_sample_maze4():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])
    return maze

maze2 = my_sample_maze2()
startingpos = (5,0)

maze3 = my_sample_maze3()
maze4 = my_sample_maze4()



def main():
    dfs(maze4,startingpos, explored=[])
    dfs(maze1,startingpos, explored=[])
    dfs(maze3,startingpos, explored=[])
    dfs(maze2,startingpos, explored=[])

if __name__ == '__main__':
    main()
    
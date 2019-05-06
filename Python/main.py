from mars_rover import Execution

def main():
    filename = 'sample_input/sampleinput.txt'    
    f = open(filename,'r')
    content = f.read().splitlines()
    
    #parse first line
    p_x = int(content[0][0])
    p_y = int(content[0][2])
    del content[0]
    
    #parse remaining file relating to rovers
    rover_content = {}
    for i in range(int(len(content)/2)):
        rover_content[i] = {'start':content[i*2], 'path':content[(i*2)+1]}
        
    print(Execution.extractInstructions(p_x, p_y, rover_content))
    


if __name__ == "__main__":
    main()

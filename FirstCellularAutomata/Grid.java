public class Grid{
    private int width;
    private int height; 
    private Cell[][] cells;
    
    public Grid(int width, int height){
        this. width = width;
        this.height = height;
        this.cells = new Cell[width][height];
        initializeGrid();
    }
    
    private void initializeGrid(){
        
        for (int i = 0; i< width; i++){
            for (int j = 0; j< height; j++){
                cells[i][j] = new Cell();
                
                
            }
        }
    }
    public void update(){
        Cell[][] nextGen = new Cell[width][height];
        
        //applying rules
        for (int x = 0; x < width; x++){
            for (int y = 0; y < height; y++){
                int liveNeighbors = countLiveNeighbors(x,y);
                int currentState = cells[x][y].getState();
                
                
                if (currentState == 1) {
                    if (liveNeighbors < 2 || liveNeighbors > 3){
                        nextGen[x][y] = new Cell(); //cell dies
                        
                    }else{
                        nextGen[x][y] = new Cell();
                        nextGen[x][y].setState(1); //cell Lives!
                    }
                }else{
                    //dead cells have a chance to come to life due to reporduction
                    if (liveNeighbors == 3){
                        nextGen[x][y] = new Cell();
                        nextGen[x][y].setState(1);
                    }else{
                        nextGen[x][y] = new Cell(); //cell remains dead if less than 3 neighbors or too many 
                    }
            }
        }
      
    }
      cells = nextGen;
    }
    
        
    private int countLiveNeighbors(int x, int y){
        int liveNeighbors = 0;
        int[][] neighbors = {
            {-1,-1},{-1,0} ,{-1,1},
            {0, -1},       {0, 1},
            {1, -1},{1,0},{1, 1} 
        };
        
        for(int[] neighbor : neighbors){
            //nx = neighbor x coord
            //nx = neighbor y coord
            int nx = x+neighbor[0];
            int ny = y+ neighbor[1];
            //check neighbors are within grid and alive, if so, increment amount of live neighbors
            if(nx >= 0 && nx < width && ny >= 0&& ny < height && cells[nx][ny].getState() == 1){
                liveNeighbors ++;
            }
        }
        return liveNeighbors;
        
    }
   
    public void display(){
        System.out.print("\033[H\033[2J");
        System.out.flush();
        
        
        //display the grid on console
        for (int  y = 0; y< height; y ++){
            for (int x = 0; x < width; x++){
                System.out.print(cells[x][y].getState() == 1 ? "X" : ".");
            }
            System.out.println();
        }
    
}
public void setCellState(int x, int y, int state){
    if (x >= 0 && x < width && y >= 0 && y < height){
        cells[x][y].setState(state);
    }
}

public void toggleCellState(int x, int y){
    if (x >= 0 && x < width && y >= 0 && y < height){
        cells[x][y].setState(cells[x][y].getState() == 1 ?0:1);
    
    
    }
}

public void runGenerations(int numGenerations){
    for (int i = 0; i < numGenerations; i++){
        update();
        display();
        try{
            Thread.sleep(500); //adjustable delay between generations
        } catch (InterruptedException e){
            e.printStackTrace();
            
            
        }
    }
    
}
}
import java.util.Scanner;


public class FirstCellularAutomationApp {
    public static void main(String[] args){
    System.out.println("Welcome to Cellular Automation!");
    
    
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter the size of the grid! (width height) seperated by a space");
    int width = scanner.nextInt();
    int height = scanner.nextInt();
    
    
    Grid grid = new Grid(width,height);
 
    grid.display();
    
    setInitialState(grid);
    
    grid.display();
    
    
    
 while (true){
   
        //update automatically x generations
        System.out.println("Enter the number of generations to run:");
        
        int numGenerations = scanner.nextInt();
        System.out.println("Enter the delay between generations (around 500 recommended, measured in milliseconds):");
        int delay = scanner.nextInt();
        runAutomatically(grid, numGenerations, delay);
        setNextState(grid);
        
        
    
    
    }
    }
        private static void updateManually(Grid grid){
            Scanner scanner = new Scanner(System.in);
            System.out.println("Manually update the grid:");
            System.out.println("Enter coordingated (x y) of the cell to toggle its state (type 'done' to finish)");
        while (true){
            String input = scanner.nextLine();
            if (input.equals("done")){
                break;
            }
            try{
            String[] coordinates = input.split(" ");
            int x = Integer.parseInt(coordinates[0]);
            int y = Integer.parseInt(coordinates[1]);
            grid.toggleCellState(x,y);
            grid.display();
            } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
            System.out.println("Invalid input. Please enter coordinates in the format 'x y'.");
        }
            
        }
        scanner.close();
        }
        private static void runAutomatically(Grid grid, int numGenerations, int delay){
            System.out.println("Running generations automatically...");
            for (int i = 0; i < numGenerations; i++){
                grid.update();
                grid.display();
                try{
                    Thread.sleep(delay);
                }catch (InterruptedException e){
                    e.printStackTrace();
                }
                
            }
            
        }
    private static void setInitialState (Grid grid){
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("Set initial state of the grid:");
        System.out.println("Enter Coordinates (x y) of live cells seperated by space. Type 'done' to finish");
        while (true){
            
            String input = scanner.nextLine();
        if (input.equals("done")|| input.equals ("")){
                break;
            }
            String[] coordinates = input.split(" ");
            int x = Integer.parseInt(coordinates[0]);
            int y = Integer.parseInt(coordinates[1]);
            grid.setCellState(x,y,1);
            
            
        }
    
/**


//ENTER THESE VALUES TO ACHIEVE A 'PULSAR' PATTERN
2 5
2 6
2 7
2 11
2 12
2 13
4 3
5 3
6 3
4 8
5 8
6 8
4 10
5 10
6 10
4 15
5 15
6 15
7 5
7 6
7 7
7 11
7 12
7 13
9 5
9 6
9 7
9 11
9 12
9 13
10 8
11 8
12 8
10 10
11 10
12 10
10 15
11 15
12 15
10 3
11 3
12 3
14 5
14 6
14 7
14 11
14 12
14 13



   **/     
    }
        private static void setNextState (Grid grid){
        
        Scanner scanner = new Scanner(System.in);
        
        while (true){
            System.out.println("Set next state of the grid:");
        System.out.println("Enter Coordinates (x y) of live cells seperated by space. Type 'done' to finish");
            String input = scanner.nextLine();
        if (input.equals("done")|| input.equals ("")){
                break;
            }
            String[] coordinates = input.split(" ");
            int x = Integer.parseInt(coordinates[0]);
            int y = Integer.parseInt(coordinates[1]);
            grid.toggleCellState(x,y);
            grid.display();
            
            
        }
    }
    
}


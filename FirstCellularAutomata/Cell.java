public class Cell{
    private int state;
    public Cell() {
        this.state = 0; //state default = dead
    }
    public int getState(){
        return state;
    }
    public void setState(int state){
        this.state = state;
    }
}
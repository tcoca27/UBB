package LexicalAnalizor;

public class Pair<T1, T2> {

    private T1 v1;
    private T2 v2;

    public Pair() { }

    public Pair(T1 v1, T2 v2) {
        this.v1 = v1;
        this.v2 = v2;
    }

    public String toString(){
        return "(" + this.v1 + ", " + this.v2 + ")";
    }
}

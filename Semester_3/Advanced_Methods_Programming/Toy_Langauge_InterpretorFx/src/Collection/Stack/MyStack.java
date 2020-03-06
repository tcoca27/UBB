package Collection.Stack;


import java.util.Stack;

public class MyStack<T> implements MyIStack<T>{
    private Stack<T> stack;

    public MyStack(){
        stack=new Stack<T>();
    }

    public T pop(){
        return stack.pop();
    }

    public void push(T v){
        stack.push(v);
    }

    public Stack<T> getAll(){return stack;}

    public boolean isEmpty(){
        return stack.empty();
    }

    public String toString(){
        return stack.toString();
    }
}

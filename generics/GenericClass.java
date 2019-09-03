public class GenricClass <T> {

    List<T> list;
    int capacity;

    public void GenericClass(int x){
        this.capacity = x;
        list = new LinkedList<T>();
    }

    public void add(T obj){
        list.add(obj);
    }

    public T get(){
        if(list.size() > 0) return 
    }

}
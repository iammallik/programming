import java.util.Random;
import java.util.*;

public class PrintOddEven{

	public static void main(String[] args) throws InterruptedException{
		System.out.println("main Thread_id: "+Thread.currentThread().getId());

		Random ra = new Random();
		Val v = new Val();
		Thread odd = new Thread(new PrintOdd(v, ra));
		Thread even = new Thread(new PrintEven(v, ra));
		odd.start();
		even.start();

		while(true){
			if(v.val > 9){
				System.out.println("val is "+v.val);
				return;
			}
			try {
				Thread.sleep(ra.nextInt(5000));
			} catch (InterruptedException e) {
			}
		}
	}

	public void p(int i){
		System.out.print(i+" ");
	}

	public void p(String i){
		System.out.println(i+" ");
	}
	
}

class Val{

	int val = 0;
	Val(){}

	public void inc(boolean x) {
		if(val > 9) return;
		if(x){
			// print even
			if (val % 2 == 0){
				val += 1;
				System.out.println(val);
				System.out.println("Thread_id: "+Thread.currentThread().getId());
			}
		}else{
			if (val % 2 == 1){
				val += 1;
				System.out.println(val);
				System.out.println("Thread_id: "+Thread.currentThread().getId());
			}
		}
	}
}

class PrintEven implements Runnable{
	Val val;
	Random r;
	PrintEven(Val v, Random ra){
		this.val = v;
		this.r = ra;
	}
	public void run(){
		System.out.println("Even Thread_id: "+Thread.currentThread().getId());
		while(true){
			val.inc(true);
			if(val.val > 9) return;
			try {
				Thread.sleep(r.nextInt(5000));
			} catch (InterruptedException e)  {}
		}
	}
}

class PrintOdd implements Runnable{
	Val val;
	Random r;
	PrintOdd(Val v, Random ra){
		this.val = v;
		this.r = ra;
	}
	public void run(){
		System.out.println("Odd Thread_id: "+Thread.currentThread().getId());
		while(true){
			val.inc(false);
			if(val.val > 9) return;
			try {
				Thread.sleep(r.nextInt(5000));
			} catch (InterruptedException e) {}
		}
	}
}
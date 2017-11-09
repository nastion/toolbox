package main;

import java.math.BigInteger;

public class Fibonacci {
	public static void main(String[] args) {
		System.out.println(fib(32));
		System.out.println(fib(42));
		System.out.println(fib(100));
		
		System.out.println(fib(1000));
	}
	
	public static String fib(int n) {
		BigInteger[] fibonacci = new BigInteger[n];
		fibonacci[0] = new BigInteger("0");
		fibonacci[1] = new BigInteger("1");
		for (int i = 2; i < n; i++) {
			if (i != n) {
				fibonacci[i] = new BigInteger("0");
				fibonacci[i].add(fibonacci[i-1]);
				fibonacci[i].add(fibonacci[i-2]);
			}
		}
		
		BigInteger returnVal = new BigInteger("0");
		returnVal.add(fibonacci[n-1]);
		returnVal.add(fibonacci[n-2]);
		return returnVal.toString();
	}
}

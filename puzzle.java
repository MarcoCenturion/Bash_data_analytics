Puzzle.java

import java.math.BigInteger;

class Puzzle {

final static BigInteger M = new BigInteger("2021");

private static BigInteger compute(long n) {

String s = "";

for (long i = 0; i < n; i++) {

s = s + n;

}

return new BigInteger(s.toString()).mod(M);

}

public static void main(String args[]) {

for (long n : new long[] { 1L, 2L, 5L, 10L, 20L, 67489454811002199L }) {

System.out.println("" + n + ": " + compute(n));

}

}

}

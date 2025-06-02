class Solution {
    public int getSum(int a, int b) {
        // b is the carry
        while (b != 0){
            int temp = (a & b) << 1;
            // XOR and AND is equivalent to addition
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}

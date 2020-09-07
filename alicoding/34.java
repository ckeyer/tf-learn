package solution34;

class Solution {
    private int idx = 0;
    private int[] countArr;
    public int solution(int[][] m) {
        this.countArr = new int[m.length*m[0].length*2];
        this.subSolu(m, 0, 0, m[0][0]);
        int min = this.countArr[0];
        for (int i=1;i<this.countArr.length;i++) {
            if (min > this.countArr[i] && this.countArr[i] > 0) {
                min = this.countArr[i];
            }
        }
        return min;
    }

    public void subSolu(int[][] m, int i,int j,int count ){ 
        boolean isDown = false, isRight = false ;
        if (i>=m.length-1){
            isDown = true;
        }
        if (j>=m[0].length-1){
            isRight = true;
        }
        if (isDown && isRight) {
            this.countArr[this.idx] = count;
            this.idx++;
        }
        if (!isDown ) {
		    this.subSolu(m, i+1, j, count + m[i+1][j]);
        }
        if (!isRight) {
		    this.subSolu(m, i, j+1, count + m[i][j+1]);
        }
    }
}

System.out.println("hei");

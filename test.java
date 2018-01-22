public class test {
    public static void main(String[] args) {
        String x;
        x = "Manipal Police Station;SH 25A, Madhav Nagar, Eshwar Nagar, Manipal, Karnataka 576104, India;0820 257 0328";
        String [] words = x.split(";");
        for(String w:words)
        	System.out.println(w);
    }
    
}
import java.security.SecureRandom;

public class RandomBinary {
    public static void main(String[] args) {
        SecureRandom random = new SecureRandom();
        StringBuilder binary = new StringBuilder();
        
        for (int i = 0; i < 128; i++) {
            binary.append(random.nextBoolean() ? '1' : '0');
        }
        
        System.out.println(binary.toString());
    }
}
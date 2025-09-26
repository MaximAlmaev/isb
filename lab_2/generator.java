import java.security.SecureRandom;

public class RandomBinary {
    /**
     * Generates a 128-bit random binary sequence
     *
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        SecureRandom random = new SecureRandom();
        StringBuilder binary = new StringBuilder();
        
        for (int i = 0; i < 128; i++) {
            binary.append(random.nextBoolean() ? '1' : '0');
        }
        
        System.out.println(binary.toString());
    }
}
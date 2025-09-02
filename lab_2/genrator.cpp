#include <iostream>
#include <random>

int main() {
    std::random_device rd;
    std::mt19937_64 gen(rd());
    std::uniform_int_distribution<int> dist(0, 1);
    
    for (int i = 0; i < 128; i++) {
        std::cout << dist(gen);
    }
    
    return 0;
}
#include <iostream>
#include <iomanip> // Para usar std::setprecision

int main() {
  
  int numA = 2;
  float numB = 2.5;
  double numC = 3;
  char carD = 'C';
  
  std::cout << "A: " << numA << " || B: " << numB << " || C: " << numC << " || D: " << carD << std::endl;
  
  std::cout << "A: " << numA << " || B: " << numB << " || C: " << std::fixed 
  << std::setprecision(3) << numC << " || D: " << static_cast<int>(carD) << carD << std::endl;
}


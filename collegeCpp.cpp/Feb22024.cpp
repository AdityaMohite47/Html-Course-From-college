#include <iostream>

int main()
{
    int x , y ;
    std::cout << "Enter the number for it's table" << std::endl;
    std::cin >> x >> y;

    for (size_t i = 1; i <= 10; i++)
    
    {
        std::cout << x << " x " << i << " = " << x * i << std::endl;
    }

    // size_t i = 1;
    //  do
    //  {
    //     std::cout << 2 << " x " << i  << " = " << 2*i << std::endl ;
    //     i++;
    //  } while (i <= 10 );

    // size_t i = 1;
    //  while (i <= 10)
    //  {
    //    std::cout << 2 << " x " << i  << " = " << 2*i << std::endl ;
    //     i++;
    //  }
}

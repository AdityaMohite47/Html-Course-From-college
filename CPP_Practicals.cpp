#include <iostream>

int main()
{
    // int MarksofSubjects[5], sum = 0;

    // for (size_t i = 0; i < 5; i++)
    // {
    //     std::cout << "Enter Marks for Subject " << i + 1 << std::endl;
    //     std::cin >> MarksofSubjects[i];
    //     sum += MarksofSubjects[i];
    // }
    // float percentage = (float(sum) / 500.0f) * 100.0f;

    // if (percentage >= 60.0f)
    //     std::cout << "Student Passed the Class with " << percentage << "%" << std::endl;
    // else
    //     std::cout << "Student Failed the Class with " << percentage << "%" << std::endl;

    // return 0;

    int Matrix[3][3];

    std::cout << "Enter the values for your 3X3 Matrix" << std::endl;

    for (size_t i = 0; i < 3; i++)
    {
        for (size_t j = 0; j < 3; j++)
        {
            std::cin >> Matrix[i][j];
        }
    }

     std::cout << std::endl << "Printing Matrix :" << std::endl ;

     for (size_t i = 0; i < 3; i++)
    {
        for (size_t j = 0; j < 3; j++)
        {
            std::cout << Matrix[i][j]  << "  ";
        }
         std::cout << std::endl << std::endl;
    }
}

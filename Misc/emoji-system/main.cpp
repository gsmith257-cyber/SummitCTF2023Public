
#include <locale.h>
#include <string>
#include <iostream>
#include <map>
#include <vector>
#include <signal.h>
#include <unistd.h>

#define MAX 100
#define MIN -100

/* Create an array of emoji characters */
const char *emoji[] =
{
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "😘", "😗", "😙", "😚", "😋", "😜", "😝", "🤑", "🤗", "🤓", "😎", "🤡", "🤠", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "😤", "😠", "😡", "😶", "😐", "😑", "😯", "😦", "😧", "😮", "😲", "😵", "😳", "😱", "😨", "😰", "😢", "😥", "🤤", "😭", "😓", "😪", "😴", "🙄", "🤔", "🤥", "😬", "🤐", "🤢", "🤧", "😷", "🤒", "🤕", "😈", "👿", "👹", "👺", "💩", "👻", "💀", "☠️", "👽", "👾", "🤖", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾", "🙈", "🙉", "🙊", "💋", "💌", "💘", "💝", "💖", "💗", "💓", "💞", "💕", "💟", "❣️", "💔", "❤️", "🧡", "💛"
};

class Equation
{
    private:
        int result;
        int coefficientA;
        int coefficientB;
        int coefficientC;
        std::pair<int, int> variableA;
        std::pair<int, int> variableB;
        std::pair<int, int> variableC;
    public:
        Equation(std::pair<int, int> variableA, std::pair<int, int> variableB, std::pair<int, int> variableC)
        {
            /* Generate a random number using MIN and MAX */
            this->coefficientA = rand() % (MAX - MIN + 1) + MIN;
            this->coefficientB = rand() % (MAX - MIN + 1) + MIN;
            this->coefficientC = rand() % (MAX - MIN + 1) + MIN;

            /* Set variableA, variableB, and variableC */
            this->variableA = variableA;
            this->variableB = variableB;
            this->variableC = variableC;

            /* Calculate the result */
            result = coefficientA * variableA.second + coefficientB * variableB.second + coefficientC * variableC.second;
        }

        friend std::ostream& operator<<(std::ostream& o, Equation const & f){
            o << "(" << f.coefficientA << " * " << emoji[f.variableA.first] << ")" <<
                " + " << "(" << f.coefficientB << " * " << emoji[f.variableB.first] << ")" <<
                " + " << "(" << f.coefficientC << " * " << emoji[f.variableC.first] << ")" <<
                " = " << f.result;
            return o;
        }
};


int main(int argc, char ** argv)
{
    /* Terminate the program after three seconds */
    alarm(3);

    /* Create signal handler for SIGALRM */
    signal(SIGALRM, [](int sig)
    {
        std::cout << "Time's up!" << std::endl;
        exit(0);
    });

    /* Set the terminal to print unicode characters. */
    setlocale(LC_ALL, "");

    /* Seed the random number generator. */
    srand(time(NULL));

    /* Create a map of emoji characters to what number the variable represents */
    std::map<int, int> emoji_map;

    /* Choose three variables to be used in our system of equations */
    while (emoji_map.size() < 3)
    {
        int random_number = rand() % (sizeof(emoji) / sizeof(emoji[0]));
        if (emoji_map.find(random_number) == emoji_map.end())
        {
            /* Generate a new random number between -100 and 100 */
            int random_number_2 = rand() % (MAX - MIN + 1) + MIN;
            emoji_map[random_number] = random_number_2;
        }
    }

    /* Convert the map to a list of pairs */
    std::vector<std::pair<int, int> > emoji_list;
    for (std::pair<int, int> x : emoji_map)
    {
        emoji_list.push_back(x);
    }

    /* Print the prompt */
    std::cout << emoji[0] <<  " Solve the following systems of equations in the next three seconds " << emoji[0] << std::endl;

    Equation eqA = Equation(emoji_list[0], emoji_list[1], emoji_list[2]);
    Equation eqB = Equation(emoji_list[0], emoji_list[1], emoji_list[2]);
    Equation eqC = Equation(emoji_list[0], emoji_list[1], emoji_list[2]);

    std::cout << eqA << std::endl;
    std::cout << eqB << std::endl;
    std::cout << eqC << std::endl;

    std::cout << std::endl;

    /* Read three integers from the user */
    int userInput1;
    int userInput2;
    int userInput3;
    
    std::cout << "Enter your first answer for " << emoji[emoji_list[0].first] << ": ";
    std::cin >> userInput1;

    std::cout << "Enter your second answer for " << emoji[emoji_list[1].first] << ": ";
    std::cin >> userInput2;

    std::cout << "Enter your third answer for " << emoji[emoji_list[2].first] << ": ";
    std::cin >> userInput3;

    if (userInput1 == emoji_list[0].second && userInput2 == emoji_list[1].second && userInput3 == emoji_list[2].second)
    {
        /* Print out the flag file! */
        system("cat /src/flag.txt");
    }
    else
    {
        std::cout << "Oops! That's incorrect." << std::endl;
    }

    return 0;
}
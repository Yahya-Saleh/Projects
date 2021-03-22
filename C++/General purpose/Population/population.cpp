#include <iostream>
#include <string>
using namespace std;

class population
{
    int size, births, deaths;

public:
    population(int _size, int _births, int _deaths)
    {
        try
        {
            if (_size < 1)
            {
                throw "population size less than 1";
            }
            else if (_births < 0 || _deaths < 0)
            {
                throw "births and deaths must be at least 0";
            }

            size = _size;
            births = _births;
            deaths = _deaths;
        }
        catch (string error)
        {
            cout << error << endl;
        }
    }

    int get_population_size()
    {
        return size;
    }

    int get_births()
    {
        return births;
    }
    double get_birth_rate()
    {
        return (double)births / size;
    }

    int get_deaths()
    {
        return deaths;
    }
    double get_death_rate()
    {
        return (double)deaths / size;
    }
};

int main()
{
    population pop = population(500000, 5000, 1000);

    cout << "Population size: " << pop.get_population_size() << endl;
    cout << "Births: " << pop.get_births() << endl;
    cout << "Birth rate: %" << pop.get_birth_rate() * 100 << endl;
    cout << "Deaths: " << pop.get_deaths() << endl;
    cout << "Death rate: %" << pop.get_death_rate() * 100 << endl;

    population test = population(0, 5000, 1000);
    population test2 = population(1, -1, 1000);
    population test3 = population(2, 5000, -2);
}

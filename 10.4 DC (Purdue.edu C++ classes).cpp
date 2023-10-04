#include <iostream>
using namespace std;

class ZooAnimal 
{
private:
    const char* name;
    int cageNumber;
    int weightDate;
    int weight;
public:
    void Create(const char* a, int x, int y, int z);
    void Destroy(); // destroy function
    const char* reptName();
    int daysSinceLastWeighed(int today);
};

void ZooAnimal::Destroy() {}

// -------- member function to return the animal's name
const char* ZooAnimal::reptName()
{
    return name;
}

// -------- member function to return the number of days
// -------- since the animal was last weighed

void ZooAnimal::Create(const char* a, int x, int y, int z) 
{
    name = a;
    cageNumber = x;
    weightDate = y;
    weight = z;
}

int ZooAnimal::daysSinceLastWeighed(int today) 
{
    int startday, thisday;
    thisday = today / 100 * 30 + today - today / 100 * 100;
    startday = weightDate / 100 * 30 + weightDate - weightDate / 100 * 100;
    if (thisday < startday)
        thisday += 360;
    return (thisday - startday);
}

int main() 
{
    ZooAnimal bozo;
    bozo.Create("Bozo", 408, 1027, 400);

    cout << "This animal's name is " << bozo.reptName() << endl;

    bozo.Destroy();
}

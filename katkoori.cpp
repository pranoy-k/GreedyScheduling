#include <pair>
#include <ifstream>
#include <vector>

int main()
{
    ifstream fin("jobs1.txt");

    int cnt;
    fin >> cnt;

    vector<pair<pair<int, int>, int> > v;

    while (cnt--) {
        int a, b;
        fin >> a >> b;

        pair<int, int> p = pair(a-b, );
    }

    return 0;
}


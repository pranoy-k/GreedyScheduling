#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream fin("names.txt");

    int cnt;
    fin >> cnt;

    vector<pair<pair<int, int>, int> > v;

    while (cnt--) {
        int a, b;
        fin >> a >> b;

        pair<int, int> _p = make_pair(a-b, a);
        pair<pair<int, int>, int> p = make_pair(_p, b);

        v.push_back(p);
    }

    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
//
//    for (int i = 0; i < v.size(); i++) {
//        cout << v[i].first.first << " " << v[i].first.second << " " << v[i].second << "\n";
//    }

    long long sum = 0, len = 0;
    for (int i = 0; i < v.size(); i++) {
        len += v[i].second;
        sum += len * v[i].first.second;
    }

    cout << sum;

    return 0;
}

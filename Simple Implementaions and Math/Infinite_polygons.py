"""
https://www.codechef.com/ICM2021B/problems/ICM0003
"""

import math
def solve():
        n=int(input())
        pi=math.pi
        a=(n-2)*180/n
        a1=n*math.sin(a*pi/180)/8
        ratio=n/(4*math.tan(pi/n))
        s=(ratio-a1)/ratio
        print(1/(1-s))

for _ in range(int(input())):
    solve()
"""
     double n;
    cin >> n;
    double pi = 2 * acos(0.0);
    double angle = (n - 2) * 180 / (n);

    double area = n * sin(angle * pi / 180) / 8;
    double Area = n / (4 * tan(pi / n));

    db(Area, area);

    double r = (Area - area) / Area;
    db(r);
    double ans = 1 / (1 - r);
    cout << setprecision(10) << fixed << ans << "\n";
    """
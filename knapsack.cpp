#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, budget;
    cin >> n;

    vector<int> cost(n), profit(n);
    for(int i = 0; i < n; i++) cin >> cost[i];
    for(int i = 0; i < n; i++) cin >> profit[i];
    cin >> budget;

    vector<vector<int>> dp(n+1, vector<int>(budget+1, 0));

    for(int i = 1; i <= n; i++) {
        for(int w = 0; w <= budget; w++) {
            if(cost[i-1] <= w)
                dp[i][w] = max(dp[i-1][w], profit[i-1] + dp[i-1][w - cost[i-1]]);
            else
                dp[i][w] = dp[i-1][w];
        }
    }

    cout << dp[n][budget] << endl;

    int w = budget;
    for(int i = n; i > 0 && w > 0; i--) {
        if(dp[i][w] != dp[i-1][w]) {
            cout << i-1 << " ";
            w -= cost[i-1];
        }
    }

    return 0;
}
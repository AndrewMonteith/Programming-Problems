// Solution to https://leetcode.com/problems/maximum-length-of-pair-chain/

namespace {

using Pair = std::vector<int>; // not typesafe but oh well

static int findLongestChain(std::vector<vector<int>>& pairs) {
    if (pairs.empty()) {
        return 0;
    }

    std::sort(pairs.begin(), pairs.end(), [](const Pair& lhs, const Pair& rhs) {
        return lhs[0] < rhs[0];
    });

    auto maxLengths = std::vector<int>(pairs.size());
    for (int ii = 0; ii < pairs.size(); ++ii) {
        auto bestLength = 1;
        for (int j = 0; j < ii; ++j) {
            if (pairs[j][1] < pairs[ii][0]) {
                bestLength = std::max(bestLength, maxLengths[j]+1);
            }
        }

        maxLengths[ii] = bestLength;
    }

    return *std::max_element(maxLengths.begin(), maxLengths.end());
}

}

int main() {
    auto input = std::vector<Pair> { {1, 2}, {2, 3}, {3, 4} };
    
    std::cout << findLongestChain(input) << '\n';
}

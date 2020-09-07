// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

#include <limits>
#include <algorithm>
#include <vector>

namespace {

static bool kLengthApart(std::vector<int>& nums, int k) {
    auto prevOne = std::find(nums.begin(), nums.end(), 1);
    if (std::end(nums) == prevOne) {
        return true;
    }

    auto minDist = std::numeric_limits<int>::max();
    auto iter = std::next(prevOne);
    while (iter != std::end(nums)) {
        if (1 == *iter) {
            int distance = std::distance(prevOne, iter) - 1;
            minDist = std::min(minDist, distance);
            prevOne = iter;
        }

        ++iter;
    }

    return k <= minDist;
}

}  // close anonymous namespace

int main(int argc, const char** argv) {
    auto vec = std::vector<int> {1, 0, 0, 0, 1, 0, 0, 1};
    const auto k = 2;
    
    assert(kLengthApart(vec, 2));
}

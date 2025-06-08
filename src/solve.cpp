 #define NDEBUG

#include <iostream>

void solve() {
    
}

__attribute__((constructor))
void init() {
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

int main() {
    solve();
}
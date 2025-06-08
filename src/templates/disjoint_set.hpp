#include <vector>
#include <cassert>

class disjoint_set {
    private:
        int _n;
        std::vector<int> parent_or_size;

    public:
        disjoint_set(): _n(0) {}
        disjoint_set(int n): _n(n), parent_or_size(n, -1) {}

        void merge(int x, int y) {
            assert(0 <= x && x < _n);
            assert(0 <= y && y < _n);

            x = find(x);
            y = find(y);

            if (x == y)
                return;

            if (parent_or_size[x] > parent_or_size[y])
                std::swap(x, y);
            
            parent_or_size[x] += parent_or_size[y];
            parent_or_size[y] = x;
        }

        int find(int x) {
            assert(0 <= x && x < _n);

            if (parent_or_size[x] < 0)
                return x;
            else
                return parent_or_size[x] = find(parent_or_size[x]);
        }

        bool same(int x, int y) {
            assert(0 <= x && x < _n);
            assert(0 <= y && y < _n);

            return find(x) == find(y);
        }
        
        int size(int x) {
            assert(0 <= x && x < _n);

            return -parent_or_size[find(x)];
        }
};

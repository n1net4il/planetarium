/********************************************************************************/

#include <vector>
#include <functional>
#include <cassert>
#include <cmath>

template <typename T>
class segment_tree {
private:
    int _n, _m;
    std::vector<T> tree;

    std::function<T(T, T)> op;
    T identity;

public:
    segment_tree(): _n(0), _m(0) {}

    segment_tree(const std::vector<T> &arr, std::function<T(T, T)> op, T identity)
        : op(op), identity(identity) {
        _n = arr.size();

        _m = 1 << ((int)std::ceil(std::log2(_n)));
        tree.resize(_m << 1, identity);

        for (int i = 0; i < _n; i++)
            tree[_m | i] = arr[i];
        for (int i = _n; i < _m; i++)
            tree[_m | i] = identity;

        for (int i = _m - 1; i > 0; i--)
            tree[i] = op(tree[i << 1], tree[(i << 1) | 1]);
    }
    
    segment_tree(int n, std::function<T(T, T)> op, T identity)
        : _n(n), op(op), identity(identity) {
        _m = 1 << ((int)std::ceil(std::log2(n)));
        tree.resize(_m << 1, identity);
    }

    T root() const {
        assert (_n > 0);

        return tree[1];
    }

    T get(int index) const {
        assert(0 <= index && index < _n);

        return tree[index + _m];
    }

    T query(int start, int end) const {
        assert(0 <= start && start <= end && end <= _n);

        T value = identity;

        for (
            start += _m, end += _m;
            start < end;
            start >>= 1, end >>= 1
        ) {
            if (start & 1) value = op(tree[start++], value);
            if (  end & 1) value = op(value, tree[--end]);
        }

        return value;
    }
    
    void update(int index, T value) {
        assert(0 <= index && index < _n);

        for (tree[index += _m] = value; index > 1; index >>= 1)
            tree[index >> 1] = op(tree[index], tree[index ^ 1]);            
    }

    void update(int index, const std::function<T(T)> &func) {
        T value = func(get(index));
        update(index, value);
    }
};

/********************************************************************************/
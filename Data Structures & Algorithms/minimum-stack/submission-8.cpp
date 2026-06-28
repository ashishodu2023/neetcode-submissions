class MinStack {
   private:
    vector<int> stack;
    vector<int> min_stack;

   public:
    MinStack() {}

    void push(int val) {
        stack.push_back(val);
        if (min_stack.empty() || val <= min_stack.back()) {
            min_stack.push_back(val);
        } else {
            min_stack.push_back(min_stack.back());
        }
    }

    void pop() {
        if (!stack.empty()) {
            stack.pop_back();
            min_stack.pop_back();
        }
    }

    int top() { return stack.back(); }

    int getMin() { return min_stack.back(); }
};

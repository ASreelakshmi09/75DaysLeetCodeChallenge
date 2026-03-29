function createCounter(n: number): () => number {
    let i = n;
    return function () {
        return i++;
    };
}

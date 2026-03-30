type Fn = (...params: any[]) => any;

function memoize(fn: Fn): Fn {
    const cache: Record<string, any> = {};

    return function (...args: any[]) {
        // Convert args array into a string key
        const key = JSON.stringify(args);

        if (key in cache) {
            return cache[key];
        }
        const result = fn(...args);
        cache[key] = result;
        return result;
    };
}


/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
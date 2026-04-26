import java.util.LinkedList;
import java.util.Queue;

class Solution {
    long[] segmentinc;
    long[] segmentdec;

    void updateinc(int l, int r, int index, int pos, long val) {
        if (l == r) {
            segmentinc[index] = Math.max(segmentinc[index], val);
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) {
            updateinc(l, mid, 2 * index, pos, val);
        } else {
            updateinc(mid + 1, r, 2 * index + 1, pos, val);
        }
        segmentinc[index] = Math.max(segmentinc[2 * index], segmentinc[2 * index + 1]);
    }

    long queryinc(int l, int r, int index, int ql, int qr) {
        if (ql <= l && qr >= r) {
            return segmentinc[index];
        }
        if (ql > r || qr < l) {
            return 0;
        }
        int mid = (l + r) / 2;
        long a = queryinc(l, mid, 2 * index, ql, qr);
        long b = queryinc(mid + 1, r, 2 * index + 1, ql, qr);
        return Math.max(a, b);
    }

    void updatedec(int l, int r, int index, int pos, long val) {
        if (l == r) {
            segmentdec[index] = Math.max(segmentdec[index], val);
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) {
            updatedec(l, mid, 2 * index, pos, val);
        } else {
            updatedec(mid + 1, r, 2 * index + 1, pos, val);
        }
        segmentdec[index] = Math.max(segmentdec[2 * index], segmentdec[2 * index + 1]);
    }

    long querydec(int l, int r, int index, int ql, int qr) {
        if (ql <= l && qr >= r) {
            return segmentdec[index];
        }
        if (ql > r || qr < l) {
            return 0;
        }
        int mid = (l + r) / 2;
        long a = querydec(l, mid, 2 * index, ql, qr);
        long b = querydec(mid + 1, r, 2 * index + 1, ql, qr);
        return Math.max(a, b);
    }

    // Custom Pair class since Java doesn't have std::pair
    static class Pair {
        int first;
        long second;
        Pair(int first, long second) {
            this.first = first;
            this.second = second;
        }
    }

    public long maxAlternatingSum(int[] nums, int k) {
        int n = nums.length;
        
        // Find the maximum element to size our segment tree
        int m = 0;
        for (int num : nums) {
            m = Math.max(m, num);
        }
        m++;
        
        long ans = 0;
        segmentinc = new long[4 * m];
        segmentdec = new long[4 * m];
        
        Queue<Pair> qinc = new LinkedList<>();
        Queue<Pair> qdec = new LinkedList<>();
        
        for (int i = n - 1; i >= 0; i--) {
            int curr = nums[i];
            
            // Process delayed updates FIRST before doing any queries
            if (qdec.size() == k) {
                Pair p = qdec.poll();
                updatedec(0, m - 1, 1, p.first, p.second);
            }
            if (qinc.size() == k) {
                Pair p = qinc.poll();
                updateinc(0, m - 1, 1, p.first, p.second);
            }
            
            // Query valid transitions from the trees
            long mxdec = queryinc(0, m - 1, 1, 0, curr - 1);
            qdec.add(new Pair(curr, curr + mxdec));
            
            long mxinc = querydec(0, m - 1, 1, curr + 1, m - 1);
            qinc.add(new Pair(curr, curr + mxinc));
            
            // Update the maximum answer found so far
            ans = Math.max(ans, curr + mxdec);
            ans = Math.max(ans, curr + mxinc);
        }
        
        return ans;
    }
}
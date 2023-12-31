class CppSolution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Step 1: Initialize two pointers, p1 to the end of the valid elements in nums1, 
        // and p2 to the end of nums2
        int p1 = m - 1;
        int p2 = n - 1;
        
        // Step 2: Initialize a pointer to hold the current position in nums1 where 
        // the next largest element should be placed. Initially, it will be at the end of nums1.
        int current = m + n - 1;
        
        // Step 3: Loop until we have exhausted either nums1 or nums2
        while (p1 >= 0 && p2 >= 0) {
            // Step 4: Compare the elements at p1 and p2, 
            // and place the larger element at the current position in nums1
            if (nums1[p1] > nums2[p2]) {
                nums1[current] = nums1[p1];
                p1--;
            } else {
                nums1[current] = nums2[p2];
                p2--;
            }
            
            // Step 5: Decrease the current position pointer
            current--;
        }
        
        // Step 6: If there are leftover elements in nums2, copy them into nums1
        while (p2 >= 0) {
            nums1[current] = nums2[p2];
            p2--;
            current--;
        }
        
        // Step 7: If there are leftover elements in nums1, they are already in their correct place
    }
};

# Define a Solution class
class PythonSolution(object):
    # Define a method named 'merge' with parameters: nums1, m, nums2, and n
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]  # Parameter nums1 is of type list of integers
        :type m: int            # Parameter m is of type integer
        :type nums2: List[int]  # Parameter nums2 is of type list of integers
        :type n: int            # Parameter n is of type integer
        :rtype: None            # The return type is None, this method does not return anything but modifies nums1 in place
        """
        # Initialize three pointers: p1, p2, and target
        p1 = m - 1  # Point to the last valid element in nums1
        p2 = n - 1  # Point to the last element in nums2
        target = m + n - 1  # Point to the last position in the merged array
        
        # Print the initial state of nums1 and nums2
        print(nums1)
        print(nums2)
        
        # Loop to merge elements from nums1 and nums2 in descending order
        while (p1 >=0 and p2 >= 0):
          # If the current element in nums1 is greater than the current element in nums2
          if (nums1[p1] > nums2[p2]) :
            nums1[target] = nums1[p1]  # Place the greater element at the current target position
            p1 -= 1  # Move p1 one step back
          else :
            nums1[target] = nums2[p2]  # Otherwise, place the element from nums2 at the current target position
            p2 -= 1   # Move p2 one step back
          target -= 1  # Move the target pointer one step back
        
        # Print the intermediate state of nums1
        print(nums1)

        # Loop to add any remaining elements from nums2 to nums1
        while (p2 >= 0) :
          nums1[target] = nums2[p2]  # Add the current element from nums2 to nums1 at the current target position
          p2 -= 1  # Move p2 one step back
          target -= 1  # Move the target pointer one step back

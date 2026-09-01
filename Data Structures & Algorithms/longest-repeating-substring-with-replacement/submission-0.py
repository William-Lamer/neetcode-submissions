class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {char:0 for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        left, right = 0, 0
        longest_window = 0
        


        while True:
            if (len(s) - 1) - left  < longest_window:
                return longest_window

            window_length = right - left + 1

            # Update the count of the new right character
            window[s[right]] += 1

            # Get the count of the most frequent character in the window
            most_frequent_count = max(window.values())

            if window_length - most_frequent_count <= k:
                longest_window = max(longest_window, window_length)
            else:
                window[s[left]] -= 1
                left += 1
                
            right += 1

        return longest_window



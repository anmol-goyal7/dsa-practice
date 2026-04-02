#!/usr/bin/env python3
"""Scan solution files and generate README.md with NeetCode 150 progress."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Complete NeetCode 150 problem list.
# Each entry: (filename_slugs, problem_name, leetcode_number)
# filename_slugs: list of possible filenames (without .cpp) that match this problem.
CATEGORIES = {
    "Arrays & Hashing": {
        "dir": "arrays-and-hashing",
        "problems": [
            (["contains_duplicate", "contains-duplicate"], "Contains Duplicate", 217),
            (["valid_anagram", "valid-anagram"], "Valid Anagram", 242),
            (["two_sum", "two-sum", "two-sum-hashmaps", "two_sum_hashmaps"], "Two Sum", 1),
            (["group_anagrams", "group-anagrams"], "Group Anagrams", 49),
            (["top_k_frequent_elements", "top-k-frequent-elements", "top_k_frequent"], "Top K Frequent Elements", 347),
            (["encode_and_decode_strings", "encode-and-decode-strings", "encode_decode_strings", "encode-decode-strings"], "Encode and Decode Strings", 271),
            (["product_of_array_except_self", "product-of-array-except-self", "product_except_self", "product-except-self"], "Product of Array Except Self", 238),
            (["valid_sudoku", "valid-sudoku"], "Valid Sudoku", 36),
            (["longest_consecutive_sequence", "longest-consecutive-sequence", "longest_consecutive"], "Longest Consecutive Sequence", 128),
        ],
    },
    "Two Pointers": {
        "dir": "two-pointers",
        "problems": [
            (["valid_palindrome", "valid-palindrome"], "Valid Palindrome", 125),
            (["two_sum_ii", "two-sum-ii", "two_sum_2", "two-sum-2"], "Two Sum II", 167),
            (["3sum", "three_sum", "three-sum"], "3Sum", 15),
            (["container_with_most_water", "container-with-most-water"], "Container With Most Water", 11),
            (["trapping_rain_water", "trapping-rain-water"], "Trapping Rain Water", 42),
        ],
    },
    "Sliding Window": {
        "dir": "sliding-window",
        "problems": [
            (["best_time_to_buy_and_sell_stock", "best-time-to-buy-and-sell-stock", "buy_sell_stock", "buy-sell-stock"], "Best Time to Buy and Sell Stock", 121),
            (["longest_substring_without_repeating_characters", "longest-substring-without-repeating-characters", "longest_substring", "longest-substring"], "Longest Substring Without Repeating Characters", 3),
            (["longest_repeating_character_replacement", "longest-repeating-character-replacement"], "Longest Repeating Character Replacement", 424),
            (["permutation_in_string", "permutation-in-string"], "Permutation in String", 567),
            (["minimum_window_substring", "minimum-window-substring"], "Minimum Window Substring", 76),
            (["sliding_window_maximum", "sliding-window-maximum"], "Sliding Window Maximum", 239),
        ],
    },
    "Stack": {
        "dir": "stack",
        "problems": [
            (["valid_parentheses", "valid-parentheses"], "Valid Parentheses", 20),
            (["min_stack", "min-stack"], "Min Stack", 155),
            (["evaluate_reverse_polish_notation", "evaluate-reverse-polish-notation", "reverse_polish_notation", "reverse-polish-notation"], "Evaluate Reverse Polish Notation", 150),
            (["generate_parentheses", "generate-parentheses"], "Generate Parentheses", 22),
            (["daily_temperatures", "daily-temperatures"], "Daily Temperatures", 739),
            (["car_fleet", "car-fleet"], "Car Fleet", 853),
            (["largest_rectangle_in_histogram", "largest-rectangle-in-histogram"], "Largest Rectangle in Histogram", 84),
        ],
    },
    "Binary Search": {
        "dir": "binary-search",
        "problems": [
            (["binary_search", "binary-search"], "Binary Search", 704),
            (["search_a_2d_matrix", "search-a-2d-matrix", "search_2d_matrix", "search-2d-matrix"], "Search a 2D Matrix", 74),
            (["koko_eating_bananas", "koko-eating-bananas"], "Koko Eating Bananas", 875),
            (["find_minimum_in_rotated_sorted_array", "find-minimum-in-rotated-sorted-array", "find_min_rotated", "find-min-rotated"], "Find Minimum in Rotated Sorted Array", 153),
            (["search_in_rotated_sorted_array", "search-in-rotated-sorted-array"], "Search in Rotated Sorted Array", 33),
            (["time_based_key_value_store", "time-based-key-value-store"], "Time Based Key-Value Store", 981),
            (["median_of_two_sorted_arrays", "median-of-two-sorted-arrays"], "Median of Two Sorted Arrays", 4),
        ],
    },
    "Linked List": {
        "dir": "linked-list",
        "problems": [
            (["reverse_linked_list", "reverse-linked-list"], "Reverse Linked List", 206),
            (["merge_two_sorted_lists", "merge-two-sorted-lists"], "Merge Two Sorted Lists", 21),
            (["reorder_list", "reorder-list"], "Reorder List", 143),
            (["remove_nth_node_from_end_of_list", "remove-nth-node-from-end-of-list", "remove_nth_node", "remove-nth-node"], "Remove Nth Node From End of List", 19),
            (["copy_list_with_random_pointer", "copy-list-with-random-pointer"], "Copy List with Random Pointer", 138),
            (["add_two_numbers", "add-two-numbers"], "Add Two Numbers", 2),
            (["linked_list_cycle", "linked-list-cycle"], "Linked List Cycle", 141),
            (["find_the_duplicate_number", "find-the-duplicate-number", "find_duplicate", "find-duplicate"], "Find The Duplicate Number", 287),
            (["lru_cache", "lru-cache"], "LRU Cache", 146),
            (["merge_k_sorted_lists", "merge-k-sorted-lists"], "Merge K Sorted Lists", 23),
            (["reverse_nodes_in_k_group", "reverse-nodes-in-k-group", "reverse_k_group", "reverse-k-group"], "Reverse Nodes in K-Group", 25),
        ],
    },
    "Trees": {
        "dir": "trees",
        "problems": [
            (["invert_binary_tree", "invert-binary-tree"], "Invert Binary Tree", 226),
            (["maximum_depth_of_binary_tree", "maximum-depth-of-binary-tree", "max_depth", "max-depth"], "Maximum Depth of Binary Tree", 104),
            (["diameter_of_binary_tree", "diameter-of-binary-tree"], "Diameter of Binary Tree", 543),
            (["balanced_binary_tree", "balanced-binary-tree"], "Balanced Binary Tree", 110),
            (["same_tree", "same-tree"], "Same Tree", 100),
            (["subtree_of_another_tree", "subtree-of-another-tree"], "Subtree of Another Tree", 572),
            (["lowest_common_ancestor_of_a_bst", "lowest-common-ancestor-of-a-bst", "lowest_common_ancestor", "lowest-common-ancestor"], "Lowest Common Ancestor of a BST", 235),
            (["binary_tree_level_order_traversal", "binary-tree-level-order-traversal", "level_order_traversal", "level-order-traversal"], "Binary Tree Level Order Traversal", 102),
            (["binary_tree_right_side_view", "binary-tree-right-side-view", "right_side_view", "right-side-view"], "Binary Tree Right Side View", 199),
            (["count_good_nodes_in_binary_tree", "count-good-nodes-in-binary-tree", "good_nodes", "good-nodes"], "Count Good Nodes in Binary Tree", 1448),
            (["validate_binary_search_tree", "validate-binary-search-tree", "validate_bst", "validate-bst"], "Validate Binary Search Tree", 98),
            (["kth_smallest_element_in_a_bst", "kth-smallest-element-in-a-bst", "kth_smallest", "kth-smallest"], "Kth Smallest Element in a BST", 230),
            (["construct_binary_tree_from_preorder_and_inorder_traversal", "construct-binary-tree-from-preorder-and-inorder-traversal", "construct_tree", "construct-tree"], "Construct Binary Tree from Preorder and Inorder Traversal", 105),
            (["binary_tree_maximum_path_sum", "binary-tree-maximum-path-sum", "max_path_sum", "max-path-sum"], "Binary Tree Maximum Path Sum", 124),
            (["serialize_and_deserialize_binary_tree", "serialize-and-deserialize-binary-tree", "serialize_deserialize", "serialize-deserialize"], "Serialize and Deserialize Binary Tree", 297),
        ],
    },
    "Tries": {
        "dir": "tries",
        "problems": [
            (["implement_trie", "implement-trie", "trie"], "Implement Trie (Prefix Tree)", 208),
            (["design_add_and_search_words_data_structure", "design-add-and-search-words-data-structure", "add_search_words", "add-search-words"], "Design Add and Search Words Data Structure", 211),
            (["word_search_ii", "word-search-ii", "word_search_2", "word-search-2"], "Word Search II", 212),
        ],
    },
    "Heap / Priority Queue": {
        "dir": "heap-priority-queue",
        "problems": [
            (["kth_largest_element_in_a_stream", "kth-largest-element-in-a-stream", "kth_largest_stream", "kth-largest-stream"], "Kth Largest Element in a Stream", 703),
            (["last_stone_weight", "last-stone-weight"], "Last Stone Weight", 1046),
            (["k_closest_points_to_origin", "k-closest-points-to-origin", "k_closest_points", "k-closest-points"], "K Closest Points to Origin", 973),
            (["kth_largest_element_in_an_array", "kth-largest-element-in-an-array", "kth_largest", "kth-largest"], "Kth Largest Element in an Array", 215),
            (["task_scheduler", "task-scheduler"], "Task Scheduler", 621),
            (["design_twitter", "design-twitter"], "Design Twitter", 355),
            (["find_median_from_data_stream", "find-median-from-data-stream", "median_data_stream", "median-data-stream"], "Find Median from Data Stream", 295),
        ],
    },
    "Backtracking": {
        "dir": "backtracking",
        "problems": [
            (["subsets"], "Subsets", 78),
            (["combination_sum", "combination-sum"], "Combination Sum", 39),
            (["permutations"], "Permutations", 46),
            (["subsets_ii", "subsets-ii", "subsets_2", "subsets-2"], "Subsets II", 90),
            (["combination_sum_ii", "combination-sum-ii", "combination_sum_2", "combination-sum-2"], "Combination Sum II", 40),
            (["word_search", "word-search"], "Word Search", 79),
            (["palindrome_partitioning", "palindrome-partitioning"], "Palindrome Partitioning", 131),
            (["letter_combinations_of_a_phone_number", "letter-combinations-of-a-phone-number", "letter_combinations", "letter-combinations"], "Letter Combinations of a Phone Number", 17),
            (["n_queens", "n-queens"], "N-Queens", 51),
        ],
    },
    "Graphs": {
        "dir": "graphs",
        "problems": [
            (["number_of_islands", "number-of-islands"], "Number of Islands", 200),
            (["max_area_of_island", "max-area-of-island"], "Max Area of Island", 695),
            (["clone_graph", "clone-graph"], "Clone Graph", 133),
            (["walls_and_gates", "walls-and-gates"], "Walls and Gates", 286),
            (["rotting_oranges", "rotting-oranges"], "Rotting Oranges", 994),
            (["pacific_atlantic_water_flow", "pacific-atlantic-water-flow"], "Pacific Atlantic Water Flow", 417),
            (["surrounded_regions", "surrounded-regions"], "Surrounded Regions", 130),
            (["course_schedule", "course-schedule"], "Course Schedule", 207),
            (["course_schedule_ii", "course-schedule-ii", "course_schedule_2", "course-schedule-2"], "Course Schedule II", 210),
            (["graph_valid_tree", "graph-valid-tree"], "Graph Valid Tree", 261),
            (["number_of_connected_components", "number-of-connected-components", "connected_components", "connected-components"], "Number of Connected Components in an Undirected Graph", 323),
            (["redundant_connection", "redundant-connection"], "Redundant Connection", 684),
            (["word_ladder", "word-ladder"], "Word Ladder", 127),
        ],
    },
    "Advanced Graphs": {
        "dir": "advanced-graphs",
        "problems": [
            (["reconstruct_itinerary", "reconstruct-itinerary"], "Reconstruct Itinerary", 332),
            (["min_cost_to_connect_all_points", "min-cost-to-connect-all-points"], "Min Cost to Connect All Points", 1584),
            (["network_delay_time", "network-delay-time"], "Network Delay Time", 743),
            (["swim_in_rising_water", "swim-in-rising-water"], "Swim in Rising Water", 778),
            (["alien_dictionary", "alien-dictionary"], "Alien Dictionary", 269),
            (["cheapest_flights_within_k_stops", "cheapest-flights-within-k-stops", "cheapest_flights", "cheapest-flights"], "Cheapest Flights Within K Stops", 787),
        ],
    },
    "1-D Dynamic Programming": {
        "dir": "1d-dynamic-programming",
        "problems": [
            (["climbing_stairs", "climbing-stairs"], "Climbing Stairs", 70),
            (["min_cost_climbing_stairs", "min-cost-climbing-stairs"], "Min Cost Climbing Stairs", 746),
            (["house_robber", "house-robber"], "House Robber", 198),
            (["house_robber_ii", "house-robber-ii", "house_robber_2", "house-robber-2"], "House Robber II", 213),
            (["longest_palindromic_substring", "longest-palindromic-substring"], "Longest Palindromic Substring", 5),
            (["palindromic_substrings", "palindromic-substrings"], "Palindromic Substrings", 647),
            (["decode_ways", "decode-ways"], "Decode Ways", 91),
            (["coin_change", "coin-change"], "Coin Change", 322),
            (["maximum_product_subarray", "maximum-product-subarray", "max_product_subarray", "max-product-subarray"], "Maximum Product Subarray", 152),
            (["word_break", "word-break"], "Word Break", 139),
            (["longest_increasing_subsequence", "longest-increasing-subsequence"], "Longest Increasing Subsequence", 300),
            (["partition_equal_subset_sum", "partition-equal-subset-sum"], "Partition Equal Subset Sum", 416),
        ],
    },
    "2-D Dynamic Programming": {
        "dir": "2d-dynamic-programming",
        "problems": [
            (["unique_paths", "unique-paths"], "Unique Paths", 62),
            (["longest_common_subsequence", "longest-common-subsequence"], "Longest Common Subsequence", 1143),
            (["best_time_to_buy_and_sell_stock_with_cooldown", "best-time-to-buy-and-sell-stock-with-cooldown", "buy_sell_stock_cooldown", "buy-sell-stock-cooldown"], "Best Time to Buy and Sell Stock with Cooldown", 309),
            (["coin_change_ii", "coin-change-ii", "coin_change_2", "coin-change-2"], "Coin Change II", 518),
            (["target_sum", "target-sum"], "Target Sum", 494),
            (["interleaving_string", "interleaving-string"], "Interleaving String", 97),
            (["longest_increasing_path_in_a_matrix", "longest-increasing-path-in-a-matrix", "longest_increasing_path", "longest-increasing-path"], "Longest Increasing Path in a Matrix", 329),
            (["distinct_subsequences", "distinct-subsequences"], "Distinct Subsequences", 115),
            (["edit_distance", "edit-distance"], "Edit Distance", 72),
            (["burst_balloons", "burst-balloons"], "Burst Balloons", 312),
            (["regular_expression_matching", "regular-expression-matching", "regex_matching", "regex-matching"], "Regular Expression Matching", 10),
        ],
    },
    "Greedy": {
        "dir": "greedy",
        "problems": [
            (["maximum_subarray", "maximum-subarray", "max_subarray", "max-subarray"], "Maximum Subarray", 53),
            (["jump_game", "jump-game"], "Jump Game", 55),
            (["jump_game_ii", "jump-game-ii", "jump_game_2", "jump-game-2"], "Jump Game II", 45),
            (["gas_station", "gas-station"], "Gas Station", 134),
            (["hand_of_straights", "hand-of-straights"], "Hand of Straights", 846),
            (["merge_triplets_to_form_target_triplet", "merge-triplets-to-form-target-triplet", "merge_triplets", "merge-triplets"], "Merge Triplets to Form Target Triplet", 1899),
            (["partition_labels", "partition-labels"], "Partition Labels", 763),
            (["valid_parenthesis_string", "valid-parenthesis-string"], "Valid Parenthesis String", 678),
        ],
    },
    "Intervals": {
        "dir": "intervals",
        "problems": [
            (["insert_interval", "insert-interval"], "Insert Interval", 57),
            (["merge_intervals", "merge-intervals"], "Merge Intervals", 56),
            (["non_overlapping_intervals", "non-overlapping-intervals"], "Non-overlapping Intervals", 435),
            (["meeting_rooms", "meeting-rooms"], "Meeting Rooms", 252),
            (["meeting_rooms_ii", "meeting-rooms-ii", "meeting_rooms_2", "meeting-rooms-2"], "Meeting Rooms II", 253),
            (["minimum_interval_to_include_each_query", "minimum-interval-to-include-each-query", "minimum_interval", "minimum-interval"], "Minimum Interval to Include Each Query", 1851),
        ],
    },
    "Math & Geometry": {
        "dir": "math-and-geometry",
        "problems": [
            (["rotate_image", "rotate-image"], "Rotate Image", 48),
            (["spiral_matrix", "spiral-matrix"], "Spiral Matrix", 54),
            (["set_matrix_zeroes", "set-matrix-zeroes"], "Set Matrix Zeroes", 73),
            (["happy_number", "happy-number"], "Happy Number", 202),
            (["plus_one", "plus-one"], "Plus One", 66),
            (["pow_x_n", "pow-x-n", "powx_n", "powx-n"], "Pow(x, n)", 50),
            (["multiply_strings", "multiply-strings"], "Multiply Strings", 43),
            (["detect_squares", "detect-squares"], "Detect Squares", 2013),
        ],
    },
    "Bit Manipulation": {
        "dir": "bit-manipulation",
        "problems": [
            (["single_number", "single-number"], "Single Number", 136),
            (["number_of_1_bits", "number-of-1-bits", "number_of_one_bits", "hamming_weight", "hamming-weight"], "Number of 1 Bits", 191),
            (["counting_bits", "counting-bits"], "Counting Bits", 338),
            (["reverse_bits", "reverse-bits"], "Reverse Bits", 190),
            (["missing_number", "missing-number"], "Missing Number", 268),
            (["sum_of_two_integers", "sum-of-two-integers"], "Sum of Two Integers", 371),
            (["reverse_integer", "reverse-integer"], "Reverse Integer", 7),
        ],
    },
}


def find_solved(category_dir: str, slugs: list[str]) -> str | None:
    """Return the path to the first matching solution file, or None."""
    dir_path = REPO_ROOT / category_dir
    if not dir_path.is_dir():
        return None
    existing = {f.stem: f.name for f in dir_path.iterdir() if f.suffix == ".cpp"}
    for slug in slugs:
        if slug in existing:
            return f"{category_dir}/{existing[slug]}"
    return None


def name_to_slug(name: str) -> str:
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9\s]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    return slug


def generate() -> str:
    lines: list[str] = []
    total_solved = 0
    total_problems = 0

    lines.append("# NeetCode 150 - C++ Solutions")
    lines.append("")
    lines.append("My solutions to the [NeetCode 150](https://neetcode.io/practice) problem list in C++.")
    lines.append("")
    lines.append("**LeetCode Profile:** [anmol-goyal7](https://leetcode.com/u/anmol-goyal7/)")
    lines.append("")

    # Count totals first for the badge
    for cat_name, cat_data in CATEGORIES.items():
        for slugs, name, lc_num in cat_data["problems"]:
            total_problems += 1
            if find_solved(cat_data["dir"], slugs):
                total_solved += 1

    lines.append(f"### Progress: `{total_solved} / {total_problems}` completed")
    lines.append("")

    for cat_name, cat_data in CATEGORIES.items():
        cat_solved = 0
        cat_total = len(cat_data["problems"])
        table_rows: list[str] = []

        for slugs, name, lc_num in cat_data["problems"]:
            solved_path = find_solved(cat_data["dir"], slugs)
            lc_slug = name_to_slug(name)
            lc_link = f"https://leetcode.com/problems/{lc_slug}/"

            if solved_path:
                cat_solved += 1
                status = f"[Solution]({solved_path})"
            else:
                status = ""

            table_rows.append(f"| [{name}]({lc_link}) | {status} |")

        lines.append(f"### {cat_name} ({cat_solved}/{cat_total})")
        lines.append("")
        lines.append("| Problem | Solution |")
        lines.append("|---------|----------|")
        lines.extend(table_rows)
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    readme_path = REPO_ROOT / "README.md"
    content = generate()
    readme_path.write_text(content)
    print(f"README.md generated ({readme_path})")

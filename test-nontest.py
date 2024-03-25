def filter_and_write(input_file_path, output_test_file_path, output_other_file_path):
    with open('reviews-english.txt', 'r') as input_file, \
         open('test-related-reviews.txt', 'w') as output_test_file, \
         open('non-test-reviews.txt', 'w') as output_other_file:

        for line in input_file:
            if 'test' in line:
                output_test_file.write(line)
            else:
                output_other_file.write(line)

# Example usage:
input_file_path = 'input.txt'
output_test_file_path = 'output_test.txt'
output_other_file_path = 'output_other.txt'

filter_and_write(input_file_path, output_test_file_path, output_other_file_path)

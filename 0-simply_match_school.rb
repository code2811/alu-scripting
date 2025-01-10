#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

# Get the input string from command line argument
input_string = ARGV[0]

# Match the word "School" in the input string
# The pattern /School/ will match exactly the word "School"
matches = input_string.scan(/School/)

# Print all matches joined together (without spaces)
# If no matches are found, an empty string will be printed
puts matches.join

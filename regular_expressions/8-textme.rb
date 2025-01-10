#!/usr/bin/env ruby

log_entry = ARGV[0]

# Regular expression to extract the required parts from the log entry
regex = /\[from:([^\]]+)\].*\[to:([^\]]+)\].*\[flags:([^\]]+)\]/

# Match the regex and extract the parts
match = log_entry.match(regex)

# Output the result if a match is found
if match
  puts "#{match[1]},#{match[2]},#{match[3]}"
end
````

#!/usr/bin/env ruby
# Match the sender, receiver, and flags using regular expressions
log_line = ARGV[0]
matches = log_line.match(/from:(\S+).+to:(\S+).+flags:(\S+)/)

# If a match is found, output the sender, receiver, and flags
if matches
  puts "#{matches[1]},#{matches[2]},#{matches[3]}"
end


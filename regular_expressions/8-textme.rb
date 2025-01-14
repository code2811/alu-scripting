#!/usr/bin/env ruby

# Regular expression to match the necessary parts of the log line
log_pattern = /from:(\S+).*to:(\S+).*flags:(\S+)/

# Read each line from standard input
ARGF.each do |line|
  # Search for the relevant parts using the regular expression
  if match = line.match(log_pattern)
    sender = match[1]  # The sender's phone number or name
    receiver = match[2]  # The receiver's phone number or name
    flags = match[3]  # The flags used

    # Print the result in the required format
    puts "#{sender},#{receiver},#{flags}"
  end
end
i

#!/usr/bin/env ruby

# Check if there's a command-line argument
if ARGV.length != 1
puts "Usage: #{$PROGRAM_NAME} <string>"
exit 1
end

puts ARGV[0].scan(/School/).join

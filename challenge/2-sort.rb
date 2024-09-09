###
#
#  Sort integer arguments (ascending)
#
###

result = []
ARGV.each do |arg|
  # skip if not integer
  next if arg !~ /^-?[0-9]+$/

  # convert to integer
  i_arg = arg.to_i

  # insert the integer into the result array
  result << i_arg
end

# sort the result in ascending order
result.sort!

puts result

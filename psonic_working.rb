live_loop :run_code_receiver do
  data = sync "/osc*/run-code"  # Listen for /run-code messages
  puts "Received Ruby code: #{data[1]}"  # Log the Ruby code
  eval(data[1]) if data[1]  # Execute the Ruby code if it exists
end

live_loop :debug_osc do
  data = sync "/osc/*"
  puts "Debug OSC message: #{data}"
end

live_loop :stopper do
  stop_cue = sync "/cue/stop_sound"
  stop :my_sound
end
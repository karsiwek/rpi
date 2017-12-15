require 'sinatra'
require 'json'

PAGE = "<br/><a href='/light/on'>on</a><br/><a href='/light/off'>off</a><br/><a href='/light/blink'>blink</a>"
get "/" do
	PAGE
end
get "/graph/outside" do
	send_file File.join("/logs/temp/outside1/", "graph.png")
end
get "/graph/inside" do
	send_file File.join("/logs/temp/inside1/", "graph.png")
end
get "/graph/all" do
	send_file File.join("/logs/temp/graphs/", "graph.png")
end
get "/light" do
	print "<html>LIGHT!"+PAGE
end
get "/light/on" do
	system "sudo python /home/pi/scripts/on.py &"
	"<html>"+"light on!"+PAGE
end
get "/light/off" do
	system "sudo python /home/pi/scripts/off.py &"
	"light off" + PAGE
end
get "/light/blink" do
	system "sudo python /home/pi/scripts/blink_long.py &"
 	"blink blink!"	+PAGE
end

get "/aquarium/light/on" do
	headers 'Access-Control-Allow-Origin' => '*'
        system "sudo python /home/pi/scripts/aquarium/aqua.py light on"
        "light on!"
end     
get "/aquarium/heater/on" do
	headers 'Access-Control-Allow-Origin' => '*'
        system "sudo python /home/pi/scripts/aquarium/aqua.py heater on"
        "grzala on"
end     
get "/aquarium/filter/on" do
	headers 'Access-Control-Allow-Origin' => '*'
        system "sudo python /home/pi/scripts/aquarium/aqua.py filter on"
        "bomble on!"
end     
get "/aquarium/light/off" do
	headers 'Access-Control-Allow-Origin' => '*'
        system "sudo python /home/pi/scripts/aquarium/aqua.py light off"
        "light off"
end     
get "/aquarium/heater/off" do
	headers 'Access-Control-Allow-Origin' => '*'
        system "sudo python /home/pi/scripts/aquarium/aqua.py heater off"
        "grzala off"
end
get "/aquarium/filter/off" do
	headers 'Access-Control-Allow-Origin' => '*'
        system "sudo python /home/pi/scripts/aquarium/aqua.py filter off"
        "bomble off!"
end
get "/aquarium/status" do
        headers 'Access-Control-Allow-Origin' => '*'
        status = system "sudo python /home/pi/scripts/aquarium/status.py"
        
        status
end   
get "/test" do
	File.read('/tmp/test')
end
post "/status" do
	request.body.rewind
    	request_payload = JSON.parse(request.body.read.to_s)

    	puts(request_payload)

	File.open('/tmp/test', 'w') { |file| file.write(request_payload) }
	status 200
  	body ''
end

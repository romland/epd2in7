{
   "targets" : [
      {
         "target_name": "epd2in7",
         "sources": ["src/epd2in7.cpp", "src/epdif.cpp"],
		 "libraries": [ "-L/usr/local/lib", "-lwiringPi"],
         "include_dirs" : [
            "<!(node -e \"require('nan')\")"
        ]
      }
   ]
}

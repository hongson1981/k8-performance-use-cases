# Run Artillery pod over Squid_icap Pod proxy

## Basic Flow

              
	  + ----------------------------------------------+              
	  | +----+-----+             +----+------+        |
	  | | Artilerry|             |           |        |
	  | | Pod      |             | Squid     |        |     +----+------+
	  | |          |-----------> | Proxy Pod |--------|---> | Tested    |
	  | |          |             |           |        |     | website   |
	  | +----+-----+             +----+------+        |     |           |
	  |               Kubernetes                      |     +----+------+
	  + ----------------------------------------------+                      

## Usage
### Build Docker imager for Squid_icap
   Refer /Docker/SquidProxy/Readme.md
### Build Docker imager  for Artillery
   Refer /Docker/Artillery/Readme.md
### Build and run Kubernetes pod for Squid_icap
   Refer /Kebernetes/SquidProxy/Readme.md
### Build and run Kubernetes pod for Artillery
	Refer /Kebernetes/Artillery/Readme.md
## License
MIT License
See: LICENSE

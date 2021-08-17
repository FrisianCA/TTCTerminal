# TTCTerminal

Python application to query TTC Station routes, and query route information for TTC subway and bus routes. 

I created this simple program, so I could easily get information for my bus route home from the command line.

## Installation

Clone the repository

```bash
git clone https://github.com/GarrettHofland/TTCTerminal.git

chmod +x ttcterminal.py
```
Add the following line to your .bash_profile

```bash
export PATH=$PATH:/path/to/download
```

## Usage 

```bash
ttc -h
```

```bash
ttc -s finch_station
```

```bash
ttc -r 309_finch_west finch_station 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
Do whatever you want with this.
# GetCryptoMarketData

script to grabs some fast data about crypto prices and dump it to csv 

## Installation

```bash
pip install requirements.txt
```

## Register for APIs

Get your Coinmarketcap api [here](https://coinmarketcap.com/api/). 

Get your FTX api [here](https://ftx.com/profile)

You will need to create a login and password in both cases. 

Store the keys in a .env file like so: 

```bash
COINMARKETCAP_API_KEY="blahblah"
READ_ONLY_FTX_API_KEY="blahblah"
READ_ONLY_FTX_API_SECRET="blahblah"
```


## Usage

```bash
python get_crypto_data.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
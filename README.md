# COVID-19 in Ontario Schools
Analyzes some of the publicly availible data from the Government of Ontario about COVID-19 cases in Ontario Schools

## Running the code

Pretty self explanitory here. Either download the code and the csv file or git clone the entire repo. Here are some instructions if you really need it.

```bash
git clone https://github.com/flyme2bluemoon/COVID-19-in-Ontario-Schools.git
cd COVID-19-in-Ontario-Schools
python3 cumulative_percentage.py
python3 school_boards.py
```

## Updating the dataset

Run the `get_data.sh` shell script to update the csv file(s).

```bash
chmod +x get_data.sh
./get_data.sh
```

## License

The code is licensed under the [MIT License](https://github.com/flyme2bluemoon/COVID-19-in-Ontario-Schools/blob/main/LICENSE)  
The COVID-19 data comes from the [Ontario Data Catalogue Dataset: Schools COVID-19 data](https://data.ontario.ca/dataset/summary-of-cases-in-schools). The data is subject to the [Open Government Licence (Ontario)](https://www.ontario.ca/page/open-government-licence-ontario).
# Log_report
### Installation
To use in your project just use your dependency manager to install it, with pip is like this:

`pip install log_report`
### Usage
Program takes path to directory with logs and return statistic about them  place|name|car|time 

arguments
- path first positional arg
- --driver optional takes name of driver statistic only about him
- --desc or --asc sort by, asc is default

`python -m log_report <path to dir with logs> --desc`

`python -m log_report <path to dir with logs>  --driver <name driver in "">`

### Documentation function and classes

the package has 2 classes and 2 function

* args_parser()

add arguments and parse, return namespace with them 

* parse_call(args_cm=<namespace_args>)

takes namespace of args from previous func and call something it depends what args were parsed

* class Log
  + obj Log parameters path
  + Log.read_data
  
    read data from files in path 
  + Log.get_logs
    
    validate for usage and return three lists with abbreviations start_time and end_time

* class Report
    + obj Report parameters abbr_list, start_list, end_list
    + Report.get_diff calculate difference 
  
       between start and end time 
    + Report.concatenate_sort_data 
      
       concatenate diff time with abbr and then sort it 
    + Report.output
        
       print statistic about all drivers
    + Report.driver
  
        takes name and get statistic about driver
  
    + Report.solo_output
        
        print statistic about driver work with previous method 
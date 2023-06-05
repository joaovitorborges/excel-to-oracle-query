# excel-to-oracle-query
Small script developed to convert an excel sheet into a table on Oracle SQL, formatting values as needed

## comments about code
- Excel file is read using Pandas dataframes.
- Monetary values had the currency (R$), commas(,) and dots(.) removed, which changes its stored value to decimal (cents).
- Single quotes (') had to be added to strings
- Date was kept in dd-mm-yyyy format

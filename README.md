# Language: R
# Input: TXT (keyword-value pairs)
# Output: CSV 
# Tested with: PluMA 1.0, R 4.0

PluMA plugin to append to a CSV file (row or column).

The plugin takes as input a TXT file of keyword-value pairs:
csvfile: The CSV file to which to append
column: New column name (if appending a column, otherwise leave out)
row: New row name (if appending a row, otherwise leave out)
value: New initial value in the row/column

The plugin will output a new CSV file, consisting of the original
CSV file with the new row/column.

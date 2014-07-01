# SELECT * FROM [nyc.dob_permit_issuance] where Owners_Business_Name like '%RED%' order by filing_date desc
# bq query --max_rows 20000 --format csv "SELECT * FROM [nyc.dob_permit_issuance] where Street_Name like '%VAN BUREN%' and borough like '%BROOKLYN%' order by filing_date desc"
# bq query --max_rows 20000 --format csv "SELECT filing_date FROM [nyc.dob_permit_issuance] order by filing_date asc limit 10"
# bq query --max_rows 20000 --format csv "SELECT year(filing_date) year, count(*) FROM [nyc.dob_permit_issuance] group by year order by year asc"
# bq query --max_rows 20000  "SELECT year(filing_date) year, count(*) count FROM [nyc.dob_permit_issuance] group by year order by year asc"
bq query --max_rows 20000 "SELECT * FROM [nyc.dob_permit_issuance] where owners_business_name like 'PRIME HOMES%'  order by filing_date desc"

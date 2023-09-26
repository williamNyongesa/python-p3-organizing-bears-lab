# sql_queries.py
















# Query to select all female bears and return their name and age
select_all_female_bears_return_name_and_age = '''
SELECT name, age
FROM bears
WHERE gender = 'F';
'''


# Query to select all bear names and order them alphabetically
select_all_bears_names_and_orders_in_alphabetical_order = '''
SELECT name
FROM bears
ORDER BY name ASC;
'''

# Query to select all bear names and ages that are alive and order them from youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = '''
SELECT name, age
FROM bears
WHERE status = 'alive'
ORDER BY age ASC;
'''

# Query to select the oldest bear and return its name and age
select_oldest_bear_and_returns_name_and_age = '''
SELECT name, age
FROM bears
ORDER BY age DESC
LIMIT 1;
'''

# Query to select the youngest bear and return its name and age
select_youngest_bear_and_returns_name_and_age = '''
SELECT name, age
FROM bears
ORDER BY age ASC
LIMIT 1;

'''

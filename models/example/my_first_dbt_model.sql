/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

with source_data as (
    select "Survived", "Pclass", "Age",
           CASE WHEN t."Sex" = 'male' THEN 0 ELSE 1 END as Sex,
           "SibSp", "Parch", "Fare"
    from train t
    where "Age" is not null
)

select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
